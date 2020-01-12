from tkinter import *
import pygame
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os

win = Tk()
win.geometry('300x200')
win.title('Music Player')
win.minsize(300, 200)
win.maxsize(300, 200)
win.configure(background='violet')


pygame.init()
pygame.mixer.init()

def Open_Music():
    global file
    file = askopenfile(mode='r')
    Play_Music()

def Play_Music():
    global sound
    sound = True

    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    l1 = Label(text='Music Playing:\n' + os.path.basename(file.name))
    l1.place(anchor=CENTER, relx=0.5, rely=0.4)

def Pause_Music():
    global sound
    if sound == True:
        pygame.mixer.music.pause()
        sound = False

    elif sound == False:
        pygame.mixer.music.unpause()
        sound = True

def Stop_Music():
    pygame.mixer.music.stop()


# Main Menu
mainmenu = Menu(win)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label='Open', command=Open_Music)
win.config(menu=mainmenu)
mainmenu.add_cascade(label='File', menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label='Cut')
win.config(menu=mainmenu)
mainmenu.add_cascade(label='Edit', menu=m2)

                
icon = Image.open(r'C:\Users\Rapter\Downloads\Play.png')
image = icon.resize((40, 40), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

icon2 = Image.open(r'C:\Users\Rapter\Downloads\stop-button.png')
image2 = icon2.resize((40, 40), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)

icon3 = Image.open(r'C:\Users\Rapter\Downloads\pause.png')
image3 = icon3.resize((40, 40), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)


Play = Button(text='Play', command=Play_Music, image=photo)
Play.grid(row=0, column=1, padx=0, pady=150)

Pause = Button(text='Pause', command=Pause_Music, image=photo3)
Pause.grid(row=0, column=0, padx=35, pady=150)

Stop = Button(text='Stop', command=Stop_Music, image=photo2)
Stop.grid(row=0, column=2, padx=35, pady=150)

win.mainloop()
