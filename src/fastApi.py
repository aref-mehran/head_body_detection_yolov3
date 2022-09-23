from detect import detect
from fastapi import FastAPI, File, UploadFile

import torch

# Import relevant modules
import numpy as np
import cv2

def extractPolygon(polygon,img):
    # Define points
    pts = np.array([[542, 107], [562, 102], [582, 110], [598, 142], [600, 192], [601, 225], [592, 261], [572, 263], [551, 245], [526, 220], [520, 188], [518, 152], [525, 127], [524, 107]], dtype=np.int32)

    ### Define image here
    img = 255*np.ones((300, 700, 3), dtype=np.uint8)

    # Initialize mask
    mask = np.zeros((img.shape[0], img.shape[1]))

    # Create mask that defines the polygon of points
    cv2.fillConvexPoly(mask, pts, 1)
    mask = mask.astype(np.bool)

    # Create output image (untranslated)
    out = np.zeros_like(img)
    out[mask] = img[mask]

    # Find centroid of polygon
    (meanx, meany) = pts.mean(axis=0)

    # Find centre of image
    (cenx, ceny) = (img.shape[1]/2, img.shape[0]/2)

    # Make integer coordinates for each of the above
    (meanx, meany, cenx, ceny) = np.floor([meanx, meany, cenx, ceny]).astype(np.int32)

    # Calculate final offset to translate source pixels to centre of image
    (offsetx, offsety) = (-meanx + cenx, -meany + ceny)

    # Define remapping coordinates
    (mx, my) = np.meshgrid(np.arange(img.shape[1]), np.arange(img.shape[0]))
    ox = (mx - offsetx).astype(np.float32)
    oy = (my - offsety).astype(np.float32)

    # Translate the image to centre
    out_translate = cv2.remap(out, ox, oy, cv2.INTER_LINEAR)

    # Determine top left and bottom right of translated image
    topleft = pts.min(axis=0) + [offsetx, offsety]
    bottomright = pts.max(axis=0) + [offsetx, offsety]

    # Draw rectangle
    cv2.rectangle(out_translate, tuple(topleft), tuple(bottomright), color=(255,0,0))

    # Show image, wait for user input, then save the image
    cv2.imwrite('output.png', out_translate);
    return out_translate;


app = FastAPI()

def get_person_count(imageBuffer):
    try:
        tempFileName = './temp.jpg'
        with open(tempFileName, 'wb') as f:
            f.write(imageBuffer)
        with torch.no_grad():
            result = detect(tempFileName)
            return {"message1": result}
    except Exception :
        return {"message":"there was an error in person detection"};

@app.post("/")
async def upload(file: UploadFile = File(...),polygons=[]):
    try:
        if len(polygons)==0 :
            imageBuffer = await file.read();
            message=get_person_count(imageBuffer);
            return message;
        else:
            messages=[];
            for polygon in polygons:
                img=extractPolygon(polygon,imageBuffer);
                message=get_person_count(img);
                messages.append(message);
            return messages;
        



    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()
