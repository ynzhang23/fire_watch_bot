# Forest 'Fire' Gump
A bot that analyzes photos from a camera to detect forest fires using GoogLeNet.
## Project Description: 
Forest Fires are a major issue affecting climate change by contributing massive amounts of CO2 emissions to the atmosphere. This bot was created in the hopes that it could eventually be run on a vast system of cameras deployed in forests prone to forest fires. The vision is that all these cameras would have a live feed of the forest and will intermittently send an image to the bot to detect if there is a fire. 
### Purpose
The code could be implemented onto a camera attached to a rotational servo. The camera will take periodic photos which will be analyzed by the bot to be presented on a interface used by Fire Watchers.

<img src="https://github.com/ynzhang23/forest-fire-gump/assets/106020817/d57f8a58-8ed2-4539-b35d-68ee52ef47de" width="400">

We have created a conceptual interface that could represent all the cameras deployed and when one detects a fire, the node corresponding to the camera on the UI will turn red.  
### Concept UI
<img src="https://github.com/ynzhang23/forest-fire-gump/assets/106020817/c6ddc430-c677-4278-9002-e1b045816c7c" width="400">

## Usage Guide
### Installation
These are the necessary dependencies to test the code
```
python -m pip install matlabengine==23.2.1
pip install opencv-python
pip install keyboard
pip install matlab
```
### Usage
To activate the camera (in this case we will use the web cam for test):
```
sudo python3 camera.py
```
Take a photo: Press **space bar**, the photo will be saved into the `./photo`
To check for fire in the latest photo:
```
python3 run_mat.py
```
The output on the terminal will reflect the prediction of the model.
```
FIRE FIRE FIRE
or
WE ARE SAFE
```
### 
# Process: 
## Model Training using MATLAB
### Dataset
[Dataset](https://www.kaggle.com/datasets/phylake1337/fire-dataset)

The first part of creating the model was acquiring data on forest fires and forests without fires. We found a labeled data set online that fit our needs but we needed to clean it to make sure all images were relevant (some of them depicted buildings on fire). We also needed to write a function to modify all of the images into the same dimensions for our model (224,224,3). Then we split up our data set into three categories: training, validation, and testing. We used a 70%:15%:15% ratio for this. 

### Model Training
Creating the neural network: We used Matlab to create our model based on an already available neural network on MatLab called GoogLeNet. We needed to modify the layers of the model so that it could be trained and deployed with our specific data set. 

Training the neural network: We trained the model using the training and validation data. We came up with optimal parameters to train the model such as the minibatch size, initial learning rate, validation frequency, and many more. 

<img width="600" alt="trianing image" src="https://github.com/ynzhang23/fire_watch_bot/assets/144401108/973e1140-8846-4574-aeaa-3dabc3e5f5bb">

### Testing the neural network
Then we tested the model using the test data that we partitioned off before. We created a confusion matrix that plotted our results. The accuracy was 96.64%. This is the confusion matrix: 

<img width="600" alt="confusion matrix" src="https://github.com/ynzhang23/fire_watch_bot/assets/144401108/c9a5da70-f11a-4b14-b419-60ef35fcc5e1">

#### Credits
forest_map = https://www.patreon.com/posts/forest-trek-36109284
