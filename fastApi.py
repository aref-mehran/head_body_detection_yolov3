from detect import detect
from fastapi import FastAPI, File, UploadFile

import torch

app = FastAPI()


@app.get("/")
async def root():

   with torch.no_grad():
       result = detect()
       return {"message1": result}


@app.post("/inference")
async def upload(file: UploadFile = File(...)):
    try:
        tempFileName = './temp.jpg'
        contents = await file.read()
        with open('./temp.jpg', 'wb') as f:
            f.write(contents)
        with torch.no_grad():
            result = detect(tempFileName)
            return {"message1": result}

    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()
