import rclpy
from robotont_msgs.msg import LedModulePixel, LedModuleSegment, LedModuleMode, ColorRGB

node = None
pub_pixel = None
pub_segment = None
pub_mode = None

def check_input():
    global pub_pixel, pub_segment, pub_mode
    key = input("Input: ")
    key = key.split(":")
    try:
        if key[0] == "LD":
            led_msg_pixel = LedModulePixel()
            led_msg_pixel.idx = int(key[1])
            color = ColorRGB()
            color.r = int(key[2])
            color.g = int(key[3])
            color.b = int(key[4])
            led_msg_pixel.color = color
            node.get_logger().info('Publishing: "%s"' % led_msg_pixel)
            pub_pixel.publish(led_msg_pixel)
        elif key[0] == "LS":
            led_msg_seg = LedModuleSegment()
            led_msg_seg.idx_start = int(key[1])
            led_msg_seg.idx_end = int(key[2])
            for i in range(3, len(key), 3):
                if i+2 < len(key):
                    color = ColorRGB()
                    color.r = int(key[i])
                    color.g = int(key[i+1])
                    color.b = int(key[i+2])
                    led_msg_seg.colors.append(color)
            led_msg_seg.colors.append(color)
            node.get_logger().info('Publishing: "%s"' % led_msg_seg)
            pub_segment.publish(led_msg_seg)
        elif key[0] == "LM":
            led_msg_mode = LedModuleMode()
            led_msg_mode.mode = int(key[1])
            for i in range(2, len(key)):
                led_msg_mode.params.append(int(key[i]))
            node.get_logger().info('Publishing: "%s"' % led_msg_mode)
            pub_mode.publish(led_msg_mode)
    except:
        pass

def main(args=None):
    global pub_pixel, pub_segment, pub_mode, node
    rclpy.init(args=args)
    node = rclpy.create_node('demo_lighting_manual')
    pub_pixel = node.create_publisher(LedModulePixel, 'led_pixel', 10)
    pub_segment = node.create_publisher(LedModuleSegment, 'led_segment', 10)
    pub_mode = node.create_publisher(LedModuleMode, 'led_mode', 10)
    node.create_timer(1, check_input)
    try:
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
