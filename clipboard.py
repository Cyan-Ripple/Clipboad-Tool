import time
import os
import pyperclip
from PIL import ImageGrab


def fallback(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return True
        except Exception as e:
            return False
    return wrapper


@fallback
def exec_grab():
    img = ImageGrab.grabclipboard()
    name = hex(int(time.strftime("%m%d%H%M%S", time.localtime())))[2:]
    img.save(f'{name}.png', "png")
    print("Screen Shot Saved as")
    print(name)


@fallback
def exec_strip():
    """logic"""
    content = pyperclip.paste().replace('\r\n', '').replace('\n', '')
    pyperclip.copy(content)
    print(content)


if __name__ == '__main__':
    flag = exec_grab() or exec_strip()

    os.system(f"color {'03' if flag else '47'}")
    time.sleep(2)
