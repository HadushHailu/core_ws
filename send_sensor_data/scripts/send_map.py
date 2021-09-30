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
sys.path.insert(0, os.path.abspath("../comm/msg_ntk"))
LOGGER.info("current path: %s", os.path.abspath("../comm/msg_ntk"))

from msg_ntk import Map2DDataPUB



def map_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)

    # msg_ntk
    
def send_map():

    rospy.init_node('send_map', anonymous=True)

    rospy.Subscriber("map", OccupancyGrid, map_callback)

    # thread
    rospy.spin()

if __name__ == '__main__':
    send_map()
