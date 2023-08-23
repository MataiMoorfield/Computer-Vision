from ultralytics import YOLO
import cv2
import math 
import tkinter as tk
from PIL import Image, ImageTk

# Create a GUI window
root = tk.Tk()
root.title("Object Detection")

# Create a label to display the webcam feed
label = tk.Label(root)
label.pack()

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("yolo-Weights/yolov8n.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

def update_frame():
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100

            # class name
            cls = int(box.cls[0])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 0.5
            text = classNames[cls]
            color = (255, 242, 0) # Bright bold red color (BGR format)
            bg_color = (255, 0, 255)  # Purple color for background
            thickness = 2        # Increased thickness for boldness

            # Get text size to create a background rectangle
            text_size = cv2.getTextSize(text, font, fontScale, thickness)[0]
            text_width = text_size[0]
            text_height = text_size[1]

            # Calculate the coordinates for the background rectangle
            bg_x1 = x1
            bg_y1 = y1 - text_height - 5
            bg_x2 = x1 + text_width + 10
            bg_y2 = y1 - 3

            # Draw background rectangle and text
            cv2.rectangle(img, (bg_x1, bg_y1), (bg_x2, bg_y2), bg_color, -1)  # Filled rectangle
            cv2.putText(img, text, (x1 + 5, y1 - 5), font, fontScale, color, thickness)

    # Convert the OpenCV image to a format compatible with Tkinter
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img_tk = ImageTk.PhotoImage(image=img)

    # Update the label with the new frame
    label.img = img_tk
    label.config(image=img_tk)
    label.after(1, update_frame)  # Reduced delay for higher frame rate

# Start updating the frame
update_frame()

# Run the GUI event loop
root.mainloop()

cap.release()
cv2.destroyAllWindows()
