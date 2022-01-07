#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('st')                                # ノード名「count」に設定
pub = rospy.Publisher('st', Int32, queue_size=1)  # パブリッシャ「count_up」を作成
rate = rospy.Rate(10)                                   # 10Hzで実行
st = "これはサァンのばいすうぅーーー"
while not rospy.is_shutdown():
        pub.publish(st)
        rate.sleep()
