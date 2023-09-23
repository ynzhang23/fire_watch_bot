import matlab.engine

# Start MATLAB engine
eng = matlab.engine.start_matlab()

# Run MATLAB function in another folder
eng.cd(r'matlab/2-PretrainedModels', nargout=0)

# Call the MATLAB function with the image as input
prediction = eng.predict_image()

# Print the prediction from MATLAB
print(prediction)

# Close the MATLAB engine
eng.quit()