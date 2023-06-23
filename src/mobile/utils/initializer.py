import importlib.util
import os.path
import inspect
import importlib
from appium.webdriver import Remote


def init_page(driver: Remote, base_class):
    # get path with file name of base_class
    base_class_dir = inspect.getmodule(base_class).__file__
    # get directory where is placed module base_class
    module_dir = base_class_dir[:base_class_dir.rfind('/')]

    # choose needed OS for finding a required class
    if "uiautomator2" in driver.capabilities["automationName"]:
        operating_system = "android"
    else:
        operating_system = "IOS"
    # search for the directory where the classes for the selected OS are stored
    while not os.path.isdir(os.path.join(module_dir, operating_system)):
        module_dir = os.path.abspath(os.path.join(module_dir, "../"))

    # when directory is found set module_dir this directory
    module_dir = os.path.join(module_dir, operating_system)

    # loop through all files in module_dir  to find a required module
    for file in os.listdir(module_dir):
        # we search only files
        if os.path.isfile(os.path.join(module_dir, file)):
            # get a module name without extension
            module_name = os.path.splitext(file)[0]
            # get spec from this
            spec = importlib.util.spec_from_file_location(module_name, os.path.join(module_dir, file))
            # some magic ?
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # define a map to saving a module attributes
            map_of_attribute = {}
            # loop for initialize map
            for attribute_name in dir(module):
                map_of_attribute[attribute_name] = getattr(module, attribute_name)
            # looking for a module whose class is inherited from base_class
            if base_class.__name__ in map_of_attribute.keys():
                # looping to find a attribute class name
                for attribute in map_of_attribute.values():
                    if isinstance(attribute, type) and issubclass(attribute, base_class) and attribute != base_class:
                        return attribute(driver)
