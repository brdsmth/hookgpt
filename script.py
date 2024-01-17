# #!/usr/bin/env python3
from mygpt.get_openai_response_and_log import get_openai_response_and_log


prompt = "What is the US Independence Day?"
system = "You are an AI that can give the answer to anything"
response = get_openai_response_and_log(prompt, system)
print(response)
