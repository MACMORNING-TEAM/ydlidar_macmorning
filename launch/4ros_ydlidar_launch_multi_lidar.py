from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import LifecycleNode, Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    share_dir = get_package_share_directory('ydlidar_ros2_driver')

    # Declare launch arguments for two param files
    param_file_1 = LaunchConfiguration('params_file_1')
    param_file_2 = LaunchConfiguration('params_file_2')

    params_declare_1 = DeclareLaunchArgument(
        'params_file_1',
        default_value=os.path.join(share_dir, 'params', 'ydlidar_4ros_1.yaml'),
        description='Path to the first LiDAR parameters file.'
    )

    params_declare_2 = DeclareLaunchArgument(
        'params_file_2',
        default_value=os.path.join(share_dir, 'params', 'ydlidar_4ros_2.yaml'),
        description='Path to the second LiDAR parameters file.'
    )

    # First LiDAR node
    lidar_node_1 = LifecycleNode(
        package='ydlidar_ros2_driver',
        executable='ydlidar_ros2_driver_node',
        name='ydlidar_node_1',
        namespace='',
        output='screen',
        parameters=[param_file_1]
    )

    # Second LiDAR node
    lidar_node_2 = LifecycleNode(
        package='ydlidar_ros2_driver',
        executable='ydlidar_ros2_driver_node',
        name='ydlidar_node_2',
        namespace='',
        output='screen',
        parameters=[param_file_2]
    )

    return LaunchDescription([
        params_declare_1,
        params_declare_2,
        lidar_node_1,
        lidar_node_2
    ])
