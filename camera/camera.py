import cv2
import keyboard
from datetime import datetime
import os

# Define the directory to save photos
save_directory = "./photos"  # Change this to your desired directory

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Display the frame in a window
    cv2.imshow("Webcam", frame)

    # Check if the spacebar key is pressed
    if keyboard.is_pressed("space"):
        # Generate a timestamp string
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Save the current frame as an image with the timestamp as the filename in the "photo" folder
        filename = os.path.join(save_directory, f"{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Photo captured and saved as {filename}!")

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
