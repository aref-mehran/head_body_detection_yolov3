import detect
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    result = detect.detect()
    return {"message1": result}
