# evdev-joystick-xboxdrv
Easy and simple tool to generate a xboxdrv config.

Wait for 3 seconds and press any button to skip the mapping in case the controller doesn't support the button (like thumb buttons on Nintendo Wii Classic Controller)

Press any button during analogs mapping to skip if the controller doesn't have em.
# install
```bash
$ sudo apt install python3-pip git -y
$ sudo pip3 install git+https://github.com/Virusmater/evdev-joystick-xboxdrv
```
# example
```bash
$ evdev-joystick-xboxdrv 
Available devices:
0 Nintendo Wii Remote Pro Controller
Pick one device for the mapping: 0
press button Start (start) or wait 3 sec. and press any button to skip
BTN_START
press button Guide (xbox) or wait 3 sec. and press any button to skip
BTN_MODE
press button Back (select) or wait 3 sec. and press any button to skip
BTN_SELECT
press button A (south) or wait 3 sec. and press any button to skip
BTN_A
press button B (east) or wait 3 sec. and press any button to skip
BTN_B
press button X (west) or wait 3 sec. and press any button to skip
BTN_WEST
press button Y (north) or wait 3 sec. and press any button to skip
BTN_NORTH
press button LB (left bumper) or wait 3 sec. and press any button to skip
BTN_TL
press button RB (right bumper) or wait 3 sec. and press any button to skip
BTN_TR
press button LT (left trigger) or wait 3 sec. and press any button to skip
BTN_TL2
press button RT (right trigger) or wait 3 sec. and press any button to skip
BTN_TR2
press button TL (thumb left) or wait 3 sec. and press any button to skip
BTN_THUMBL
press button TR (thumb right) or wait 3 sec. and press any button to skip
BTN_THUMBR
press button DPAD_UP (up) or wait 3 sec. and press any button to skip
BTN_DPAD_UP
press button DPAD_DOWN (down) or wait 3 sec. and press any button to skip
BTN_DPAD_DOWN
press button DPAD_LEFT (left) or wait 3 sec. and press any button to skip
BTN_DPAD_LEFT
press button DPAD_RIGHT (right) or wait 3 sec. and press any button to skip
BTN_DPAD_RIGHT
tilt left X1 (left stick horizontal) and hold for 3 sec. or press any button to skip
ABS_X
release axe X1
tilt down Y1 (left stick vertical) and hold for 3 sec. or press any button to skip
ABS_Y
release axe Y1
tilt left X2 (right stick horizontal) and hold for 3 sec. or press any button to skip
ABS_RX
release axe X2
tilt down Y2 (right stick vertical) and hold for 3 sec. or press any button to skip
ABS_RY
release axe Y2
Configuration for Nintendo Wii Remote Pro Controller was saved at /home/kompot/.config/evdev_joystick_xboxdrv/NintendoWiiRemoteProController.ini
```
# use
```bash
$ xboxdrv --evdev /dev/input/event21  --mimic-xpad --config /home/user/.config/evdev-joystick-xboxdrv/NintendoWiiRemoteProController.ini
```