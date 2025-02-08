# Basic Retrieval Augmented Generation App

A basic web application that answers questions based on the URL you provide to it. It works by providing a URl to the app. It scraps data from a URL, which is then fed to `llama3.2` running locally. The LLM will then be able to answer questions setting the contents of that URL as the main context.

## Pre-requsites

- Must have `Ollama` installed locally in your machine. You can install Ollama from this link: https://ollama.com/
- Must have `llama3.2` installed. Run the following command after installing `Ollama`

```
ollama run llama3.2
```

- Insure you have python version 3.10 installed.

## Installation Steps

- Create a virtual environment. Run the following command to create the virtual environment

```
conda env -p venv python=3.10
```

- Once an environment is created, install the necessary packages from `requirements.txt` file. Run the following command:

```
pip install -r requirements.txt
```

- After finishing dependency installation, run the following command:

```
streamlit run app.py
```
