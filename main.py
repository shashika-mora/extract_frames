import cv2

video = cv2.VideoCapture("test.mp4")
# Replace with your video or with a file path

count, success = 0, True
while success:
    success, frame = video.read() # Read Frame
    if success:
        cv2.imwrite(f"frame_{count}.jpg", frame) # Save Frame
        count += 1
    else:
        break

video.release() # Release Video
print(f"Extracted {count} frames.")
cv2.destroyAllWindows()