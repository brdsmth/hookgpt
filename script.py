# #!/usr/bin/env python3
import argparse
from mygpt.generate_chat import generate_chat
from mygpt.generate_image import generate_image

# Set up the argument parser
parser = argparse.ArgumentParser(description="Generate content using OpenAI's API")
parser.add_argument(
    "mode", choices=["chat", "image"], help="Mode of generation: chat or image"
)
parser.add_argument("prompt", help="Prompt for the AI")
parser.add_argument(
    "--system",
    default="You are an AI that can give the answer to anything",
    help="System message for chat (optional)",
)

# Parse command line arguments
args = parser.parse_args()

# Call the appropriate function based on the mode argument
if args.mode == "chat":
    response = generate_chat(args.prompt, args.system)
elif args.mode == "image":
    response = generate_image(args.prompt, args.system)
else:
    raise ValueError("Invalid mode. Choose 'chat' or 'image'.")

print(response)
