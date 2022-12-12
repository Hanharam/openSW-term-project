import cv2

capture=cv2.VideoCapture(0)
if not cap.isOpened():
    print("camera open failed")
    exit()
while True:
    ret, img=capture.read()
    if not ret:
        print("Can't read camera")
        break

    cv.imshow('PC_camera',img)
    if num==0: #마스크 안쓴 사람일 경우
        img_captured=cv2.imwrite("img_captured_png",img)
    
