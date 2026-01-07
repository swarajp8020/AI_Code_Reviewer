# 🩺 Gemini Code Doctor V2.0 (Enterprise Edition)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Microservice-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Security](https://img.shields.io/badge/Security-Rate%20Limited-orange)
![Status](https://img.shields.io/badge/Status-Live%20Demo-success)

**An Intelligent, Secure AI-Powered Code Migration & Debugging SaaS.**
*Capable of fixing bugs, explaining logic, and converting legacy code across Python, Java, C++, and Go.*

🔗 **[TRY THE LIVE DEMO HERE](https://aicodereviewer-swaraj.streamlit.app/)**

---

## 🏗️ System Architecture

This project implements a **Secure Cloud-Native Microservices Architecture** that decouples the user interface from the logic engine.

### **1. Frontend (The Face)**
* **Tech:** Streamlit (Python)
* **Role:** Handles user input, syntax highlighting, and securely manages API headers.
* **Security:** Silently passes the `X-Service-Token` to authenticate with the backend.

### **2. Backend (The Brain)**
* **Tech:** FastAPI (Python) on Render Cloud
* **Role:** Orchestrates the AI logic and enforces security policies.
* **AI Engine:** Integrated **Google Gemini 2.5 (Flash)** for low-latency reasoning.

---

## 🛡️ Enterprise Security Features

Unlike simple scripts, this API is fortified for production use:

* **🔐 Service-to-Service Authentication:**
    * Implements a strict **API Key Header (`X-Service-Token`)** policy.
    * The Backend rejects any request without the correct internal signature (403 Forbidden).
* **🛑 Rate Limiting (The Bouncer):**
    * Integrated **`slowapi`** (Token Bucket Algorithm) to prevent abuse.
    * Limits users to **5 requests per minute** by tracking IP addresses.
    * Returns `429 Too Many Requests` if the limit is breached.

---

## ⚡ Features

* **🐞 Auto-Debugging:** Instantly identifies syntax and logic errors.
* **🧠 Deep Explanations:** Returns a JSON "Bug Report" explaining *why* the code failed.
* **🔄 Multi-Language Support:**
    * 🐍 Python
    * ☕ Java
    * 🚀 C++
    * 🐹 Go
* **☁️ Resilience:** Implements exponential backoff strategies to handle AI latency.

---

## 🛠️ Local Installation

**1. Clone the Repository**
```bash
git clone [https://github.com/swarajp8020/AI_Code_Reviewer.git](https://github.com/swarajp8020/AI_Code_Reviewer.git)
cd AI_Code_Reviewer