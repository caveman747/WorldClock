# This is a sample Python script.
import tkinter
from datetime import datetime
import pytz
from tkinter import *
from time import strftime

from PIL import ImageTk, Image

root = Tk()

#root.overrideredirect(True)
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
#                                        root.winfo_screenheight()))

mycolor = '#%02x%02x%02x' % (000, 37, 150)  # set your favourite rgb color

root.configure(bg=mycolor)


root.attributes("-fullscreen", True)

def times():
    home = pytz.timezone("America/Los_Angeles")
    local_time=datetime.now(home)
    datime = local_time.strftime('%H:%M:%S %p')
    clock1.config(text=datime, bg=mycolor)
    name1.config(text="Time in Eugene Oregon", bg=mycolor)
    clock1.after(200, times)

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

name1 = Label(root, font=("calibri", 20, "bold"))
name1.place(rely=.1, relx=.1)
clock1=Label(root, font=("calibri", 25, "bold"))
clock1.place(rely=.2, relx=.1)

path = "/home/tester/PycharmProjects/WorldClock /DL-2.jpg"

img = ImageTk.PhotoImage(Image.open(path))

panel = Label(root, image = img)

panel.place(rely=.25, relx=.12)

# name2 = Label(root, font=("times", 20, "bold"))
# name2.place(rely=.1, relx=.1)
# clock2=Label(root, font=("times", 25, "bold"))
# clock2.place(rely=.2, relx=.1)

times()

root.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
