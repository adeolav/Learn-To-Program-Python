# ---------- KIVY TUTORIAL PT 5  ----------

# ---------- kivytut.py  ----------

import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

# Used to display popup
class CustomPopup(Popup):
    pass

class SampBoxLayout(BoxLayout):

    # For checkbox
    checkbox_is_active = ObjectProperty(False)
    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

    # For radio buttons
    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    # For Switch
    def switch_on(self, instance, value):
        if value is True:
            print("Switch On")
        else:
            print("Switch Off")

    # Opens Popup when called
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

    # For Spinner
    def spinner_clicked(self, value):
        print("Spinner Value " + value)


class SampleApp(App):
    def build(self):

        # Set the background color for the window
        Window.clearcolor = (1, 1, 1, 1)
        return SampBoxLayout()

sample_app = SampleApp()
sample_app.run()

# ---------- sample.kv  ----------

#: import CheckBox kivy.uix.checkbox

<CustLabel@Label>:
    color: 0, 0, 0, 1

<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: "The Popup"
    Button:
        text: "Close"
        on_press: root.dismiss()

SampBoxLayout:

<SampBoxLayout>:
    orientation: "vertical"
    padding: 10
    spacing: 10

    # ---------- Holds CheckBox and RadioBox ----------
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .22
            CustLabel:
                text: "Are you over 18"
                size_hint_x: .80
            CheckBox:
                on_active: root.checkbox_18_clicked(self, self.active)
                size_hint_x: .20
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .55
            CustLabel:
                text: "Favorite Color"
                color: 0, 0, 0, 1
                size_hint_x: .265
            CheckBox:
                group: "fav_color"
                value: root.blue
                size_hint_x: .05
            CustLabel:
                text: "Blue"
                color: 0, 0, 0, 1
                size_hint_x: .15
            CheckBox:
                group: "fav_color"
                value: root.red
                size_hint_x: .05
            CustLabel:
                text: "Red"
                color: 0, 0, 0, 1
                size_hint_x: .15
            CheckBox:
                group: "fav_color"
                value: root.green
                size_hint_x: .05
            CustLabel:
                text: "Green"
                color: 0, 0, 0, 1
                size_hint_x: .15

    # ---------- Holds Slider & Switch ----------
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25
            CustLabel:
                text: str(slider_id.value)

            # Define the min, max, starting value and how
            # much the value changes with each move
            Slider:
                id: slider_id
                min: -100
                max: 100
                value: 0
                step: 1

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25
            CustLabel:
                text: "On / Off"

            Switch:
                id: switch_id
                on_active: root.switch_on(self, self.active)

    # ---------- Displays Popup & Spinner ----------
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            # When clicked the popup opens
            Button:
                text: "Open Popup"
                on_press: root.open_popup()

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            Spinner:
                text: "First"
                values: ["First", "Second", "Third"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)

    # ---------- Displays TabbedPanel ----------
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            TabbedPanel:
                do_default_tab: False

                TabbedPanelItem:
                    text: "1st Tab"
                    Label:
                        text: "Content of First Panel"
                TabbedPanelItem:
                    text: "2nd Tab"
                    Label:
                        text: "Content of Second Panel"
                TabbedPanelItem:
                    text: "3rd Tab"
                    Label:
                        text: "Content of Third Panel"

# ---------- kivytut2.py  ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# You can create your kv code in the Python file
Builder.load_string("""
<ScreenOne>:
    BoxLayout:
        Button:
            text: "Go to Screen 2"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'

<ScreenTwo>:
    BoxLayout:
        Button:
            text: "Go to Screen 1"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_one'
""")

# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    pass


# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))

class KivyTut2App(App):

    def build(self):
        return screen_manager

sample_app = KivyTut2App()
sample_app.run()
