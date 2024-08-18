import os, sys


def clamp(value, min, max):
    """Limits a Value
    """
    if value < min:
        return min
    if value > max:
        return max
    return value

def remap(value, min, max, targetMin, targetMax):
    """Remaps a value from one range to other
    
    Args:
        value (int or float): Value to remap
        min (int or float): lower bound of the value's current range
        max (int or float): upper bound of the value's current range
        targetMin (int or float ): lower bound of the value's target rang
        targetMax (int or flot): upper bound of the value's target range
    
    Returns:
        float: Remapped value
    """
    # Figure out how 'wide' each range is
    span = max - min
    targetSpan = targetMax - targetMin
    
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - min) / float(span)
    
    # Convert the 0-1 range into a value in the right range.
    return targetMin + (valueScaled * targetSpan)

def resource_path(relative_path):
    """ Returns the asset's path """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)



def collisions(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    return (a_x + a_width > b_x) and (a_x < b_x + b_width) and (a_y + a_height > b_y) and (a_y < b_y + b_height)



