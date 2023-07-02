from itertools import count

import cv2
import PIL
import time
from datetime import date

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
local_time = time.localtime()
final_time = time.strftime("%H:%M:%S", local_time)
while True:
    try:
        check, frame = webcam.read()
        print(check)  # prints true as long as the webcam is running
        print(frame)  # prints matrix values of each framecd
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('t'):
            # cv2.imwrite(filename='saved_img.jpg', img=frame)
            cv2.imwrite(
                filename='C:/Users/SAIDHEERAJ/Downloads/beautnology-projects-main/beautnology-projects-main/tops/shirt_' + str(
                    date.today()) + '_' + final_time + '.jpg',
                img=frame)
            webcam.release()
            # img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            # img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Image saved!")
            # print("Converting RGB image to grayscale...")
            # gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            # print("Converted RGB image to grayscale...")
            # print("Resizing image to 28x28 scale...")
            # img_ = cv2.resize(gray, (28, 28))
            # print("Resized...")

            # img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            # img_resized.save(r'C:\Users\SAIDHEERAJ\Downloads\beautnology-projects-main\beautnology-projects-main\test.png')
            print("Image saved!")

        elif key == ord('b'):

            # cv2.imwrite(filename='saved_img.jpg', img=frame)

            cv2.imwrite(filename='C:/Users/SAIDHEERAJ/Downloads/beautnology-projects-main/beautnology-projects-main/bottoms/{:03d}.png'.format(count),img=frame)
            webcam.release()
            # img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            # img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Image saved!")

            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
