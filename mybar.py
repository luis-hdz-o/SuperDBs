from alive_progress import alive_bar
from time import sleep

with alive_bar(100) as bar:   # default setting
    for i in range(100):
        sleep(0.03)
        bar() 