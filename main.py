from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/campaign")
def list_campaign():
  return {"campaign": [
    {
      "id": 1,
      "name": "2022 fall dues",
      "description": "chapter dues",
      "category": "dues",
      "startDate": "2022-06-01 00:00:00",
      "endDate": "2022-09-30 23:59:59",
      "fundingGoal": 2500.52
    },
    {
      "id": 2,
      "name": "2023 spring dues",
      "description": "chapter dues",
      "category": "dues",
      "startDate": "2022-01-01 00:00:00",
      "endDate": "2022-04-30 23:59:59",
      "fundingGoal": 1000
    }
  ]}
    

@app.get("/campaign/{id}")
def read_campaign(id: int):
  return {
    "id": id,
    "name": "2023 fall dues",
    "description": "chapter dues",
    "category": "dues",
    "startDate": "2022-06-01 00:00:00",
    "endDate": "2022-09-30 23:59:59",
    "fundingGoal": 2500.52
  }
  


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
