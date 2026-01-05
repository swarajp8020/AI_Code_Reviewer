import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel, field_validator
import uvicorn
import logging
import json

# --- 1. SETUP LOGGING & CONFIG ---
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Get Gemini Key
try:
    from config import GEMINI_API_KEY
    api_key = GEMINI_API_KEY
except ImportError:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No API Key found! Set GEMINI_API_KEY environment variable.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# --- 2. SECURITY CONFIGURATION (THE LOCK) 🔒 ---
API_KEY_NAME = "X-Service-Token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# The Secret Password
INTERNAL_TOKEN = os.getenv("INTERNAL_TOKEN", "SWARAJ_SECURE_2026")

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == INTERNAL_TOKEN:
        return api_key_header
    else:
        raise HTTPException(
            status_code=403, 
            detail="⛔ Access Forbidden: Invalid or Missing Service Token"
        )

# --- 3. INITIALIZE APP ---
app = FastAPI()

# --- 4. DATA MODELS ---
class CodeRequest(BaseModel):
    code: str
    task: str = "fix_python" # Default

    @field_validator('code')
    def check_code_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Code cannot be empty/blank!')
        return v

# --- 5. ENDPOINTS ---
@app.get("/")
def greet():
    return {"message": "Gemini AI Server is Running 🟢"}

@app.post("/review", dependencies=[Depends(get_api_key)]) # <--- LOCKED 🔒
def review_code(request: CodeRequest):
    logging.info(f"Received Request: {request.task}")

    prompts = {
        "fix_python": "Fix this Python code. Explain the bugs.",
        "fix_java": "Fix this Java code. Explain the bugs.",
        "fix_cpp": "Fix this C++ code. Explain the bugs.",
        "fix_go": "Fix this Go code. Explain the bugs.",
    }
    
    instruction = prompts.get(request.task, "Fix this code.")

    prompt = f"""
    You are a Senior Developer. {instruction}
    
    Return ONLY a JSON object with this EXACT format:
    {{
        "fixed_code": "PUT_THE_FIXED_CODE_HERE",
        "bug_report": "Explain WHAT was wrong and WHY it caused an error."
    }}
    
    The Buggy Code:
    {request.code}
    """

    attempts = 0
    max_retries = 2

    while attempts < max_retries:
        try:
            logging.info(f"Attempt {attempts+1}...")
            response = model.generate_content(prompt)
            
            text = response.text.replace("```json", "").replace("```", "").strip()
            data = json.loads(text)
            return data

        except Exception as e:
            logging.error(f"Error: {e}")
            attempts += 1
            
    return {
        "fixed_code": request.code, 
        "bug_report": "Server is busy or AI failed to format JSON. Please try again."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))