# nebiusacademytask-repoanalysis
Code related to task for nebius academy assessment

## Overview 
This task is about creating an API that takes in a githubrepository URL and summarises the contents. 
The API has been built using the Flask framework. 

The expected input and output parameters are as follows:

Input - Request 
    Expected JSON body: {'github_url': 'https://github.com/username/repositoryname'}

Output - Response JSON with following contents 
{
  "summary": "**Requests** is a popular Python library for making HTTP requests...",
  "technologies": ["Python", "urllib3", "certifi"],
  "structure": "The project follows a standard Python package layout with the main source code in `src/requests/`, tests in `tests/`, and documentation in `docs/`."
}

## Dependencies - 

1. Language required: Python 3.10+ : Assumption - It is assumed that Python 3.10+ is already installed in the environment where the API will be tested. 
2. Following dependencies were installed in the virtual environment. These dependencies are mentioned in the requirements.txt
 
    a. Web framework: Flask

2. LLM: Nebius Token Factory API or an alternative LLM provider You choose which LLM model to use from the available models on Nebius Token Factory or an alternative LLM provider - Google gemini

# Installing the application
* These instructions have been tested using windows explorer and bash shell. * 
1. In windows File explorer, create a folder named repoanalysis to save the application files.
2. Download the application zip and extract the files to the new folder repoanalysis 

2. Open a bash terminal and run the following command  to confirm the python version is 3.10+ or more 
which python

3. If the python version is not updated, please follow the instructions on https://www.python.org/downloads/

else go to step 4 directly.

3. In the bash terminal, 
```
python -m venv .venv
```

```
source .venv/Scripts/activate
```

```
pip install -r requirements.txt
```

###API key 
1. In the project folder, create a new .env file. Copy the contents of examples\.env.example to .env file.  
2. Update the GOOGLE-API-KEY by replacing the text your-google-api-key-here with your  own api key value. (To create the API key, please follow the instructions here - https://ai.google.dev/gemini-api/docs/quickstart#before_you_begin) 

## Running the application 

1. To run the program, download the code. 
2. In python environment, run the command - 
```
python -m flask --app analyseapi run
```

The server is programmed to run on localhost at http://127.0.0.1:5001 or 5000???????. If the host 5001 is already used by , please follow the instructions given https://flask.palletsprojects.com/en/stable/server/#address-already-in-use to resolve the same. 

```
curl localhost:5000/summarize -X POST -d '{"github_url": "https://github.com/tcltk/tcl"}' -H 'Content-Type: application/json'
````