from detect import detect
from fastapi import FastAPI
import torch

app = FastAPI()


@app.get("/")
async def root():

   with torch.no_grad():
       result = detect()
       return {"message1": result}
