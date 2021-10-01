#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
#https://docs.opencv.org/4.5.3/dd/d49/tutorial_py_contour_features.html
#https://learnopencv.com/edge-detection-using-opencv/#how-are-edges-detected

#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #https://learnopencv.com/edge-detection-using-opencv/#how-are-edges-detected
    img_blur = cv2.GaussianBlur(gray, (3,3), 0)
    
    # Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

    # Display Sobel Edge Detection Images
    cv2.imshow('Sobel X', sobelx)

    cv2.waitKey(0)
    cv2.imshow('Sobel Y', sobely)
    cv2.waitKey(0)
    cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
    cv2.waitKey(0)

    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection

    # Display Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', edges)

    #end of https://learnopencv.com/edge-detection-using-opencv/#how-are-edges-detected
    
    cv2.waitKey(0)
    
    #https://docs.opencv.org/4.5.3/dd/d49/tutorial_py_contour_features.html
    ret,thresh = cv2.threshold(edges,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[1]
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.imshow('contours',  cv2.drawContours(frame,[box],0,(0,0,255),2))
    
    #end of https://docs.opencv.org/4.5.3/dd/d49/tutorial_py_contour_features.html
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # Display the resulting frame   
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#end of https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html