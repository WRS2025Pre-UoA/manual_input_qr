import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
import numpy as np

class TextPublisher(Node):
    def __init__(self):
        super().__init__('text_publisher')
        self.publisher_ = self.create_publisher(String, 'text_topic', 10)
        self.create_subscription(
            String,
            'manual_input_qr',
            self.listener_callback,
            10)
        self.upper_flg = False  # 大文字フラグ


    def listener_callback(self,msg):
        if msg != None:
            # OpenCV設定
            img = np.zeros((720, 1280, 3))
            text=""   # パブリッシュするテキスト
            while True:
                cv2.putText(img, text, (30, 30), cv2.FONT_HERSHEY_DUPLEX,
                            1.0, (255, 255, 255))
                cv2.imshow("Text Publisher", img)

                key = cv2.waitKey(10)
                if key == 13:  # Enterキーが押された場合
                    print("pressed Enter Key")
                    self.publish_text(text)
                    cv2.destroyAllWindows()  # ウィンドウを閉じる
                    break
                if key == 225:
                    self.upper_flg = not self.upper_flg  # 大文字フラグを反転
                    continue
                if key != -1:
                    if ord('a') <= key <= ord('z') and self.upper_flg:
                        text += chr(key).upper()
                    else:
                        text += chr(key)

    def publish_text(self,text):
        msg = String()
        msg.data = text
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    text_publisher = TextPublisher()
    rclpy.spin(text_publisher)
    text_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
