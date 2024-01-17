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


def generate_image(prompt, system):
    max_retry = 5
    retry = 0

    while retry < max_retry:
        try:
            print("Creating image with OpenAI API...")

            response = client.images.generate(prompt=prompt, n=1, size="1024x1024")

            url = response.data[0].url
            text = re.sub("\s+", " ", url)

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
                    + f"Image prompt: ===\n{prompt}\n===\n"
                    + f"RESPONSE:\n====\n{text}\n===\n"
                )

            return text
        except Exception as error:
            print("Image API Error:", error)
            retry += 1
            time.sleep(1)
