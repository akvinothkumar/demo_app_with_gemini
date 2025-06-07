from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Can't find the GEMINI_API_KEY in environment variables.")

genai.configure(api_key=GEMINI_API_KEY)
# to_check_the_existing_models_to_serve
# for m in genai.list_models():
#     print(
#         f"Name: {m.name}, supports generation: {'generateContent' in m.supported_generation_methods}"
#     )
model = genai.GenerativeModel("gemini-1.5-flash")
