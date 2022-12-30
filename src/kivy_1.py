# ---------- Install Kivy on Mac ----------

1. Install Python and PyCharm like I show here : https://youtu.be/nwjAHQERL08?t=37m

2. Download Kivy for Python 3 Kivy-1.9.1-osx-python3.7z here : https://kivy.org/#download

3. In terminal : cd <Directory you Downloaded Kivy>

4. In terminal : sudo mv Kivy2.app /Applications/Kivy.app

5. In terminal : ln -s /Applications/Kivy.app/Contents/Resources/script /usr/local/bin/kivy

6. Test it works in terminal type : kivy and then import kivy

7. Run application by typing in terminal : kivy yourapp.py

# ---------- Install Kivy on Windows ----------

1. Install Python and PyCharm like I show here : https://youtu.be/nwjAHQERL08?t=37m

2. In command prompt : python -m pip install --upgrade pip wheel setuptools

3. In command prompt : python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

4. In command prompt : python -m pip install kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/

5. In command prompt : python -m pip install kivy

# ---------- kivytut.py ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label

# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class HelloKivy(App):

    # This returns the content we want in the window
    def build(self):

        # Return a label widget with Hello Kivy
        return Label(text="Hello Kivy")

helloKivy = HelloKivy()
helloKivy.run()

# ---------- kivytut2.py ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label

# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class HelloKivyApp(App):

    # This returns the content we want in the window
    def build(self):

        # Return a label widget with Hello Kivy
        # The name of the kv file has to be hellokivy
        # minus the app part from this class to
        # match up properly
        return Label()

hello_kivy = HelloKivyApp()
hello_kivy.run()

# ---------- hellokivy.kv ----------

# We can separate the logic from the presentation layer
<Label>:
    text: "Hello Kivy"
