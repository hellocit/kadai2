#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import time

rospy.init_node('count')                                # ノード名「count」に設定
pub = rospy.Publisher('count_up', Int32, queue_size=1)  # パブリッシャ「count_up」を作成
rate = rospy.Rate(10)                                   # 10Hzで実行
n = 0

time.sleep(2)

while not rospy.is_shutdown():
        n += 1
        if n % 3 == 0:
            print("これは%d" % n)
            pub.publish(n)
        else:
            pub.publish(n)
        if n == 227:
            print("\nThis is unko\n")
        rate.sleep()
