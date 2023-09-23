# Forest 'Fire' Gump
A bot that analyzes photos from a camera to detect forest fires.
## Project Description: 
Forest Fires are a major issue affecting climate change by contributing massive amounts of CO2 emissions to the atmosphere. This bot was created in the hopes that it could eventually be run on a vast system of cameras deployed in forests prone to forest fires. The vision is that all these cameras would have a live feed of the forest and will intermittently send an image to the bot to detect if there is a fire. We have created a hypothetical interface that could be created to represent all the cameras deployed and when one detects a fire, the node corresponding to the camera on the nap will switch to red.  

### Concept UI
![Untitled (1)](https://github.com/ynzhang23/forest-fire-gump/assets/144401108/3e050e00-5650-40bd-b159-dbb8509942c6)

## Installations to run our code
pip install opencv-python

pip install keyboard

pip install matlab

$ python -m pip install matlabengine==23.2.1

# Process: 

Data: The first part of creating the model was acquiring data on forest fires and forests without fires. We found a labeled data set online that fit our needs but we needed to clean it to make sure all images were relevant (some of them depicted buildings on fire). We also needed to write a function to modify all of the images into the same dimensions for our model (224,224,3). Then we split up our data set into three categories: training, validation, and testing. We used a 70%:15%:15% ratio for this. 

Creating the neural network: We used Matlab to create our model based on an already available neural network on MatLab called GoogLeNet. We needed to modify the layers of the model so that it could be trained and deployed with our specific data set. 

Training the neural network: We trained the model using the training and validation data. We came up with optimal parameters to train the model such as the minibatch size, initial learning rate, validation frequency, and many more. This is an image of the model being trained: <img width="1193" alt="trianing image" src="https://github.com/ynzhang23/fire_watch_bot/assets/144401108/973e1140-8846-4574-aeaa-3dabc3e5f5bb">


Testing the neural network: Then we tested the model using the test data that we partitioned off before. We created a confusion matrix that plotted our results. The accuracy was 96.64%. This is the confusion matrix: <img width="823" alt="confusion matrix" src="https://github.com/ynzhang23/fire_watch_bot/assets/144401108/c9a5da70-f11a-4b14-b419-60ef35fcc5e1">
