#for GUI it's the rug that brings the room together
import tkinter
#used in converting pytz object into a "time" to be displayed
from datetime import datetime
#stands for python timezones, self explanatory
import pytz
#modules responsible for pulling in images
from PIL import ImageTk, Image

#creates a tkinter window object with fullscreen attributes
root = tkinter.Tk()
root.attributes("-fullscreen", True)

#datalogic color with slight alterations to better blend with background image
mycolor = '#%02x%02x%02x' % (2, 30, 110)

#directory locations of images used as background
imageEugene = ImageTk.PhotoImage(Image.open("/home/tester/PycharmProjects/WorldClock2/LockScreen-Eugene.png"))
imageBologna = ImageTk.PhotoImage(Image.open("/home/tester/PycharmProjects/WorldClock2/LockScreen-Bologna..png"))
imageVietnam = ImageTk.PhotoImage(Image.open("/home/tester/PycharmProjects/WorldClock2/LockScreen-Vietnam.png"))

#creates list of directory locations for required images to iterate through
imagelist = [imageEugene, imageBologna, imageVietnam]

#creates pytz timezone objects
tzEugene = pytz.timezone("America/Los_Angeles")
tzBologna = pytz.timezone("Europe/Rome")
tzVietnam = pytz.timezone("Asia/Ho_Chi_Minh")

#creates list of pytz objects to iterate through
timezonelist = [tzEugene, tzBologna, tzVietnam]


def times(timezone, timezonelist, nextindex):
    local_time=datetime.now(timezonelist[nextindex])
    datime = local_time.strftime('%H:%M %p')
    clock.config(text=datime)
    name.config(text="Time in Eugene Oregon")
    clock.after(60000, lambda: times(timezone, timezonelist, (nextindex+1) % len(imagelist)))

def change_image(label, imagelist, nextindex):
    background_label.configure(image=imagelist[nextindex])
    root.after(60000, lambda: change_image(label, imagelist, (nextindex+1) % len(imagelist)))

background_label = tkinter.Label(root)
background_label.pack(fill=tkinter.BOTH)

name = tkinter.Label(root, fg= "white", bg=mycolor, font=("calibri", 20, "bold"))
name.place(rely=.85, relx=.15)
clock = tkinter.Label(root, fg="white", bg=mycolor, font=("calibri", 25, "bold"))
clock.place(rely=.9, relx=.15)

times(clock, timezonelist, 0)

change_image(background_label, imagelist, 0)

root.mainloop()