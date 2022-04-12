import time
from functions.arraytools import panjang

def admin_menu():
    pass
def user_menu():
    pass

def loading_animation():
    animation = "|/-\\|"
    for i in range(10):
        print("Loading", animation[i % panjang(animation)], end="\r")
        time.sleep(0.1)

def saving_animation():
    animation = [
        "[        ]",
        "[=       ]",
        "[==      ]",
        "[===     ]",
        "[====    ]",
        "[=====   ]",
        "[======  ]",
        "[======= ]",
        "[========]",
    ]

    for i in range(panjang(animation)):
        print(animation[i % panjang(animation)], end='\r')
        time.sleep(0.1)

    print("Saving success!")
