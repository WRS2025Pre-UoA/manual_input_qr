from setuptools import setup

package_name = 'manual_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='motti',
    maintainer_email='motti@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'manual_publisher = manual_package.text_publisher:main',
        'manual_subscriber = manual_package.text_subscriber:main'

        ],
    },
)
