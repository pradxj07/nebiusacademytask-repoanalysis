from dotenv import find_dotenv
from flask import Flask, request

def load_env_variables():
  from dotenv import load_dotenv, find_dotenv
  import os

  load_dotenv(find_dotenv())
  print(os.getenv("GEMINI_API_KEY"))

def generate_summary():
   # Placeholder for the actual summarization logic
  from google import genai

  client = genai.Client()

  response = client.models.generate_content(
      model="gemini-3-flash-preview",
      contents="Explain how AI works in a few words",
  )

  print(response.text)

  return response.text

app = Flask(__name__)

@app.route('/')
def home():
  # home endpoint
    return "<h1>GitHub Repository Analysis API</h1>"

@app.route('/summarize', methods=['POST'])
def call_to_summarize():
  if request.method == 'POST':
    load_env_variables()
    output = generate_summary()
    combined = "POST request received in summarize endpoint. Generated summary: " + output
    return combined
  else:
    return "No other method allowed other than POST "


if __name__ == '__main__':
  print("Starting the Flask app...")    
  app.run(host='127.0.0.0', port=5000, debug=True)