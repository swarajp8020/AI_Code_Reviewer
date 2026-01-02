# 🩺 Gemini Code Doctor - https://aicodereviewer-swaraj.streamlit.app/

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red)
![Status](https://img.shields.io/badge/Status-Live%20Demo-success)

**An Intelligent, AI-Powered Code Migration & Debugging Assistant.**
*Capable of fixing bugs and converting legacy code across Python, Java, C++, and Go.*

🔗 **[Live Demo Application](https://aicodereviewer-swaraj.streamlit.app/)**

---

## 🏗️ System Architecture

This project implements a **Cloud-Native Microservices Architecture** to decouple the user interface from the logic engine.

1.  **Frontend (The Face):** Built with **Streamlit**, deployed on Streamlit Community Cloud. It handles user input and displays real-time feedback.
2.  **Backend (The Brain):** A high-performance **FastAPI** server hosted on **Render**. It manages:
    * **Prompt Engineering:** Dynamic context injection based on the selected language.
    * **Resilience:** Custom retry logic with exponential backoff to handle LLM latency.
    * **Validation:** Pydantic models ensure rigorous data schema enforcement.
3.  **AI Engine:** Powered by **Google Gemini 2.5 (Flash)** for low-latency code reasoning.

---

## ⚡ Features

* **🐞 Auto-Debugging:** Instantly identifies syntax and logic errors.
* **🧠 Deep Explanations:** Returns a "Bug Report" explaining *why* the code failed, not just the fix.
* **🔄 Multi-Language Support:**
    * 🐍 Python
    * ☕ Java
    * 🚀 C++
    * 🐹 Go
* **☁️ Production Ready:** Fully deployed with separate frontend/backend services communicating via REST API.

---

## 🛠️ Installation & Local Setup

If you want to run this locally:

**1. Clone the Repository**
```bash
git clone [https://github.com/swarajp8020/AI_Code_Reviewer.git](https://github.com/swarajp8020/AI_Code_Reviewer.git)
cd AI_Code_Reviewer
