import numpy as np
import cv2 as cv

#Atribui ao objeto uma url para leitura de video, conectado com o Ipv4 da rede (IP Webcam)
img = cv.VideoCapture('https://xxx.xxx.x.xxx:8080/video') 

while True:
    #Processamento da imagem para obter apenas os pontos de interesse, utilizando binarização
    _,frame = img.read() #Faz a leitura da imagem recebida pela url
    resized = cv.resize(frame,(600,400))
    imgGray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(imgGray,19)
    _,bin = cv.threshold(blur,135,255,cv.THRESH_BINARY)

    #Detecção dos pontos de interesse do dado, utilizando Blob para determinar a pontuação do dado
    detectObj = cv.SimpleBlobDetector_create()
    keyPoints = detectObj.detect(bin)
    blob = cv.drawKeypoints(resized,keyPoints,np.array([]),(0,0,255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.putText(blob,("Points : ")+str(len(keyPoints)),(15,60),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1,cv.LINE_AA)

    #Definir os contornos do dado para realizar a contagem do numero total de dados na câmera
    conts,_ = cv.findContours(bin,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(blob,conts,-1,(0,255,255),2)
    cv.putText(blob,("Dice : ")+str(len(conts)),(15,30),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,255),1,cv.LINE_AA)
    
    key = cv.waitKey(1)
    if key == ord("e"): 
        break
    cv.imshow("Source",bin)
    cv.imshow("Processed", blob)