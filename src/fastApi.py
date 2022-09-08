from detect import detect
from fastapi import FastAPI, File, UploadFile

import torch

app = FastAPI()


@app.post("/")
async def upload(file: UploadFile = File(...)):
    try:
        tempFileName = './temp.jpg'
        contents = await file.read()
        with open(tempFileName, 'wb') as f:
            f.write(contents)
        with torch.no_grad():
            result = detect(tempFileName)
            return {"message1": result}

    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()
