FROM python
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY ./weights/best.pt /home//best.pt
COPY requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt
