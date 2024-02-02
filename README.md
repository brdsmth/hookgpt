## Introduction

This is a project for interacting with the OpenAI ChatGPT API.

### Usage

This project uses `python3` and `pip3`.

Create virtual environment

`python3 -m venv .venv`

Activate virtual environment

`source .venv/bin/activate`

Environment variables

```python
OPENAI_API_KEY="your api key"
```

Install requirements:

`pip3 install -r requirements.txt`

To generate a chat:

- Specify the `mode` to be `chat` and include your prompt as an argument.

`python3 script.py chat "how many inches in a foot"`

To generate an image:

- Specify the `mode` to be `image` and include your prompt as an argument.

`python3 script.py image "workaholic"`

#### Running the Server

To run the HookGPT server:

`uvicorn api:app --port 9000 --reload`

### Notes

Activate virtual environment

`source .venv/bin/activate `

Format `python` files

`black .`

This script writes a log of all interactions with `ChatGPT` to a local `.logs` directory
