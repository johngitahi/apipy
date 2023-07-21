import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# cors policy
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_phrases_from_file():
    with open("file.TXT", "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

phrases = read_phrases_from_file()

@app.get("/api")
def get_message():
    phrase = random.choice(phrases)
    return {"message": f"John Gitahi is thinking {phrase} right now"}

