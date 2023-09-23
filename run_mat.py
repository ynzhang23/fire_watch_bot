import matlab.engine

def run_mat(image_path):
    # Start MATLAB engine
    eng = matlab.engine.start_matlab()

    # Run MATLAB function in another folder
    eng.cd(r'fire_detection_model', nargout=0)

    # Call the MATLAB function with the image as input
    prediction = eng.predictFire(image_path)

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