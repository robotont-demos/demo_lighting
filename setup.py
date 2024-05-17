from setuptools import find_packages, setup

package_name = 'demo_lighting'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Raimo Köidam',
    maintainer_email='raimokoidam@gmail.com',
    description='Robotont lighting demo package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo_lighting = demo_lighting.demo_lighting:main',
            'demo_lighting_scan = demo_lighting.demo_lighting_scan:main',
            'demo_lighting_manual = demo_lighting.demo_lighting_manual:main'
        ],
    },
)
