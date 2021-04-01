from fastapi import FastAPI
from env_config import DEBUG

app = FastAPI(debug=DEBUG)

@app.get("/", tags=["Root"])
async def read_root():
  return {"message": "Hello, World!"}