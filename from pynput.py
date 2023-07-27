# Import required libraries
import cv2  # OpenCV for computer vision tasks
from cvzone.HandTrackingModule import HandDetector  # Custom hand tracking module
from pynput.keyboard import Key, Controller  # For controlling the keyboard

# Set up video capture from the default camera (index 0)
cap = cv2.VideoCapture(0)

# Set the width and height of the capture window (optional)
    
# Create a hand detector object with a confidence threshold of 0.7 and allow detecting a maximum of 1 hand
detector = HandDetector(detectionCon=0.7, maxHands=1)
# Create a keyboard controller object to simulate keyboard inputs
keyboard = Controller()

# Start an infinite loop to continuously process video frames from the camera
while True:
    # Read a frame from the video capture
    _, img = cap.read()
    img = cv2.flip(img, 1)

    # Detect hands in the current frame and get the modified image with annotations
    hands, img = detector.findHands(img)

    # Check if hands are detected in the frame
    if hands:   
        # Get the status of fingers (how many are raised) for the first detected hand
        fingers = detector.fingersUp(hands[0])

        # Check if all fingers are closed (all 0s in the fingers list)
        if sum(fingers) == 0:
            # If all fingers are closed, press the left arrow key and release the right arrow key
            keyboard.press(Key.up)
            keyboard.release(Key.left)
            keyboard.release(Key.right)
            print('Go')
        # Check if all fingers are open (all 1s in the fingers list)
        elif sum(fingers) == 5:
            # If all fingers are open, press the right arrow key and release the left arrow key
            keyboard.press(Key.down)
            keyboard.release(Key.up)
            print('stop')
        elif sum(fingers) == 1:
            # If all fingers are open, press the right arrow key and release the left arrow key
            keyboard.press(Key.right)
            keyboard.release(Key.left)
            print('Right')
        elif sum(fingers) == 2:
            #If all fingers are open, press the right arrow key and release the left arrow key
            keyboard.press(Key.left)
            keyboard.release(Key.right)
            print('Left')
        '''elif sum(fingers) == 3:
            # If all fingers are open, press the right arrow key and release the left arrow key
            keyboard.press(Key.down)
            keyboard.release(Key.up)
            print('Duck')
        elif sum(fingers) == 4:
            # If all fingers are open, press the right arrow key and release the left arrow key
            keyboard.press(Key.space)
            keyboard.release(Key.down)
            print('Jump')'''
    else:
        # If no hands are detected, release both arrow keys (to stop movement)
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        keyboard.release(Key.up)
        keyboard.release(Key.down)

    # Display the modified image with hand annotations
    cv2.imshow("Cam", img)

    # Check if the user pressed the 'q' key to quit the program
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video capture and close the display window