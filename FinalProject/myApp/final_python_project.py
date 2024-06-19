# Make a Text-to-Speech program to read aloud some text as well as text from a URL

# Import modules
import turtle # to draw the screen and buttons
from gtts import gTTS # google translate, text to speech
import shutil # Moving the .mp3 file to another location
import os # to open the .mp3 file and see if the name already exists
from urllib.request import urlopen # Read the website and make it an HTML file
from bs4 import BeautifulSoup # Parses the HTML file after reading the website so that
                              # it can become a string
import psutil # Iterates over all running processes | To check if an application is running
from tkinter import messagebox # To display a warning


# Where all the mp3 files will be saved
# Can be changed to user satisfaction
mp3Path = "D:\Account"

# Clear the screen
os.system("cls")

pen = turtle.Turtle() # To draw the buttons and title
screen = turtle.Screen() # To make the input boxes

pen.speed(0)
screen.setup(650,450)
pen.hideturtle()

# Defining variables so that they can be used as variables AND parameters
button_x = 0
button_y = 0
button_width = 0
button_height = 0
text = ""
text_input = ""
url_input = ""

# Get the coordinates of a click
# Not going to be used in the code
def get_mouse_click_coor(x, y):
    coordinates = (x,y)
    coor = list(coordinates)
    print(coor)

# Creating and drawing the URL and Text and files button function
def draw_button(fill_color, button_x, button_y, button_width, button_height, text,textspot1,textspot2):
    pen.goto(button_x, button_y)
    pen.setheading(0)
    pen.pendown()
    pen.color(fill_color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(button_width)
        pen.circle(-15,90,100)
        pen.forward(button_height)
        pen.circle(-15,90,100)
    pen.end_fill()
    pen.penup()
    pen.goto(button_x+textspot1,button_y-textspot2)
    pen.color("white")
    pen.write(text, align = "center", font = ("Arial", 20, "normal"))

# Text Button Function
def text_function(text_input, language):
    # Type in anything
    text_message = text_input
    store_audio = gTTS(text=text_message, lang=language)
    save = screen.textinput("Save File Permission", "Would you like to save the audio file as an .mp3?")
    if save.lower() == "y" or save.lower() == "yes":
        name = screen.textinput("Naming File","What would you like to name the file? (.mp3 will be automatically included)")
        # If the file already exists
        if os.path.exists(f"{mp3Path}/{name}.mp3") == True:
            while os.path.exists(f"{mp3Path}/{name}.mp3") == True:
                name = screen.textinput("Naming File", "The file already exits. Please enter another name for the file: (.mp3 will be automatically included)")
            else:
                # If a file name that doesn't exist is entered
                store_audio.save(f"{name}.mp3")
        else:
            # If a file name that doesn't exist is entered
            store_audio.save(f"{name}.mp3")
        # to start the file from computer
        os.system(f"start {name}.mp3")
        shutil.move(f"{name}.mp3", f"{mp3Path}\{name}.mp3")
    else:
        store_audio.save("unsavedtextfile.mp3")
        os.system( "attrib +h unsavedtextfile.mp3" )
        os.system("start unsavedtextfile.mp3")
        is_open = "wmplayer.exe" in (i.name() for i in psutil.process_iter())
        while is_open == True:
            is_open = "wmplayer.exe" in (i.name() for i in psutil.process_iter())
        else:
            os.remove("unsavedtextfile.mp3")

# URL Button Function
def url_function(url_input, language):
    open_url = urlopen(url_input).read()
    parse = BeautifulSoup(open_url, features="html.parser")
    # Get the text
    real_text = parse.get_text()
    # Say the text
    store_audio = gTTS(text=real_text, lang=language)
    save = screen.textinput("Save File Permission", "Would you like to save the audio file as an .mp3?")
    if save.lower() == "y" or save.lower() == "yes":
        name = screen.textinput("Naming File","What would you like to name the file? (.mp3 will be automatically included)")
        # If the file already exists
        if os.path.exists(f"{mp3Path}\{name}.mp3") == True:
            while os.path.exists(f"{mp3Path}\{name}.mp3") == True:
                name = screen.textinput("Naming File", "The file already exits. Please enter another name for the file: (.mp3 will be automatically included)")
            else:
                store_audio.save(f"{name}.mp3")
        else:
            # If a file name that doesn't exist is entered
            store_audio.save(f"{name}.mp3")
        # to start the file from computer
        os.system(f"start {name}.mp3")
        shutil.move(f"{name}.mp3", f"{mp3Path}\{name}.mp3")

    else:
        store_audio.save("unsavedurlfile.mp3")
        os.system( "attrib +h unsavedurlfile.mp3" )
        os.system("start unsavedurlfile.mp3")
        is_open = "wmplayer.exe" in (i.name() for i in psutil.process_iter())
        while is_open == True:
            is_open = "wmplayer.exe" in (i.name() for i in psutil.process_iter())
        else:
            os.remove("unsavedurlfile.mp3")

# Files Button function
def files_function():
    os.startfile(mp3Path)

# What to do when the "Text", "URL", or "Files" button is clicked
def button_click_decider(x, y):
    # This checks if the "Text" button is clicked
    if -215 < x < -35:
        if -130 < y < -50:
            text_input = screen.textinput("Text Input", "Please enter the text you would like to hear aloud:")
            only_spaces = str(text_input).isspace() # If the input was only spaces
            if only_spaces == True or text_input == "": # If the input was only spaces or if nothing was entered
                messagebox.showinfo("Alert!", "Please enter a valid piece of text") # Give an error message
            else: # If the user entered something valid
                try:
                    text_function(text_input, "en")
                except (AssertionError, AttributeError):
                    os.system("cls") # Clear Screen
            
    # If the URL button was clicked
    if 35 < x < 216:
        if -130 < y < -50:
            url_input = screen.textinput("URL Link", "Please enter the URL for the article you would like to hear aloud:")
            # If the user pressed "OK" without entering anything
            # Or if the user pressed "Cancel"
            try:
                url_function(url_input, "en")
            except ValueError:
                os.system("cls")
                messagebox.showinfo("Alert!", "Please enter a valid URL")
            except AttributeError:
                os.system("cls")
    # If the Files button was clicked
    if -190 < x < 190:
        if 20 < y < 100:
            files_function()
    # If the exit button was clicked
    if -56 < x < 56:
        if -210 < y < -150:
            # Close the window
            screen.bye()

# Creating the title
pen.penup()
pen.color("Blue")
pen.goto(0,170)
pen.write("Text to Speech (TTS)", align = "center", font = ("Cambria", 30, "bold"))
# Show all saved .mp3 files button
draw_button("black", -175, 100, 350, 50, "Show all saved .mp3 files", 175, 55)
# Insert Text button
draw_button("black", -200, -50, 150, 50, "Insert Text", 75, 55)
# URL Button
draw_button("black", 50, -50, 150, 50, "URL", 75, 55)
# Exit Button
draw_button("red", -40, -150, 80, 30, "Exit", 40, 46)

# When the screen is clicked, it checks if it was on one of the buttons
# and does its function
screen.onscreenclick(button_click_decider)


# Keep the screen open
screen.mainloop()
