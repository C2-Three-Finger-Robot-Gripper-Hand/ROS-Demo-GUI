from PyQt4.QtGui import QStandardItem
from PyQt4 import QtGui
import sys
import main_frame
import rospy
from std_msgs.msg import Int16


class GripperHandGui:
    def __init__(self):
        self.init_gui()
        self.init_ros()
        self.frame.show()
        sys.exit(self.app.exec_())

    def init_gui(self):
        self.app = QtGui.QApplication(sys.argv)
        self.frame = QtGui.QMainWindow()
        self.ui = main_frame.Ui_main_frame()
        self.ui.setupUi(self.frame)

        self.ui.Finger1_motor1_slider.valueChanged.connect(self.finger1_motor1_set)
        self.ui.Finger1_motor2_slider.valueChanged.connect(self.finger1_motor2_set)
        self.ui.Finger1_motor3_slider.valueChanged.connect(self.finger1_motor3_set)
        self.ui.Finger2_motor1_slider.valueChanged.connect(self.finger2_motor1_set)
        self.ui.Finger2_motor2_slider.valueChanged.connect(self.finger2_motor2_set)
        self.ui.Finger2_motor3_slider.valueChanged.connect(self.finger2_motor3_set)
        self.ui.Finger3_motor1_slider.valueChanged.connect(self.finger3_motor1_set)
        self.ui.Finger3_motor2_slider.valueChanged.connect(self.finger3_motor2_set)
        self.ui.Finger3_motor3_slider.valueChanged.connect(self.finger3_motor3_set)

    def init_ros(self):
        rospy.init_node('gripper-gui', anonymous=True)

        rospy.Subscriber("finger1_motor1_value", Int16, self.finger1_motor1_callback)
        rospy.Subscriber("finger1_motor2_value", Int16, self.finger1_motor2_callback)
        rospy.Subscriber("finger1_motor3_value", Int16, self.finger1_motor3_callback)
        rospy.Subscriber("finger2_motor1_value", Int16, self.finger2_motor1_callback)
        rospy.Subscriber("finger2_motor2_value", Int16, self.finger2_motor2_callback)
        rospy.Subscriber("finger2_motor3_value", Int16, self.finger2_motor3_callback)
        rospy.Subscriber("finger3_motor1_value", Int16, self.finger3_motor1_callback)
        rospy.Subscriber("finger3_motor2_value", Int16, self.finger3_motor2_callback)
        rospy.Subscriber("finger3_motor3_value", Int16, self.finger3_motor3_callback)

        self.finger1_motor1_set = rospy.Publisher('finger1_motor1_set', Int16, queue_size=10)
        self.finger1_motor2_set = rospy.Publisher('finger1_motor2_set', Int16, queue_size=10)
        self.finger1_motor3_set = rospy.Publisher('finger1_motor3_set', Int16, queue_size=10)
        self.finger2_motor1_set = rospy.Publisher('finger2_motor1_set', Int16, queue_size=10)
        self.finger2_motor2_set = rospy.Publisher('finger2_motor2_set', Int16, queue_size=10)
        self.finger2_motor3_set = rospy.Publisher('finger2_motor3_set', Int16, queue_size=10)
        self.finger3_motor1_set = rospy.Publisher('finger3_motor1_set', Int16, queue_size=10)
        self.finger3_motor2_set = rospy.Publisher('finger3_motor2_set', Int16, queue_size=10)
        self.finger3_motor3_set = rospy.Publisher('finger3_motor3_set', Int16, queue_size=10)

    #
    # Callback functions
    #
    def finger1_motor1_callback(self, data):
        self.ui.set_finger1_motor1_value(data.data)

    def finger1_motor2_callback(self, data):
        self.ui.set_finger1_motor2_value(data.data)

    def finger1_motor3_callback(self, data):
        self.ui.set_finger1_motor3_value(data.data)

    def finger2_motor1_callback(self, data):
        self.ui.set_finger2_motor1_value(data.data)

    def finger2_motor2_callback(self, data):
        self.ui.set_finger2_motor2_value(data.data)

    def finger2_motor3_callback(self, data):
        self.ui.set_finger2_motor3_value(data.data)

    def finger3_motor1_callback(self, data):
        self.ui.set_finger1_motor1_value(data.data)

    def finger3_motor2_callback(self, data):
        self.ui.set_finger1_motor2_value(data.data)

    def finger3_motor3_callback(self, data):
        self.ui.set_finger1_motor3_value(data.data)

    #
    # set functions
    #
    def finger1_motor1_set(self, value):
        self.finger1_motor1_set.publish(value)

    def finger1_motor2_set(self, value):
        self.finger1_motor2_set.publish(value)

    def finger1_motor3_set(self, value):
        self.finger1_motor3_set.publish(value)

    def finger2_motor1_set(self, value):
        self.finger2_motor1_set.publish(value)

    def finger2_motor2_set(self, value):
        self.finger2_motor2_set.publish(value)

    def finger2_motor3_set(self, value):
        self.finger2_motor3_set.publish(value)

    def finger3_motor1_set(self, value):
        self.finger3_motor1_set.publish(value)

    def finger3_motor2_set(self, value):
        self.finger3_motor2_set.publish(value)

    def finger3_motor3_set(self, value):
        self.finger3_motor3_set.publish(value)


if __name__ == "__main__":
    GripperHandGui()
