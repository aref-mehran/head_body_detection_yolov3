from detect import detect
from fastapi import FastAPI
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cfg', type=str,
                    default='cfg/yolov3-spp.cfg', help='*.cfg path')
parser.add_argument(
    '--names', type=str, default='/home/allen/Desktop/yolo/YOLO_V3_TRAIN/yolov3/data/humanface.names', help='*.names path')
parser.add_argument('--weights', type=str,
                    default='/home/allen/Desktop/yolo/YOLO_V3_TRAIN/yolov3/weights/best.pt', help='weights path')
# input file/folder, 0 for webcam
parser.add_argument(
    '--source', type=str, default='/home/allen/Downloads/track2.2_test_sample', help='source')
parser.add_argument('--output', type=str, default='output',
                    help='output folder')  # output folder
parser.add_argument('--img-size', type=int, default=512,
                    help='inference size (pixels)')
parser.add_argument('--conf-thres', type=float,
                    default=0.3, help='object confidence threshold')
parser.add_argument('--iou-thres', type=float,
                    default=0.6, help='IOU threshold for NMS')
parser.add_argument('--fourcc', type=str, default='mp4v',
                    help='output video codec (verify ffmpeg support)')
parser.add_argument('--half', action='store_true',
                    help='half precision FP16 inference')
parser.add_argument('--device', default='',
                    help='device id (i.e. 0 or 0,1) or cpu')
parser.add_argument('--view-img', action='store_true',
                    help='display results')
parser.add_argument('--save-txt', action='store_true',
                    help='save results to *.txt')
parser.add_argument('--classes', nargs='+',
                    type=int, help='filter by class')
parser.add_argument('--agnostic-nms', action='store_true',
                    help='class-agnostic NMS')
parser.add_argument('--augment', action='store_true',
                    help='augmented inference')
# opt = parser.parse_args()

opt, unknown = parser.parse_known_args()


app = FastAPI()


@app.get("/")
async def root():
    opt.weights = './weights/best.pt'
    opt.source = 'people_counting/a.jpg'
    opt.names = './data/humanface.names'
    result = detect(opt)
    return {"message1": result}
