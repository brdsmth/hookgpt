## Introduction

This is a project for interacting with the OpenAI ChatGPT API.

### Usage

Environment variables

```python
OPENAI_API_KEY=
```

This project uses `python3` and `pip3`

Install requirements:

`pip3 install requirements.txt`

To generate a chat:

- Specify the `mode` to be `chat` and include your prompt as an argument.

`python3 script.py chat "how many inches in a foot"`

To generate an image:

- Specify the `mode` to be `image` and include your prompt as an argument.

`python3 script.py image "workaholic"`

### Notes

Activate virtual environment

`source .venv/bin/activate `

Format `python` files

`black .`

This script writes a log of all interactions with `ChatGPT` to a local `.logs` directory
