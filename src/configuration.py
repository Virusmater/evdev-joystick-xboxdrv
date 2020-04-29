import os
from configparser import ConfigParser
from os.path import expanduser

conf_path = expanduser("~") + "/.config/evdev-joystick-xboxdrv/"


def store(evdev_keymap, evdev_absmap, axismap, name):
    if not os.path.exists(conf_path):
        os.mkdir(conf_path)
    conf_name = conf_path + __get_name(name)
    with open(conf_name, 'w') as outfile:
        # Add content to the file
        config = ConfigParser()
        config.optionxform = str
        config.add_section("axismap")
        for axis in axismap:
            config.set("axismap", axismap[axis], axis)
        config.add_section("evdev-absmap")
        for axe in evdev_absmap:
            config.set("evdev-absmap", evdev_absmap[axe], axe)
        config.add_section("evdev-keymap")
        for button in evdev_keymap:
            config.set("evdev-keymap", evdev_keymap[button], button)
        config.write(outfile)
        outfile.close()
    print("Configuration for", name, "was saved at", conf_name)


def __get_name(name):
    return name.replace(" ", "") + ".ini"