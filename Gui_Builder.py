# A class to build each GUI for Vaaya.
# tkinter based.
# Not sure if we need another class for interaction with SQLite
# CLICK-ABLE PICTURE BUTTON
# b = tk.Button(root, image=photo, command=on_click)
# Try importing the open source emojis
from tkinter import *
from tkinter import font

main_window = Tk()
main_window.geometry("700x600+350+100")
main_window.resizable(0, 0)
main_window.title("")
background_color = "#A2D2FF"
main_window.config(background=background_color)
theFont = font.Font(family="Franklin Gothic Medium Cond", size=16)
theLargeFont = font.Font(family="Franklin Gothic Medium Cond", size=24)
theSmallFont = font.Font(family="Franklin Gothic Medium Cond", size=10)

# Use a save button or something to make a new button in the scroll window.

def load_text_window(icon, emotion):  # STILL NEED TO ADD SQL ON THE "SIDE BAR" FUNCTIONALITY
    text_window = Toplevel()
    text_window.geometry("700x600+350+100")  # 700x600 size gui, placed at (350, 100) on the screen
    text_window.resizable(0, 0)
    text_window.title("")
    text_window.config(background=background_color)
    icon_label = Label(text_window, image=icon, background=background_color)
    icon_label.place(x=575, y=5)
    description_label = Label(text_window, text="Describe why you felt " + str(emotion) + " today", font=theLargeFont,
                              background=background_color)
    description_label.place(x=125, y=45)
    user_entry = Text(text_window, height=26, width=67)
    user_entry.place(x=125, y=125)
    save_button = Button(text_window, text="Save Entry", font=theSmallFont)
    save_button.place(x=375, y=560)
    ####CALL METHOD HERE ON SAVE CLICK###
    
    frame = Frame(text_window, width=90, height=450)
    frame.place(x=10, y=125)
    #####################SCROLL REGION################################
    scroll_canvas = Canvas(frame, bg=background_color, width=90, height=450, scrollregion=(0, 0, 500, 500))
    scrollbar = Scrollbar(frame, orient=VERTICAL)
    scrollbar.pack(side=LEFT, fill=Y)
    scrollbar.config(command=scroll_canvas.yview)
    scroll_canvas.config(xscrollcommand=scrollbar.set)
    scroll_canvas.pack(side=LEFT, fill=Y)
    #scroll_canvas.place(x=10, y=125)
    scrollbar.config(command=scroll_canvas.yview)

    text_window.mainloop()


# Change the background to blue.
def change_to_blue():
    global background_color
    background_color = "#A2D2FF"


# Change the background to red.
def change_to_red():
    global background_color
    background_color = "#FF0000"


# Change the background to green.
def change_to_green():
    global background_color
    background_color = "#008000"

    
def load_settings_window():
    settings_window = Toplevel()
    settings_window.geometry("300x50+350+100")
    settings_window.resizable(0, 0)
    settings_window.title("")
    settings_window.config(background=background_color)

    background_label = Label(settings_window, background=background_color, text="Background Color:", font=theFont)
    background_label.place(x=0, y=0)
    blue_button = Button(settings_window, background="#A2D2FF", command=change_to_blue)
    blue_button.place(x=155, y=5)
    red_button = Button(settings_window, background="red", command=change_to_red)
    red_button.place(x=175, y=5)
    green_button = Button(settings_window, background="green", command=change_to_green)
    green_button.place(x=195, y=5)
    settings_window.mainloop()


# Build buttons
how_are_you_label = Label(text="How are you feeling today?", font=theLargeFont, background=background_color)
how_are_you_label.place(x=195, y=195)

logo = PhotoImage(file="vaaya_logo.gif")
logoCanvas = Label(image=logo)
logoCanvas.place(x=200, y=25)

smiley_face = PhotoImage(file="vaaya_smiley.gif")
smiley_face_button = Button(main_window, image=smiley_face, height=100, width=100,
                            command=lambda: load_text_window(smiley_face, "happy"))
smiley_face_button.place(x=25, y=300)
smiley_face_label = Label(text="Happy", font=theFont, background=background_color)
smiley_face_label.place(x=45, y=420)

sad_face = PhotoImage(file="vaaya_sad.gif")
sad_face_button = Button(main_window, image=sad_face, height=100, width=100,
                         command=lambda: load_text_window(sad_face, "sad"))
sad_face_button.place(x=135, y=300)
sad_face_label = Label(text="Sad", font=theFont, background=background_color)
sad_face_label.place(x=165, y=420)

angry_face = PhotoImage(file="vaaya_angry.gif")
angry_face_button = Button(main_window, image=angry_face, height=100, width=100,
                           command=lambda: load_text_window(angry_face, "angry"))
angry_face_button.place(x=245, y=300)
angry_face_label = Label(text="Angry", font=theFont, background=background_color)
angry_face_label.place(x=272, y=420)

surprised_face = PhotoImage(file="vaaya_surprise.gif")
surprised_face_button = Button(main_window, image=surprised_face, height=100, width=100,
                               command=lambda: load_text_window(surprised_face, "surprised"))
surprised_face_button.place(x=355, y=300)
surprised_face_label = Label(text="Surprised", font=theFont, background=background_color)
surprised_face_label.place(x=365, y=420)

fearful_face = PhotoImage(file="vaaya_fear.gif")
fearful_face_button = Button(main_window, image=fearful_face, height=100, width=100,
                             command=lambda: load_text_window(fearful_face, "fearful"))
fearful_face_button.place(x=465, y=300)
fearful_face_label = Label(text="Fear", font=theFont, background=background_color)
fearful_face_label.place(x=495, y=420)

disgusted_face = PhotoImage(file="vaaya_disgusted.gif")
disgusted_face_button = Button(main_window, image=disgusted_face, height=100, width=100,
                               command=lambda: load_text_window(disgusted_face, "disgusted"))
disgusted_face_button.place(x=575, y=300)
disgusted_face_label = Label(text="Disgusted", font=theFont, background=background_color)
disgusted_face_label.place(x=585, y=420)

settings_icon = PhotoImage(file="vaaya_settings_icon.gif")
settings_button = Button(main_window, image=settings_icon, height=40, width=40, background="gray",
                         command=load_settings_window)
settings_button.place(x=25, y=535)

questions_icon = PhotoImage(file="vaaya_question.gif")
questions_button = Button(main_window, image=questions_icon, height=40, width=40, background="gray")
questions_button.place(x=635, y=535)

main_window.mainloop()


