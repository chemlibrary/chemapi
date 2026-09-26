"""
REQUIREMENTS:
python3 -m pip install fastapi[standard]

USAGE:
uv run fastapi dev
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}