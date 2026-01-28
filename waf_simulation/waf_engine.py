import re
import html

SQLI_PATTERNS = [r"or\s+1=1",r"union\s+select",r"drop\s+table",r"--"]
XSS_PATTERNS = [r"<\s*script",r"javascript\s*:",r"on\w+\s*=",r"<\s*img",r"alert\s*\("]

def normalize(payload:str)->str:
    return html.unescape(payload.lower())

def detect_attack(payload:str, enable_ml=False):
    payload = normalize(payload)
    for rule in SQLI_PATTERNS:
        if re.search(rule,payload):
            return "Blocked","SQL Injection",rule
    for rule in XSS_PATTERNS:
        if re.search(rule,payload):
            return "Blocked","XSS",rule
    return "Allowed", None, None
