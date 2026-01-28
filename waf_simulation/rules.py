STRICTNESS = 2 # 1=Low, 2=Medium, 3=High
SQLI_PATTERNS = [
    r"(?i)(union\s+select)",
    r"(?i)(or\s+1=1)",
    r"(?i)(--|#|/\\*)",
    r"(?i)(sleep\()",
    r"(?i)(information_schema)"
    r"--",
    r"or\s+1=1",
    r"union\s+select",
    r"sleep\\(",
r"sleep\s*\("
]


XSS_PATTERNS = [
    r"<\s*script.*?>.*?<\s*/\s*script\s*>",
    r"on\w+\s*=",
    r"javascript\s*:",
    r"<\s*img.*?onerror\s*=",
    r"<\s*svg.*?onload\s*=",
    r"document\.cookie",
    r"alert\s*\(",
    r"<\s*script",
    r"on\w+\s*=",
    r"javascript:",
    r"on\\w+\\s*=",
r"<\s*svg"
]
