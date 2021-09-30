import rospy
import zmq
import sys
import os
import logging
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid

## LOGGING INFO
logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(level=logging.INFO)

## ws_client and msg_ntk path 
sys.path.insert(0, os.path.abspath("../uni_auto_comm/msg_ntk"))
LOGGER.info("current path: %s", os.path.abspath("../uni_auto_comm/msg_ntk"))

from msg_ntk import Map2DDataPUB


##
class SendMap():
    def __init__(self):
        # init
        rospy.init_node('send_map', anonymous=True) 
        rospy.Subscriber("map", OccupancyGrid, self.map_callback)

        # init msg_ntk
        self.map_2d_data_pub = Map2DDataPUB()

    def map_callback(self,msg):
        rospy.loginfo(rospy.get_caller_id() + "Map data recieved")

        # msg_ntk
        self.map_2d_data_pub.pub("%s" % msg)

    def start_it(self):
        # thread
        rospy.spin()

if __name__ == '__main__':
    app = SendMap()
    app.start_it()
