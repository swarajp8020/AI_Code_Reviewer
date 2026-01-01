import streamlit as st
import requests

st.set_page_config(page_title="Gemini Code Doctor", page_icon="🩺", layout="centered")

# --- HEADER ---
st.title("🩺 Gemini Code Doctor")
st.write("### AI-Powered Python Debugger")
st.info("Built with FastAPI, Streamlit, and Google Gemini 2.5")

# --- INPUT AREA ---
code_input = st.text_area("Paste your broken Python code here:", height=250)

# --- ACTION BUTTON ---
if st.button("Analyze & Fix 🚑", type="primary"):
    if not code_input:
        st.warning("⚠️ Please paste some code first!")
    else:
        with st.spinner("🤖 AI is analyzing your logic..."):
            try:
                # connect to the local backend
                response = requests.post(
                    "http://127.0.0.1:8000/review", 
                    json={"code": code_input}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    fixed_code = data.get("fixed_code", "# No code returned")
                    
                    st.success("✅ Analysis Complete!")
                    
                    st.subheader("Your Fixed Code:")
                    st.code(fixed_code, language="python")
                else:
                    st.error(f"❌ Server Error: {response.status_code}")
                    
            except Exception as e:
                st.error(f"❌ Connection Failed. Is the backend running?\nError: {e}")