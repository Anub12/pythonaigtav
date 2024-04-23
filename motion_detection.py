import cv2

# Capture video from default camera
cap = cv2.VideoCapture(0)

# Read three images first:
_, frame1 = cap.read()
_, frame2 = cap.read()
_, frame3 = cap.read()

while True:
    # Detect difference between frames
    diff = cv2.absdiff(frame1, frame3)

    # Convert to gray and blur
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold and dilate
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours and draw rectangle
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 1000:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display output
    cv2.imshow('feed', frame1)

    # Read next frame
    frame1 = frame2
    frame2 = frame2
    _, frame3 = cap.read()

    # Exit on key press
    if cv2.waitKey(10) == 27:
        break

# Release resources
cv2.destroyAllWindows()
cap.release()

# take a screenshot from gta 5

# write code for motion detection in this file
# For pushing file
