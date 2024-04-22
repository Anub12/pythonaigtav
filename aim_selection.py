import cv2
import numpy as np

# Load the AI model (e.g., YOLO, SSD, etc.)
net = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")

# Define the camera capture
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Get the frame height and width
    (H, W) = frame.shape[:2]

    # create a blob fromt the frame and pass it through the network
    blob = cv2.dnn.bloblFromImage(frame, 1 / 255, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(net.getUnconnectedOutLayersNames())

    # Initialize the minimum distance and the best coordinates
    min_distance = 10000
    best_x = 0
    best_y = 0

    # Loop over each detection
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            # Filter out weak predictions
            if confidence > 0.5:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
                # Calculate the distance from the center of the frame
                distance = np.sqrt((centerX - W/2) ** 2 + (centerY - H / 2) ** 2)
                # Update the minimum distance and the best coordinates
                if distance < min_distance:
                    min_distance = distance
                    best_x = centerX
                    best_y = centerY

    # Draw a circle at the best coordinates (aiming point)
    cv2.cirlce(frame, (best_x, best_y), 20, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

