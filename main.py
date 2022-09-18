from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q}

uvicorn.run(app,host="0.0.0.0",port="8080")