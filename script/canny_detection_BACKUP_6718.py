#!/usr/bin/env python 

from sensor_msgs.msg import Image 
from cv_bridge import CvBridge, CvBridgeError
from imutils import paths
import rospy
import cv2 as cv
import numpy as np
import imutils



class listener:
    def __init__(self) :
        rospy.init_node("canny_detection", anonymous=True)
        self.bridge=CvBridge()
        self.img_sub=rospy.Subscriber("/webcam",  Image, self.image_callback)
        rospy.spin()

    def image_callback (self,msg):
        try:
            kernel= np.ones((5,5),np.uint8)
            cv2_img=self.bridge.imgmsg_to_cv2(msg,'bgr8')
<<<<<<< HEAD
            new_image = cv.convertScaleAbs(cv2_img, alpha=1, beta=10)
            gray= cv.cvtColor(new_image, cv.COLOR_BGR2GRAY)
            # ret, thresh=cv.threshold(gray, 0, 127, cv.THRESH_TOZERO)
            gblur=cv.GaussianBlur(gray,(3,3),0)
            erosi=cv.erode(gblur,kernel,iterations=1)
            canny=cv.Canny(erosi,100,200)
            # sobelxy=cv.Sobel(canny, cv.CV_64F, 1, 1, 5)
            cnts= cv.findContours(canny.copy(),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
            cnts= imutils.grab_contours(cnts)
            # c= max(cnts,key=cv.contourArea)
            
            # return cv.minAreaRect(c)
            
=======
            # gray= cv.cvtColor(cv2_img, cv.COLOR_BGR2GRAY)
            
            ret, thresh=cv.threshold(cv2_img, 0, 128, cv.THRESH_TOZERO)
            gblur=cv.GaussianBlur(thresh,(3,3),0)
            erosi=cv.erode(thresh,kernel,iterations=1)
            canny=cv.Canny(erosi,100,200)
            # sobelxy=cv.Sobel(canny, cv.CV_64F, 1, 1, 5)
            _,contours, hierarchy= cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
		
            for cnt in contours:
                rect = cv.minAreaRect(cnt)
                box = cv.boxPoints(rect)
                box = np.int0(box)
                if(rect[1][0]<110 and rect[1][0]>40 and rect[1][1]<70 and rect[1][1]>40):

                    cv.drawContours(cv2_img, [box], -1, (0,255,0),2)
                    cv.imshow('Contours', cv2_img)
>>>>>>> 57bb0923376b6c1f54a0335847b623ee04a1dc5a
        except CvBridgeError as e:
            print(e)
        cv.imshow('Gaussian Blur',gblur)
        # cv.imshow('Thresholding',thresh)
        cv.imshow('Canny',cnts)
        
            
        if cv.waitKey(1) & 0xFF == ord('q'):
            self.img_sub.unregister()
            rospy.signal_shutdown("")
            rospy.loginfo("Node akses terhenti, Good bye")

            self.counter +=1
            self.now= rospy.get_rostime().secs
            
            if (self.now-self.start)/60>0.5:
                rospy.signal_shutdown("")
<<<<<<< HEAD
    
    def end(self): 
        cv.destroyAllWindows() 

=======

    def end(self):
        cv2.destroyAllWindows() 
        rospy.loginfo ("This node would be dead, Good bye")
>>>>>>> 57bb0923376b6c1f54a0335847b623ee04a1dc5a
if __name__=='__main__':
   try: 
       listener=listener()
       rospy.spin()
   except rospy.ROSInterruptException :
        pass
        
