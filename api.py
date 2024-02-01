import argparse
from fastapi import FastAPI, HTTPException, Query, Request
from mygpt.generate_chat import generate_chat
from mygpt.generate_image import generate_image

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to your API!"}


@app.post("/generate/")
async def generate_content(
    request: Request,
):
    data = await request.json()

    mode = data.get("mode")
    prompt = data.get("prompt")
    system = data.get("system")

    if not mode or mode not in ["chat", "image"]:
        raise HTTPException(
            status_code=400, detail="Invalid mode. Choose 'chat' or 'image'."
        )

    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required.")

    if not system:
        system = "You are an AI that can give the answer to anything"

    if mode == "chat":
        response = generate_chat(prompt, system)
    elif mode == "image":
        response = generate_image(prompt, system)

    return {"response": response}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
