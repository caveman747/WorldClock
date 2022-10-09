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
mycolor = '#%02x%02x%02x' % (15, 35, 110)

#directory locations of images used as background
imageEugene = ImageTk.PhotoImage(Image.open("/home/itstats/WorldClock/LockScreen-Eugene.png"))
imageBologna = ImageTk.PhotoImage(Image.open("/home/itstats/WorldClock/LockScreen-Bologna.png"))
imageVietnam = ImageTk.PhotoImage(Image.open("/home/itstats/WorldClock/LockScreen-Vietnam.png"))

#creates list of directory locations for required images to iterate through
imagelist = [imageEugene, imageBologna, imageVietnam]

#creates pytz timezone objects
tzEugene = pytz.timezone("America/Los_Angeles")
tzBologna = pytz.timezone("Europe/Rome")
tzVietnam = pytz.timezone("Asia/Ho_Chi_Minh")

#creates list of pytz objects to iterate through
timezonelist = [tzEugene, tzBologna, tzVietnam]

nameEugene = "Local Time in Eugene"
nameMonteSanPietro = "Local Time in Bologna"
nameHoChiMinhCity = "Local Time in Ho Chi Minh City"

nameList = [nameEugene, nameMonteSanPietro, nameHoChiMinhCity]

#recursive function with no base case ripped from https://www.youtube.com/watch?v=zFCp7iczAPk and made recursive with help by looking at https://stackoverflow.com/questions/39025637/tkinter-changing-image-live-after-a-given-time
#iterates over timezonelist and displays a different HH::MM UTC and description every minute - Eugene, Bologna, and Vietnam
def times(timezone, timezonelist, nameList, nextindex):
    name.config(text=nameList[nextindex])
    local_time=datetime.now(timezonelist[nextindex])
    datime = local_time.strftime('%H:%M')
    clock.config(text=datime)
    #recursive call
    clock.after(60000, lambda: times(timezone, timezonelist, nameList, (nextindex+1) % len(imagelist)))

#recursive function with no base case ripped from https://www.youtube.com/watch?v=zFCp7iczAPk and made recursive with help by looking at https://stackoverflow.com/questions/39025637/tkinter-changing-image-live-after-a-given-time
#iterates over timezonelist and displays different images of these sites in the bottom right- Eugene, Bologna, and Vietnam
def change_image(label, imagelist, nextindex):
    background_label.configure(image=imagelist[nextindex])
    #recursive call
    root.after(60000, lambda: change_image(label, imagelist, (nextindex+1) % len(imagelist)))

#gets the label configured in the function change_imaged
background_label = tkinter.Label(root)
background_label.pack(fill=tkinter.BOTH)

#label configured in the function times
name = tkinter.Label(root, fg= "white", bg=mycolor, font=("helvetica", 21, "bold"))
name.place(rely=.85, relx=.80)

#clock configured in the function times
clock = tkinter.Label(root, fg="white", bg=mycolor, font=("helvetica", 23, "bold"))
clock.place(rely=.9, relx=.80)

#functional call parameters tkinter label, list of pytz timezones, list of site name strings, and starting index number
change_image(background_label, imagelist, 0)

#functional call parameters tkinter label, list of pytz timezones, list of site name strings, and starting index number
times(clock, timezonelist, nameList, 0)

#ends the tkinter loop - black magic that is alpha and omega for the tkinter object - root
root.mainloop()