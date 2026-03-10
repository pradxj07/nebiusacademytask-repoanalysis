# from dotenv import find_dotenv
from flask import Flask, request
import requests
import validators
from validators import url
import generatesummary
import json
from werkzeug.exceptions import HTTPException

# check if url is in valid format 
def validate_url(url):
  import validators

  isvalid, errormsg = None, ""
  isvalid = validators.url(url)

  if isvalid:
    try: 
      # geturl = url(url)
      checkresponse = requests.get(url)
      print(f"URL: {url}, Status code: {checkresponse.status_code}")
      if checkresponse.status_code == 200:
        print('{} is active'.format(url))
      else:
        errormsg = f'{url} is not active. Error: {checkresponse.status_code}: {checkresponse.reason}'
        isvalid = False
    except requests.exceptions.RequestException as e:
      errormsg = f'{url} is not active. Error: {e}'
      isvalid = False

  return isvalid, errormsg

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
  # home endpoint
    return "<h1>GitHub Repository Analysis API</h1>"

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route('/summarize', methods=['POST'])
def call_to_summarize():
  if request.method == 'POST':
    # load_env_variables()
    inp = request.get_json() # to consume the json body in the request, even if we are not using it here. 
    # This is to avoid "400 bad request" error when we send a 
    # print(inp)
    input_url = inp.get("github_url", "")
    isurlvalid, errormsg = validate_url(input_url)
    # print(f"Main isurlvalid : {isurlvalid}")
    # call function to summarize the github repository only if url appears to be valid
    if isurlvalid:
      output = generatesummary.generate_summary(input_url)
      finaloutput = "POST request received in summarize endpoint. Generated summary: " + output
    else: 
      finaloutput = (errormsg if errormsg else " ") + "\nThe provided URL is not valid. Please provide a valid URL and try again."
    return finaloutput
  else:
    return "No other method allowed other than POST "

if __name__ == '__main__':
  # print("Starting the Flask app...")    
  # app.run(host='127.0.0.1', port=5001, debug=True)
  app.run(host='127.0.0.1', port=5000)