# NOTE : we can not use grid and pack layout manager at the same time.
#        To use them together use the frame
from tkinter import *
from tkinter import ttk
import os
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox
import time
from mutagen.mp3 import MP3
import threading


global check

paused = FALSE
muted = FALSE
index = 0

# STATUS BAR


def show_details(play_song): # show details
    global filename_path
    
    filelabel['text'] = 'Playing'+' - '+os.path.basename(play_song)
    file_data = os.path.splitext(play_song)
    #print(filename_path)
    #print(file_data)
    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        totallength = audio.info.length
        #print(totallength) 
    else:    
        a = mixer.sound(play_song)  #use sound for wav file provided by mixer
  # FOR wav file , not for mp3
        totallength = a.get_length() # this include pause time also ERROR 
        
    mins,secs = divmod(totallength,60) # storing quotient in mins and remainder in secs
    print(round(mins))
    print(round(secs))
    #time_format = '{:2d}:{:2d}'.format(mins, secs)  #02d: show 0(optional) +2 digits + d:int
    #print(time_format)
    lengthlabel['text']= 'Total Length' + ' - '+ str(round(mins)) + ':' +str(round(secs))

    t1 = threading.Thread(target=time_counter, args=(totallength,)) 
    t1.start()
    
def play_btn():                                                                                                 # PLAY BUTTON
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text']='Music Resumed'
        paused = FALSE
    else:    
        try:
            stop_btn()
            time.sleep(1)
            selected_song = playlist.curselection()
            selected_song = int(selected_song[0])
            play_it = pllist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text']='NOW :'+os.path.basename(play_it)
            show_details(play_it)
        except:
            tkinter.messagebox.showerror('FILE NOT FOUND',' WE COULD NOT FETCH THE FILE. PLEASE SHOW THE DIRECTORY')
            print('ERROR: WE COULD NOT FETCH')
                    
def stop_btn():
    mixer.music.stop()
    statusbar['text']='WELCOME TO PLAY NOW'
            
def set_vol(val):
    vol = int(val)/100
    mixer.music.set_volume(vol)

def about_us():
    tkinter.messagebox.showinfo('ABOUT US','THIS IS A MUSIC PLAYER......')

# full path is required to play a music so
# we will save full path in pllist
pllist = []

def add_to_playlist(filename):
    global index
    global filename_path
    filename = os.path.basename(filename)
    playlist.insert(index,filename)
    pllist.insert(index,filename_path)
    index += 1
    
    
def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)
    
            
def pause_btn():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text']='Music Paused'
    print('pausee')


def muteAndvolume_btn():
    global muted
    
    if muted:
        mixer.music.set_volume(70)
        volume_btn.configure(image=volume_photo)
        scale.set(70)
        muted = FALSE
            
    else:
                
        mixer.music.set_volume(0)
        volume_btn.configure(image=mute_photo)
        scale.set(0)
        muted=TRUE

def rewind_btn():
    play_btn()
    statusbar['text']='Music Played'

def delsong():
    selected_song = playlist.curselection()
    selected_song = int(selected_song[0])
    playlist.delete(selected_song)
    pllist.pop(selected_song) # can use remove that need file name

# Root frame

root=Tk()
root.config(background='plum3')

# Statusbar
statusbar = Label(root,text='WELCOME TO PLAY NOW',relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill= X)

# CREATE FRAME

rightframe = Frame(root)
rightframe.pack(side = RIGHT)


topframe = Frame(rightframe)
topframe.pack()

middleframe = Frame(rightframe ) #Frame(root,relief= RAISED, borderwidth=1)
middleframe.pack(padx=10,pady=10)

leftframe = Frame(root)
leftframe.pack(side = LEFT,padx = 10,pady= 10)

bottomframe = Frame(rightframe) #Frame(root,relief= RAISED, borderwidth=1)
bottomframe.pack(padx=20,pady=30)

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

# for playList
 # listbox
playlist = Listbox(leftframe)
playlist.pack(pady = 5)
 #button
addbtn = Button(leftframe,text = '+ Add',command = browse_file)
addbtn.pack(side = LEFT)
deletebtn = Button(leftframe,text = '- Del',command = delsong)
deletebtn.pack(side = RIGHT)

# file label showing the length and the music being played
filelabel = Label(leftframe,text='Lets, Play It Now !')
filelabel.pack(pady=10) # packing and adding padding

# length label
lengthlabel = Label(leftframe,text='Length : --:-- ')
lengthlabel.pack() # packing and adding padding

currenttimelabel = Label(leftframe,text='Current time : --:--',relief = GROOVE)
currenttimelabel.pack(pady=10)

# PLAY BUTTON
play_photo = PhotoImage(file='play.png')
playmusic_btn = Button(middleframe, text="Play",command=play_btn,image=play_photo)
playmusic_btn.pack(side = LEFT,padx=5)

# STOP BUTTON
stop_photo = PhotoImage(file='stop.png')
stopmusic_btn = Button(middleframe, text="Stop",command=stop_btn,image=stop_photo)
stopmusic_btn.pack(side=LEFT,padx=5)

# PAUSE BUTTON
pause_photo = PhotoImage(file='pause.png')
pausemusic_btn = Button(middleframe, text="Pause",command=pause_btn,image =pause_photo)
pausemusic_btn.pack(side=LEFT,padx=5)

# mute and volume button 
mute_photo = PhotoImage(file='mute.png')
volume_photo = PhotoImage(file='volume.png')
volume_btn = Button(middleframe,command=muteAndvolume_btn,image=volume_photo)
volume_btn.pack(side=LEFT,padx=5)

# REWIND
rewind_photo = PhotoImage(file='rewind.png')
rewindmusic_btn = Button(bottomframe,image=rewind_photo,command=rewind_btn)
rewindmusic_btn.grid(row=0,column=0)  # NOTE : used grid instead of pack

#CONTROL VOLUME
scale = Scale(bottomframe,from_=0, to=100 , orient=HORIZONTAL , command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.grid(pady=12,padx=30,row=0,column=1)


# STOP MUSIC ON EXITING WINDOW USING CROSS
def on_closing():
    stop_btn()
    root.destroy()
    
root.protocol('WM_DELETE_WINDOW',on_closing) # for red cross button

def time_counter(t):
    while t and mixer.music.get_busy():
        print(mixer.music.get_busy())
        mins,secs = divmod(t,60) # storing quotient in mins and remainder in secs
        currenttimelabel['text']= 'Current time :' + ' - '+ str(round(mins)) + ':' +str(round(secs))
        time.sleep(1) # in s
        t=t-1
# NOTE : SINCE WHILE LOOP WILL ENGAGE CPU FOR THE TOTALTIME THEREFORE WE
# CAN USE THREADING
root.mainloop()
    
