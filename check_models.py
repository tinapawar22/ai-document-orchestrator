import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyADgAQh3GHlrUPYHzhyhwP9usVoIlNnqP8"))

for m in genai.list_models():
    print(m.name)