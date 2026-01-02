from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import google.generativeai as genai
import uvicorn
import config 
import logging

logging.basicConfig(
    filename='server.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 1. Setup the "Brain" (Gemini)
genai.configure(api_key=config.GEMINI_API_KEY)
# REPLACE "gemini-..." WITH A NAME FROM YOUR LIST
model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()

# 2. Define the Form
class codeRequest(BaseModel):
    code: str
    # The Guard Dog Function
    @field_validator('code')
    def check_code_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Code cannot be empty/blank!')
        return v
@app.get("/")
def greet():
    return {"message": "Gemini AI Server is Running 🟢"}

# 3. The Real Logic
@app.post("/review")  # <--- Renamed to match your Client!
def review_code(request: codeRequest):
    logging.info(f"\n--- 📨 Received Code (Length: {len(request.code)}) ---")
    
    # A. The Instructions for the AI
    prompt = f"""
    You are a Python Expert. 
    Fix the following Python code.
    Return ONLY a JSON object with this format:
    {{ "fixed_code": "YOUR_FIXED_CODE_HERE" }}
    
    The Buggy Code:
    {request.code}
    """
    attempts = 0
    max_retries = 2
    while attempts < max_retries:
        try:
            # B. Send to Google
            logging.info("--- 🤖 Asking Gemini... ---")
            response = model.generate_content(prompt)
            # C. Clean the text (Remove ```json and ```)
            cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
            
            # D. Return the result to the Client
            # We manually parse it to dictionary to be safe, or just return the raw text if you prefer.
            # For now, let's use eval() carefully or just trust the structure.
            # Ideally, we use json.loads, but let's keep it simple:
            import json
            data = json.loads(cleaned_text)
            logging.info("--- ✅ Fix Sent! ---")
            return data

        except Exception as e:
            logging.error(f"❌ Error: {e}")
            return {"fixed_code": "# Error: AI could not generate valid JSON after retries."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)