import os
import re
import time
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def generate_chat(prompt, system):
    max_retry = 5
    retry = 0

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt},
    ]

    while retry < max_retry:
        try:
            print("Creating chat with OpenAI API...")

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )

            text = response.choices[0].message.content.strip()
            text = re.sub("\s+", " ", text)

            # Generate a unique filename based on the current time
            filename = f"{time.strftime('%Y%m%d-%H%M%S')}_gpt3.txt"

            # Ensure the directory exists
            log_dir = ".logs/gpt_logs"
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            # Write the logs to the file
            with open(f"{log_dir}/{filename}", "w", encoding="utf-8") as outfile:
                outfile.write(
                    f"System prompt: ===\n{system}\n===\n"
                    + f"Chat prompt: ===\n{prompt}\n===\n"
                    + f"RESPONSE:\n====\n{text}\n===\n"
                )

            return text
        except Exception as error:
            print("Chat API Error:", error)
            retry += 1
            time.sleep(1)
