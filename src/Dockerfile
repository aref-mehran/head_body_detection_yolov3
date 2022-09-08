FROM python
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY ./weights/best.pt /home//best.pt
COPY requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt
WORKDIR  /home/
RUN git clone https://github.com/aref-mehran/head_body_detection_yolov3.git
RUN cp /home/best.pt /home/head_body_detection_yolov3/weights/
WORKDIR  /home/head_body_detection_yolov3/
RUN chmod +x ./init.sh