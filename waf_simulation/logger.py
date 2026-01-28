# logger.py
from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

def log_attack(ip, payload, attack, rule):
    with open("logs/attacks.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {ip} | {attack} | {rule} | {payload}\n")
