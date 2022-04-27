#!/usr/bin/env python 

from email.mime import image
import rospy
import cv2 as cv
import numpy as np
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge, CvBridgeError


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
            # gray= cv.cvtColor(cv2_img, cv.COLOR_BGR2GRAY)
            ret, thresh=cv.threshold(cv2_img, 0, 128, cv.THRESH_TOZERO)
            gblur=cv.GaussianBlur(thresh,(3,3),0)
            erosi=cv.erode(thresh,kernel,iterations=1)
            canny=cv.Canny(erosi,100,200)
            # sobelxy=cv.Sobel(canny, cv.CV_64F, 1, 1, 5)


            
        except CvBridgeError as e:
            print(e)
        cv.imshow('Gaussian Blur',gblur)
        cv.imshow('Thresholding',thresh)
        cv.imshow('Canny',canny)
            
        if cv.waitKey(1) & 0xFF == ord('q'):
            self.img_sub.unregister()
            rospy.signal_shutdown("")

            self.counter +=1
            self.now= rospy.get_rostime().secs
            if (self.now-self.start)/60>0.5:
                rospy.signal_shutdown("")
    
    def end(self):
        print ("This node would be dead, Good bye")
        cv2.destroyAllWindows() 

if __name__=='__main__':
   try: 
       listener=listener()
       rospy.spin()
   except rospy.ROSInterruptException :
        pass
