import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import qos_profile_sensor_data

class ObstacleAvoidanceNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            qos_profile=qos_profile_sensor_data
        )
        self.get_logger().info('Engel Algilama Nodu Baslatildi!')

    def scan_callback(self, msg):
        # 0. indeks robotun tam onudur
        scan_range = msg.ranges[0]
        twist = Twist()

        if scan_range > 0.5:
            # Engel yok, daire ciz
            twist.linear.x = 0.2
            twist.angular.z = 0.5
        else:
            # Engel var, DUR
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.get_logger().warning(f'ENGEL! Mesafe: {scan_range:.2f}m. Duruluyor...')

        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidanceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
