# This is a sample Python script.

from datetime import datetime
import pytz
from tkinter import *
from time import strftime

root = Tk()

#root.overrideredirect(True)
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
#                                        root.winfo_screenheight()))


root.attributes("-fullscreen", True)

def times():
    home = pytz.timezone("America/Los_Angeles")
    local_time=datetime.now(home)
    datime = local_time.strftime('%H:%M:%S %p')
    clock1.config(text=datime)
    name1.config(text="US")

    # home = pytz.timezone("Europe/Rome")
    # local_time=datetime.now(home)
    # datime = local_time.strftime('%H:%M:%S %p')
    # clock2.config(text=datime)
    # name2.config(text="Italy")

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

name1 = Label(root, font=("times", 20, "bold"))
name1.place(rely=.5, relx=.5)
clock1=Label(root, font=("times", 25, "bold"))
clock1.place(rely=0, relx=0)

# name2 = Label(root, text="Eugene OR", font=("times", 20, "bold"))
# name2.place(x=400,y=5)
# clock2=Label(root, text="Eugene, OR, USA", font=("times", 25, "bold"))
# clock2.place(x=100, y=40)



times()


root.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
