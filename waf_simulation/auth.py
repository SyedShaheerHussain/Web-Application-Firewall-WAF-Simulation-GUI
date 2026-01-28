# auth.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

SECRET_KEY = "waf-secret"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "viewer": {"password": "viewer123", "role": "viewer"}
}

def authenticate_user(username: str, password: str):
    user = USERS.get(username)
    if not user or user["password"] != password:
        return None

    token = jwt.encode(
        {"sub": username, "role": user["role"]},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
