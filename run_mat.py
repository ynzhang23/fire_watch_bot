import matlab.engine

image_path = '../photos/2023-09-23_12-28-31.jpg'

# Start MATLAB engine
eng = matlab.engine.start_matlab()

# Run MATLAB function in another folder
eng.cd(r'fire_detection_model', nargout=0)

# Call the MATLAB function with the image as input
prediction = eng.predictFire(image_path)

# Print the prediction from MATLAB
if prediction == 'non_fire_images':
  print('WE ARE SAFE')
elif prediction == 'fire_images':
  print('FIRE FIRE FIRE')
else:
  print("ERROR")

# Close the MATLAB engine
eng.quit()