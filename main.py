import cv2

video = cv2.VideoCapture("video.mp4")

count, success = 0, True
while success:
    success, frame = video.read() # Read Frame
    if success:
        cv2.imwrite(f"frame_{count}.jpg", frame)
        count += 1
    
video.release()
cv2.destroyAllWindows()