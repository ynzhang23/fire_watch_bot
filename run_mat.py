"""
Run matlab model on the latest photo taken
"""

import matlab.engine
import os
import glob

def run_mat(image_path):
    # Start MATLAB engine
    eng = matlab.engine.start_matlab()
    # Run MATLAB function in another folder
    eng.cd(r'fire_detection_model', nargout=0)

    # Call the MATLAB function with the image as input
    prediction = eng.predictFire("." + image_path)

    # Close the MATLAB engine
    eng.quit()

    return prediction

def process_matlab_result(prediction):
    if prediction == 'non_fire_images':
        return 'WE ARE SAFE'
    elif prediction == 'fire_images':
        return 'FIRE FIRE FIRE'
    else:
        return 'ERROR'

# Define the directory where your images are stored
image_directory = "./photos"

# Use glob to list image files in the directory
image_files = glob.glob(os.path.join(image_directory, "*.jpg"))  # You can specify other image extensions too

# Sort the list of image files by modification time (latest first)
image_files.sort(key=os.path.getmtime, reverse=True)

# Get the path of the latest image (if there are any images)
if image_files:
    latest_image_path = image_files[0]
else:
    print("No images found in the directory.")

prediction = run_mat(latest_image_path)
print(process_matlab_result(prediction))