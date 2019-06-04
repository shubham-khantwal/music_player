# NOTE : we can not use grid and pack layout manager at the same time.
#        To use them together use the frame
from tkinter import *
import os
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

# for user defined exception

global seven

seven=7
print(seven)

# user defined exception ends
def play_btn():
    try: # checking  is paused variable is initialised
        print('play button') #
        print('hello')
        if seven > 0:
            print(seven)
            throw
                
    except:
        try:
            print('except') # 
            mixer.music.load(filename)
            print('filename')#
            mixer.music.play()
            statusbar['text']='Playing '+os.path.basename(filename)
        except:
            print('exceptit')#
            tkinter.messagebox.showerror('FILE NOT FOUND',' WE COULD NOT FETCH THE FILE. PLEASE SHOW THE DIRECTORY')
            print('ERROR: WE COULD NOT FETCH')
                    
    else: # executes after  try if except does not execute
        mixer.music.unpause()
        print('unpause') #
        check = False
        statusbar['text']='Music Resumed'

def stop_btn():
    mixer.music.stop()
    statusbar['text']='WELCOME TO PLAY NOW'
            
def set_vol(val):
    vol = int(val)/100
    mixer.music.set_volume(vol)

def about_us():
    tkinter.messagebox.showinfo('ABOUT US','THIS IS A MUSIC PLAYER......')

def browse_file():
    global filename
    filename = filedialog.askopenfilename()
            
def pause_btn():
    global check
    print('pause button')
    # get_busy()
    print(seven)
    seven = 0
    print(seven)
    check = True
    mixer.music.pause()
    statusbar['text']='Music Paused'


def muteAndvolume_btn():
    global muted       
    if muted:
        mixer.music.set_volume(70)
        volume_btn.configure(image=volume_photo)
        scale.set(70)
        muted = False
            
    else:
                
        mixer.music.set_volume(0)
        volume_btn.configure(image=mute_photo)
        scale.set(0)
        muted=True


def rewind_btn():
            
    play_btn()
    statusbar['text']='Music Played'
            
root= Tk()

# CREATE FRAME

middleframe = Frame(root ) #Frame(root,relief= RAISED, borderwidth=1)
middleframe.pack(padx=10,pady=10)

bottomframe = Frame(root) #Frame(root,relief= RAISED, borderwidth=1)
bottomframe.pack()

# CREATE MENUBAR
menubar = Menu(root)
root.config(menu=menubar)

# CREATE SUBMENU
submenu = Menu(menubar , tearoff=0)
menubar.add_cascade(label='FILE',menu=submenu)
submenu.add_command(label='Open',command=browse_file)
submenu.add_command(label='Exit',command=root.destroy)


# CREATE SUBMENU
submenu = Menu(menubar , tearoff=0)
menubar.add_cascade(label='HELP',menu=submenu)
submenu.add_command(label='About Us',command=about_us)



mixer.init()  #initializing mixer 

# SET SIZE OF APP
# root.geometry('300x300')
# SET TITLE OF APP
        
root.title('PLAY NOW')

# SET ICON FOR APP
root.iconbitmap('icon.ico')
text= Label(root,text='Lets, Play It Now !')
text.pack(pady=10) # packing and adding padding

# PLAY BUTTON
play_photo = PhotoImage(file='play.png')
play_btn = Button(middleframe, text="Play",command=play_btn,image=play_photo)
play_btn.pack(side = LEFT,padx=5)

# STOP BUTTON
stop_photo = PhotoImage(file='stop.png')
stop_btn = Button(middleframe, text="Stop",command=stop_btn,image=stop_photo)
stop_btn.pack(side=LEFT,padx=5)

# PAUSE BUTTON
pause_photo = PhotoImage(file='pause.png')
pause_btn = Button(middleframe, text="Pause",command=pause_btn,image =pause_photo)
pause_btn.pack(side=LEFT,padx=5)

# mute and volume button
mute_photo = PhotoImage(file='mute.png')
volume_photo = PhotoImage(file='volume.png')
volume_btn = Button(middleframe, text="",command=muteAndvolume_btn,image =volume_photo)
volume_btn.pack(side=LEFT,padx=5)

# REWIND
rewind_photo = PhotoImage(file='rewind.png')
rewind_btn = Button(bottomframe,command=rewind_btn,image =rewind_photo)
rewind_btn.grid(row =0,column=1,padx=5)  # NOTE : used grid instead of pack

#CONTROL VOLUME
scale = Scale(root,from_=0, to=100 , orient=HORIZONTAL , command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack(pady=17)

# STATUS BAR

statusbar = Label(root,text='WELCOME TO PLAY NOW',relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill= X)

  
root.mainloop()
    
