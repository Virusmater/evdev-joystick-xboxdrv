from setuptools import setup, find_packages

setup(
    name='evdev-joystick-xboxdrv',
    version='0.1',
    description='Easy and simple tool to generate a xboxdrv config',
    url='https://github.com/Virusmater/evdev-joystick-xboxdrv',
    author='Dima Kompot',
    author_email='virusmater@gmail.com',
    license='MIT',
    install_requires=['evdev'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['evdev-joystick-xboxdrv=evdev_joystick_xboxdrv.__main__:main']
    )
)
