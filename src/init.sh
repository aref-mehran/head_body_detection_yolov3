#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
pip install gdown
mkdir $SCRIPT_DIR/weights
gdown 12Rq-pTAPz5ulxnWGZa6h1JxgRVBr5tc8 -O $SCRIPT_DIR/weights/best.pt
pip install fastapi[all]
uvicorn fastApi:app  --host 0.0.0.0 --port 8000 --reload
#dfdfdfdf
