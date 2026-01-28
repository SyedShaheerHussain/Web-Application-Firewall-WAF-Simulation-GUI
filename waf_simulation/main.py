from fastapi import FastAPI, Request, WebSocket, Form
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from waf_engine import detect_attack
from logger import log_attack
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

stats = {"allowed":0,"blocked":0}
clients = []
USERS = {"admin":"admin123","viewer":"viewer123"}

# WAF Middleware
@app.middleware("http")
async def waf_middleware(request: Request, call_next):
    payload = str(request.query_params)
    if request.headers.get("content-type","").startswith("application/json"):
        body = await request.body()
        payload += body.decode(errors="ignore")

    verdict, attack, rule = detect_attack(payload)
    ip = request.client.host if request.client else "Unknown"

    if verdict == "Blocked":
        stats["blocked"] += 1
        log_attack(ip, payload, attack, rule)
        await broadcast()
        return JSONResponse({"status":"blocked","attack":attack},status_code=403)

    stats["allowed"] += 1
    await broadcast()
    return await call_next(request)

# WebSocket for live chart
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    await ws.send_text(json.dumps(stats))
    try:
        while True:
            await ws.receive_text()  # keep connection alive
    except:
        clients.remove(ws)

async def broadcast():
    for ws in clients:
        try:
            await ws.send_text(json.dumps(stats))
        except:
            clients.remove(ws)

# Login / Dashboard
@app.get("/", response_class=RedirectResponse)
async def root():
    return RedirectResponse("/login")

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username in USERS and USERS[username]==password:
        response = RedirectResponse("/dashboard",status_code=302)
        response.set_cookie(key="user", value=username)
        return response
    return templates.TemplateResponse("login.html", {"request": request, "error":"Invalid credentials"})

@app.get("/dashboard")
async def dashboard(request: Request):
    user = request.cookies.get("user")
    if not user:
        return RedirectResponse("/login")
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})

# Manual test endpoint
@app.post("/test")
async def test_payload(data: dict):
    payload = data.get("payload","")
    verdict, attack, rule = detect_attack(payload)

    if verdict=="Blocked":
        stats["blocked"] +=1
        await broadcast()
        return {"status":"blocked","attack":attack}

    stats["allowed"] +=1
    await broadcast()
    return {"status":"allowed"}
@app.get("/stats")
async def get_stats():
    return stats
