from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


@app.get("/name/{name}")
def read_item(name: str):
    return {f"Hello {name} !! Welcome to FastAPI! "}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, reload=True, workers=1)
