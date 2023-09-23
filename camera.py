import cv2
import keyboard

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Display the frame in a window
    cv2.imshow("Webcam", frame)

    # Check if the spacebar key is pressed
    if keyboard.is_pressed("space"):
        # Save the current frame as an image
        cv2.imwrite("captured_photo.jpg", frame)
        print("Photo captured!")

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
