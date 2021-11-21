# Facial-Expression-Recognition-App
## Describtion 
In this project, I have built and trained a convolutional neural network in Keras to recognize facial expressions. The data consists of 48x48 pixel grayscale images of faces. The objective is to classify each face based on the emotion shown in the facial expression.I used haarcascade to automatically detect faces in images and draw bounding boxes around them.After training and saving model with its trained weights i have developed a web service using flask and applied my model to a real time video and detected the face with its emosion  

The project can be braodly divided into two parts -

1. Build and train a model in Keras for Facial Expression Recognition.
2. Deploy the model on web using FLASK and run it on videos.

## Table of contents :
1. Importing libraries and Reading Data 
2. Showing some examples of images as exploration
3. Building convnet from scratch
4. Training and evaluationg model
5. Saving model and weights
6. Building model class with the pretrained model and weights 
7. Building camera class 
8. Building Flask app in main.py 

## How to Install and Run the Project :
1. Clone the repo in your machine
2. Create new environment and install the necessary libraries 
3. Open the entire folder in visual studio code
4. In case of trying your own video you only should put the path of your video in camera.py in line 
5. In the terminal run this script --> python main.py
6. Finally go to the link that will be provided in terminal and you will see the output   

