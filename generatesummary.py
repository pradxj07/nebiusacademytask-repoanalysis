from google import genai
import requests
import os
from validgithubfiletypes import GitHubFileTypes

## Function to get the API key from environment variable
def getapi_key():
    apikey=os.getenv("GEMINI_API_KEY")
    # print(apikey)

    return apikey

## Check if the url is valid and accessible before passing it to the Gemini model for analysis  
def checkURL(input_url=None):
    # Placeholder for the actual summarization logic

    # print(input_url)

    try:
        page = requests.get(input_url)
        # print(page.status_code)
        return True, input_url
    except (requests.exceptions.RequestException, requests.exceptions.HTTPError) as e:
        # print(e)
        output =  ("The provided URL is not accessible. " +
                   str(e) +   
                  " Please check the URL and try again."
        )
        return False, output
    except Exception as e:
        # print(e)
        output =  ("An unexpected error occurred. " +
                   str(e)    
        )
        return False, output

## Function to define the contents for the gemini-3-flas-preview model 
def setup_instructions(inputurl=None):
    # filetypes = GitHubFileTypes()
    # print(filetypes)
    excludeFileTypes = GitHubFileTypes().exclude_types()
    
    llm_question1 = """ 
        You are a github repository analyst. YOur job is to a given repository by using its URL. 
        Goal: Analyse the repository at given URL - """ + inputurl  + """ 
        (Note - If the repository is not accessible, do not analyse further provide the reason and error)
        During analysis, focus on the repository content but exclude the following files - 
        """ +   str(excludeFileTypes) +  """ 
        Expected output:  
          1. summary of the repository in maximum 2-3 sentences.  
          2. List the main technologies used in the repository. 
          3. get github repository structure and list the main files and folders in the repository.
        Sample JSON response:
        {
          "summary": "**Requests** is a popular Python library for making HTTP requests..."',
          "technologies": ["Python", "urllib3", "certifi"]',
          "structure": "The project follows a standard Python package layout with the main source code in `src/requests/`, tests in `tests/`, and documentation in `docs/`."',
        }                   
        """                             

    # print(llm_question1)
    return llm_question1

## Function to pass the url and instructions to gemini-3-flash-preview model and
## get the summary of the repository 
def generate_summary(input_url=None):

    isurlvalid, error = checkURL(input_url)

    # print(isurlvalid)

    if not isurlvalid:
        # print (error)
        return error
        
    try:
        client = genai.Client(api_key=getapi_key())

        input_instructions = setup_instructions(input_url)
        print("Input Instructions for model:", input_instructions)

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[{"text": "Summary of github repository at " + input_url + " as per instructions: " + str(input_instructions)}],
            config=genai.types.GenerateContentConfig(            
                thinking_config=genai.types.ThinkingConfig(thinking_level="low")
                # system_instruction=input_instructions
            )
        )

        # print(response)
        output = response.text
        
    except Exception as e:        
        output = str(e)
        print(f"An error occurred while generating summary: {output}. ")

    # Close the sync client to release resources.
    client.close()

    return output

# for testing the function independently
if __name__ == '__main__':
    # setup_instructions(inputurl="https://googleapis.github.io/python-genai/")
    generate_summary("https://googleapis.github.io/python-genaiabc/")
