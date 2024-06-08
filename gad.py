{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86ff5e1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import math\n",
    "import argparse\n",
    "\n",
    "def highlightFace(net, frame, conf_threshold=0.7):\n",
    "    frameOpencvDnn=frame.copy()\n",
    "    frameHeight=frameOpencvDnn.shape[0]\n",
    "    frameWidth=frameOpencvDnn.shape[1]\n",
    "    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)\n",
    "\n",
    "    net.setInput(blob)\n",
    "    detections=net.forward()\n",
    "    faceBoxes=[]\n",
    "    for i in range(detections.shape[2]):\n",
    "        confidence=detections[0,0,i,2]\n",
    "        if confidence>conf_threshold:\n",
    "            x1=int(detections[0,0,i,3]*frameWidth)\n",
    "            y1=int(detections[0,0,i,4]*frameHeight)\n",
    "            x2=int(detections[0,0,i,5]*frameWidth)\n",
    "            y2=int(detections[0,0,i,6]*frameHeight)\n",
    "            faceBoxes.append([x1,y1,x2,y2])\n",
    "            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)\n",
    "    return frameOpencvDnn,faceBoxes\n",
    "\n",
    "\n",
    "parser=argparse.ArgumentParser()\n",
    "parser.add_argument('--image')\n",
    "\n",
    "args=parser.parse_args()\n",
    "\n",
    "faceProto=\"opencv_face_detector.pbtxt\"\n",
    "faceModel=\"opencv_face_detector_uint8.pb\"\n",
    "ageProto=\"age_deploy.prototxt\"\n",
    "ageModel=\"age_net.caffemodel\"\n",
    "genderProto=\"gender_deploy.prototxt\"\n",
    "genderModel=\"gender_net.caffemodel\"\n",
    "\n",
    "MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)\n",
    "ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']\n",
    "genderList=['Male','Female']\n",
    "\n",
    "faceNet=cv2.dnn.readNet(faceModel,faceProto)\n",
    "ageNet=cv2.dnn.readNet(ageModel,ageProto)\n",
    "genderNet=cv2.dnn.readNet(genderModel,genderProto)\n",
    "\n",
    "video=cv2.VideoCapture(args.image if args.image else 0)\n",
    "padding=20\n",
    "while cv2.waitKey(1)<0:\n",
    "    hasFrame,frame=video.read()\n",
    "    if not hasFrame:\n",
    "        cv2.waitKey()\n",
    "        break\n",
    "\n",
    "    resultImg,faceBoxes=highlightFace(faceNet,frame)\n",
    "    if not faceBoxes:\n",
    "        print(\"No face detected\")\n",
    "\n",
    "    for faceBox in faceBoxes:\n",
    "        face=frame[max(0,faceBox[1]-padding):\n",
    "                   min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding)\n",
    "                   :min(faceBox[2]+padding, frame.shape[1]-1)]\n",
    "\n",
    "        blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)\n",
    "        genderNet.setInput(blob)\n",
    "        genderPreds=genderNet.forward()\n",
    "        gender=genderList[genderPreds[0].argmax()]\n",
    "        print(f'Gender: {gender}')\n",
    "\n",
    "        ageNet.setInput(blob)\n",
    "        agePreds=ageNet.forward()\n",
    "        age=ageList[agePreds[0].argmax()]\n",
    "        print(f'Age: {age[1:-1]} years')\n",
    "\n",
    "        cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)\n",
    "        cv2.imwrite(\"output.jpg\", resultImg)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
