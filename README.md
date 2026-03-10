# nebiusacademytask-repoanalysis
Code related to task for nebius academy assessment

## Overview 
This repository an API that takes in a githubrepository URL and summarises the contents. The API has been built using the Flask framework. 

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
2. Following dependencies were installed in the virtual environment. These dependencies are mentioned in the file requirements.txt

2. LLM used: gemini-3-flash-preview because I have some experience of using it and it seems to give results quite quickly. Also, no cost required for tokens as Google's threshold is quite high <https://ai.google.dev/gemini-api/docs/rate-limits>. 

## Application
The zip file repoanalysis has folder repoanalysis, which contains following files - 
1. analyserepo.py - This is the main file which creates the api in the form of a Flask app "analyserepo" and home (/) and /sumarize endpoints for the api. The api will run on localhost [127.0.0.1 (IPv4)] , port 5001
2. generatesummary.py - module that contaisn the functionaility to call the gemini model and generate summary for the given github url
3. validgithubfiletypes.py - This is a helper file created using AI to list the filetypes to be excluded during the repo analysis. 
4. README.md - i.e. This file
5. requirements.txt - list of dependencies required for the api   
6. prepapp - optional script to run few command to setup the virtual environment 

## Installing the application
* These instructions has been tested using windows explorer and bash shell in vscode. * 
1. In your machine, Download the application zip named repoanalysis and extract the files. This will create new folder repoanalysis. Open a bash terminal and navigate to repoanalysis folder. 

2. If the python version in your machine is not 3.10+, please follow the instructions on https://www.python.org/downloads/ to upgrade it. 

else go to step 3 directly.

3. Opena a bash or other terminal where you can run the following commands. Go to the folder repoanalysis and run the following commands.  
```
python -m venv .venv

source .venv/Scripts/activate

pip install -r requirements.txt
```

Alternatively, you may run the script runapp, using the command in a bash terminal - 
```
source prepapp   
```

### Setting up API key 
1. To use Google gemini models in the analyserepo, an API key is required. To create the API key, please follow the instructions [here]( https://ai.google.dev/gemini-api/docs/quickstart#before_you_begin) 
2. In the given machine, please create an environment variable - GEMINI_API_KEY and save the value of the key created in step 1 in this environment variable.   
        - If using bash, please use - export VARNAME="my value" (this will create the key in current environment)
        - If using Windows, please create an environment variable as per [this page](https://docs.progress.com/bundle/openedge-sql-development/page/Set-environment-variables-in-Windows.html)

## Running the application 

1. In the bash terminal, Run the command - 
```
python -m flask --app analyserepo run 
```
or - 
```
python -m flask --app analyserepo run --debug
```

The server with the Flask API is programmed to run on localhost at http://127.0.0.1:5000. 

2. Open a new terminal (similar to step 1 above) and run the command to send a POST request to the API - 


```
curl localhost:5000/summarize -X POST -d '{"github_url": "https://github.com/tcltk/tcl"}' -H 'Content-Type: application/json'

````

**Expected output**  

```
POST request received in summarize endpoint. Generated summary: ```json
{
  "summary": "Tcl (Tool Command Language) is a mature, high-level, and extensible dynamic programming language designed for a wide range of uses including web and desktop applications, networking, and administration. This repository contains the official source code for the Tcl interpreter, its core library, and the build systems required for cross-platform deployment.",
  "technologies": [
    "C",
    "Tcl",
    "Autoconf",
    "Make",
    "NMake",
    "M4"
  ],
  "structure": "The repository is organized into platform-specific and platform-independent directories: `generic/` contains the core C source code, while `unix/`, `win/`, and `macosx/` house platform-specific implementations and build files. The `library/` directory contains the standard Tcl script library, `tests/` contains the extensive test suite, and `doc/` includes the official manual pages."
}
```


**Expected message in case of error** 

```
POST request received in summarize endpoint. Generated summary: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
```
3. In the above curl command, Change the github_url to the one you wish to analyse and run the curl command again to see the results. 