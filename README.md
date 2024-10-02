# Text Publisher for ROS2

ROS2ノードを使用して手動入力されたテキストをパブリッシュするアプリケーションです。

## 機能

- キーボードからテキストを手動で入力
- "SHIFT"を押すことで大文字と小文字の切り替え(初期は小文字)
- 入力されたテキストをROS2のトピックにパブリッシュ

## 実行方法
```bash
colcon build
ros2 run manual_package manual_publisher
