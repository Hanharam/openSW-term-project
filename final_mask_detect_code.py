import cv2
import time
import tensorflow
import numpy as np

model_filename="./converted_keras/keras_model.h5"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

try:
    capture=cv2.VideoCapture(0) #카메라 열기
    capture.set(cv2.CAP_PROP_FRAME_WIDTH,640) #이미지 가로 픽셀
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #이미지 세로 픽셀 
    model=tensorflow.keras.models.load_model(model_filename) #텐서플로 이미지 분류기 가져오기
except Exception as e:
    print(e)
def preprocessing(frame):
    size=(224,224)
    frame_resize=cv2.resize(frame,size,interpolation=cv2.INTER_AREA)
    frame_normalized=(frame_resize.astype(np.float32)/127.0)-1  #이미지 정규화 
    frame_reshaped=frame_normalized.reshape((1,224,224,3))  # 전처리 
    return frame_reshaped
def predict(frame):
    prediction=model.predict(frame) # 확률 반환 
    return prediction

while True:
    ret,frame=capture.read()
    frame=cv2.flip(frame,1)
    if cv2.waitKey(10)>0:
        cv2.destroyAllWindows()
        break
    try:    
        preprocessed=preprocessing(frame) #이미지 전처리
        prediction=predict(preprocessed) #텐서플로 모델로  분류기 적용 
    except Exception as e:
        print(e)
    #print(prediction)
    num=0
    for i in prediction[0]:
         if(i>0.9):
              print(num)
              cv.imshow('PC_camera',img)
              if(num==0): #0 일 경우 노마스크
                   img_captured=cv2.imwrite("img_captured_png",img)
                   while(cap.isOpened()):
                        if ret:
                            gray = cv2. cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            faces = face_cascade.detectMultiScale(gray, 1.05, 4, minSize=(200, 200))

                            for (x, y, w, h) in faces:
                                cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

                            cv2.imshow('Video', frame)

                            print('number of people =', enumerate(faces))
        
                            if cv2.waitkey(25) & 0xFF == ord('q'):
                                break
                   print('no mask')
              if(num==1): # 1일 경우 마스크
                   print('mask')
         num=num+1
    cv2.imshow('test',frame) #이미지 창에서 영상 표현



