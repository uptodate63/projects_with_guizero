# Imports
from unicodedata import name
from guizero import App, Text, Picture, PushButton
from random import choice


# Functions
def choose_name():
    # print("Button was pressed")
    first_names = ["Barbara", "Woody", "Tiberius"]
    last_names = ["Dugeon", "Darkmeyer", "Smith"]
    wanted_name = choice(first_names) + " " + choice(last_names)
    name.value = wanted_name


# App
app = App("Wanted!")
app.bg = (251, 251, 208)

# Widgets
wanted_text = Text(app, text="Wanted!")
wanted_text.text_size = 50
wanted_text.font = "Courier"

title = Text(app, "Push the button to declare who is wanted!")

button = PushButton(app, choose_name, text="Tell me!")
button.bg = "red"
button.text_size = 30
name = Text(app, text="")


picture = Picture(app, image="image.jpg")
picture.resize(350, 380)
# picture.align = "bottom"

# Display
app.display()
