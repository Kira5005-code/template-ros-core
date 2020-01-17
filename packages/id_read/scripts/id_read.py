#! /usr/bin/env python
import rospy

from duckietown_msgs.msg import AprilTagsWithInfos, TagInfo, AprilTagDetection
from apriltags2_ros.msg import AprilTagDetectionArray
from std_msgs.msg import String

pub = rospy.Publisher("/topic_readed_id", AprilTagsWithInfos, queue_size = 10)

def handle_msg(msg):
	for i in range(10):
		print("ID DETECTED!!!!!!")
    	#pub.publish(msg)
	for i in msg.detections:
		#pub.publish(i.id) 
		for j in range(5):
			print("ID DETECTED :: :: " + str(i.id))
if __name__ == '__main__':
  rospy.init_node('id_reader')
  sub = rospy.Subscriber('/autobot02/apriltags_postprocessing_node/apriltags_out', AprilTagsWithInfos,handle_msg,queue_size=10)
  print("Hello wordl")
  rospy.spin()
