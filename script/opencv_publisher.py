#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2 as cv

video=cv.VideoCapture(2)
print(video.isOpened())
bridge=CvBridge()

video.set(cv.CAP_PROP_FPS,5)
fps=video.get(5)
print("Frame per scond: {}".format(fps))

def talker():
	pub=rospy.Publisher('/webcam',Image, queue_size=1)
	rospy.init_node('opencv_publisher',anonymous=False)

	while not rospy.is_shutdown():
		ret,image=video.read()
		if not ret:
			break
		msg=bridge.cv2_to_imgmsg(image,'bgr8')
		pub.publish(msg)

if __name__=='__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass