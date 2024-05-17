import rclpy
from robotont_msgs.msg import LedModuleMode
import random
import os

node = None
pub_mode = None
mode = 1

def change_mode():
    global mode, pub_mode, node
    led_msg_mode = LedModuleMode()
    led_msg_mode.mode = mode
    if mode == 1 or mode == 2:
        led_msg_mode.params.append(random.randint(0, 255))
        led_msg_mode.params.append(random.randint(0, 255))
        led_msg_mode.params.append(random.randint(0, 255))
        led_msg_mode.params.append(random.randint(1, 50))
    if mode == 3 or mode == 4 or mode == 6:
        led_msg_mode.params.append(random.randint(1, 50))
    
    pub_mode.publish(led_msg_mode)
    node.get_logger().info('Publishing: "%s"' % led_msg_mode)
    mode += 1
    if mode >= 9:
        mode = 1

def main(args=None):
    global pub_mode, node
    rclpy.init(args=args)
    node = rclpy.create_node('demo_lighting')
    pub_mode = node.create_publisher(LedModuleMode, 'led_mode', 10)
    node.create_timer(3, change_mode)
    try:
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
