# This is a sample Python script.

from datetime import datetime
import pytz
from tkinter import *
from time import strftime

root = Tk()
root.geometry("300x250")

def times():
    home = pytz.timezone("America/Los_Angeles")
    local_time=datetime.now(home)
    datime = local_time.strftime('%H:%M:%S %p')
    clock.config(text=datime)
    name.config(text="US")

    home = pytz.timezone("America/Los_Angeles")
    local_time=datetime.now(home)
    datime = local_time.strftime('%H:%M:%S %p')
    clock2.config(text=datime)
    name.config(text="Italy")

    # home = pytz.timezone("America/Los_Angeles")
    # local_time=datetime.now(home)
    # datime = local_time.strftime('%H:%M:%S %p')
    # clock3.config(text=datime)
    # name.config(text="Vietnam")
    #
    # home = pytz.timezone("America/Los_Angeles")
    # local_time=datetime.now(home)
    # datime = local_time.strftime('%H:%M:%S %p')
    # clock4.config(text=datime)
    # name.config(text="Slovakia")

name = Label(root, text="Eugene OR", font=("times", 20, "bold"))
name.place(x=30,y=5)
clock=Label(root, text="Eugene, OR, USA", font=("times", 25, "bold"))
clock.place(x=10, y=40)

# name = Label(root, text="Eugene OR", font=("times", 20, "bold"))
# name.place(x=200,y=80)
# clock2=Label(root, text="Eugene, OR, USA", font=("times", 25, "bold"))
# clock.place(x=200, y=80)



times()


root.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
