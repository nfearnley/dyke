import hexchat
import time

__author__ = "Nat Fearnley"
__copyright__ = "Copyright 2017"
__email__ = "nfearnley@gmail.com"

__module_name__ = "dyke"
__module_version__ = "1.0"
__module_description__ = "Personal flood prevention"

ENTER = '65293'
DELAY = 1

_time = 0
def keypress_cb(key, *args):
    global _time
    now = time.time()
    
    eat = hexchat.EAT_NONE
    
    wait = (_time + DELAY) - now
    
    if key[0] == ENTER and wait > 0:
        print("Slow Down! Wait {:.2f} more seconds.".format(wait))
        eat = hexchat.EAT_ALL
    else:
        _time = now
    return eat

hexchat.hook_print("Key Press", keypress_cb)
