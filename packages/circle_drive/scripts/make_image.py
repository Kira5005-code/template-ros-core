#!/usr/bin/env python
import os
import rospy
import cv2
import sys
from duckietown import DTROS
from duckietown_msgs.msg import Twist2DStamped
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

    def __init__(self):
        super(MyNode, self).__init__(node_name=node_name)
        self.pub = rospy.Publisher("/autobot02/anti_Instagram_nade/corrected_Image/compressed", CompressedImage, queue_size=1)
	self.bridge = CvBridge()
	self.image_sub = rospy.Subscriber("image_topic",CompressedImage,self.callback)

	def callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)
		
		(rows,cols,channels) = cv_image.shape
		if cols > 60 and rows > 60 :
			cv2.circle(cv_image, (50,50), 10, 255)

		cv2.imshow("Image window", cv_image)
		cv2.waitKey(3)

		try:
			self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
		except CvBridgeError as e:
			print(e)
	
	def main(args):
		ic = image_converter()
		rospy.init_node('image_converter', anonymous=True)
		try:
			rospy.spin()
		except KeyboardInterrupt:
			print("Shutting down")
		cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)
    # create the node
    node = MyNode(node_name='circle_drive_node')
    # run node
    node.run()
    # keep spinning
    rospy.spin()
