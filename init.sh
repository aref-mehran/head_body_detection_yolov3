#!/bin/bash
pip install fastapi[all]
uvicorn fastApi:app  --host 0.0.0.0 --port 8000 --reload