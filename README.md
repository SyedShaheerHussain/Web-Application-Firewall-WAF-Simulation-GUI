# Web Application Firewall (WAF) Simulation

Monitors, Detects, and Blocks SQL Injection and XSS attacks in real time.

# 🛡️ Web Application Firewall (WAF) Simulation

**Developed By:** © **Syed Shaheer Hussain**

## 📘 Description

This project is a **fully functional Web Application Firewall (WAF) Simulation** built using **Python and FastAPI**, designed for **educational, demonstration, and learning purposes**. It simulates how a real-world WAF protects web applications from common web attacks such as **SQL Injection (SQLi)** and **Cross-Site Scripting (XSS)**.

The system acts as a **middleware layer** between users and a protected web application, inspecting every incoming request, detecting malicious payloads, blocking attacks, and visualizing traffic statistics through a modern web dashboard.

## 📷 Screenshots

![Screenshot 1]()

![Screenshot 2]()

![Screenshot 3]()

![Screenshot 4]()

![Screenshot 5]()

![Screenshot 6]()

## 🎯 Objectives

1. Understand how a WAF works internally
2. Detect and block SQL Injection & XSS attacks
3. Visualize allowed vs blocked traffic
4. Learn middleware-based security enforcement
5. Simulate real-world web security behavior
6. Provide an FYP / cybersecurity demo-ready project

## 🧠 Concepts Covered

* Web Security
* Web Application Firewall (WAF)
* SQL Injection (SQLi)
* Cross-Site Scripting (XSS)
* HTTP Middleware
* Pattern Matching (Regex)
* Traffic Monitoring
* Secure Coding Practices
* Cybersecurity Defense Simulation

## ❓ What is a WAF?

A **Web Application Firewall (WAF)** is a security layer that:

* Monitors HTTP/HTTPS traffic
* Filters malicious requests
* Blocks web-based attacks
* Protects backend applications and databases

🔐 **WAF sits between the client (browser) and the server (application).**

## 💡 Value of This Project

* Helps students understand **real-world web security**
* Demonstrates **attack detection logic**
* Ideal for **Final Year Projects (FYP)**
* Practical cybersecurity learning
* Extendable to ML-based detection

## 🏗️ Architecture

### 🔄 Request Flow

1. User sends request from browser
2. Request passes through WAF middleware
3. Payload extracted (query + body)
4. SQLi/XSS rules applied
5. Decision made (Allow / Block)
6. Stats updated
7. Dashboard updated

## 📊 Flow Chart (Textual)

```
Browser Request
      ↓
WAF Middleware
      ↓
Payload Normalization
      ↓
Rule Engine (SQLi / XSS)
      ↓
Decision
  ↓        ↓
Allow     Block
  ↓        ↓
App     Error Page

```
## 📂 Folder Structure

```
WAF-Project/
│
├── main.py              # FastAPI app & middleware
├── waf_engine.py        # Detection logic
├── rules.py             # SQLi & XSS regex patterns
├── logger.py            # Attack logging
├── templates/
│   ├── login.html
│   └── dashboard.html
├── static/
│   └── style.css
├── logs/
│   └── attacks.log
├── requirements.txt
└── README.md

```

## 🛠️ Technologies Used

* 🐍 Python 3.10+
* ⚡ FastAPI
* 🌐 HTML5, CSS3, JavaScript
* 📊 Chart.js
* 🔍 Regex-based Detection
* 🧪 REST APIs

## 🧪 Features

1. ✅ SQL Injection detection
2. ✅ XSS attack detection
3. 📊 Live traffic visualization
4. 🚫 Automatic request blocking
5. 📈 Allowed vs Blocked graph
6. 🧾 Attack logging
7. 🧪 Manual payload testing
8. 🎓 Educational dashboard

## ⚙️ Functions & Modules

### 🔹 `detect_attack(payload)`

* Scans payload for SQLi/XSS
* Uses regex rules
* Returns verdict

### 🔹 Middleware

* Intercepts every HTTP request
* Applies WAF logic
* Blocks malicious traffic

### 🔹 `/test` Endpoint

* Manual testing of payloads
* Simulates attacks

### 🔹 `/stats` Endpoint

* Returns allowed/blocked counts

## 🧑‍💻 Installation (Step-by-Step)

### 1️⃣ Install Python

Download Python from:
[https://www.python.org](https://www.python.org)

✔ Make sure **Add Python to PATH** is checked

### 2️⃣ Install Dependencies

```
pip install fastapi uvicorn jinja2

```

### 3️⃣ Project Setup

```
cd waf_simulation

```

## ▶️ How to Run

```
uvicorn main:app --reload

```
Expected output:

```
Running on http://127.0.0.1:8000

```

## 🌐 How to Open (Chrome)

1. Open Google Chrome
2. Go to:

```
http://127.0.0.1:8000

```

## 🔐 Login Details

```
Username: admin
Password: admin123

```

## 🧪 How to Use

1. Login to dashboard
2. Enter payload in text box
3. Click **Detect**
4. View result (Allowed / Blocked)
5. Watch graph update automatically

## 💥 Example Payloads

### ❌ SQL Injection

```
' OR 1=1 --

```

### ❌ XSS

```
<script>alert(1)</script>
```

### ✅ Normal Input

```
hello world

```

## ⚠️ Cautions

> [!caution]
> * This is a **simulation**, not a production WAF
> * Regex-based detection has limitations
> * Do not deploy on live servers

## 📌 Important Notes

* Designed for **learning & demo purposes**
* Easily extendable
* Clean & modular code

## 📢 Disclaimer

> [!note]
> This project is intended **strictly for educational and research purposes**. The developer is not responsible for misuse of this system.

## 🚀 Future Enhancements

1. 🤖 Machine Learning-based detection
2. 🔐 Role-based access control
3. 🌍 IP reputation system
4. 📄 PDF attack reports
5. ⏱️ Time-series traffic graphs
6. 🧪 Automated attack generator

## 🏁 Conclusion

This WAF Simulation provides a **clear, realistic, and interactive understanding** of how modern web security systems defend against common attacks. It bridges the gap between theory and practical cybersecurity implementation.

## © Copyright

© 2026 **Syed Shaheer Hussain**

All rights reserved.
