import evdev
from evdev import ecodes, resolve_ecodes_dict, categorize
import time
from evdev_joystick_xboxdrv.configuration import store
from enum import Enum


class Button(Enum):
    Start = ("start")
    Guide = ("xbox")
    Back = ("select")
    A = ("south")
    B = ("east")
    X = ("west")
    Y = ("north")
    LB = ("left bumper")
    RB = ("right bumper")
    LT = ("left trigger")
    RT = ("right trigger")
    TL = ("thumb left")
    TR = ("thumb right")
    DPAD_UP = ("up")
    DPAD_DOWN = ("down")
    DPAD_LEFT = ("left")
    DPAD_RIGHT = ("right")

    def __init__(self, description):
        self.description = description


class Axe(Enum):
    X1 = ("left stick horizontal", "tilt left")
    Y1 = ("left stick vertical", "tilt down")
    X2 = ("right stick horizontal", "tilt left")
    Y2 = ("right stick vertical", "tilt down")

    def __init__(self, description, instruction):
        self.description = description
        self.instruction = instruction


timeout = 3


def get_button_name(ecodes_key, event_code):
    for name in resolve_ecodes_dict(({ecodes_key: [event_code]})):
        name_a = name[1][0][0]
        if isinstance(name_a, list):
            return name[1][0][0][0]
        else:
            return name[1][0][0]


def map_buttons(device):
    evdev_keymap = {}
    for button in Button:
        print("press button", button.name, "(" + button.description + ")",
              "or wait", timeout, "sec. and press any button to skip")
        start_time = time.time()
        for event in device.read_loop():
            if event.type == ecodes.EV_KEY and event.value == 1:
                if timeout + start_time < time.time():
                    print("timeout")
                    break
                name = get_button_name(ecodes.EV_KEY, event.code)
                print(name)
                evdev_keymap[button.name] = name
                time.sleep(0.5)
                break
    return evdev_keymap


def map_axes(device):
    evdev_absmap = {}
    axismap = {}
    for axe in Axe:

        print(axe.instruction, axe.name, "(" + axe.description + ")", "and hold for",
              timeout, "sec. or press any button to skip")
        start_time = time.time()
        temp_axes = {}
        # flush pending events since sometimes gamepad is spamming with events
        while device.read_one() is not None:
            pass
        for event in device.read_loop():
            if event.type == ecodes.EV_ABS:
                # print(categorize(event) , event.value)
                name = get_button_name(ecodes.EV_ABS, event.code)
                if name not in temp_axes:
                    temp_axes[name] = event.value
                else:
                    if temp_axes[name] < abs(event.value):
                        temp_axes[name] = event.value
                if timeout + start_time < time.time():
                    max_axe = max(temp_axes, key=lambda y: abs(temp_axes[y]))
                    evdev_absmap[axe.name] = max_axe
                    print(max_axe)
                    print("release axe", axe.name)
                    # check inversion
                    if temp_axes[max_axe] > 0:
                        axismap[axe.name] = "-" + axe.name
                    time.sleep(0.5)
                    break
            if event.type == ecodes.EV_KEY and event.value == 1:
                print("skip")
                break
    return evdev_absmap, axismap


def main():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print('Available devices:')
    for index, device in enumerate(devices):
        caps = device.capabilities()
        if ecodes.EV_ABS in device.capabilities():
            print(index, device.name)
            device_path = device.path
    print('Pick one device for the mapping:', end=" ")
    index = int(input())
    device = devices[index]
    store(map_buttons(device), *map_axes(device), device.name)


if __name__ == '__main__':
    main()
