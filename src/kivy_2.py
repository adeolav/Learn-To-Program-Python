# ---------- KIVYTUT.PY ----------

# It is common practice to create your own custom
# widgets so base widgets aren't effected

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.widget import Widget

class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()

customWidget = CustomWidgetApp()

customWidget.run()

# ---------- CUSTOMWIDGET.KV ----------

# You can set default attributes that are shared by
# other widgets

# color is RGBA as a percent of 255 and alpha
# Color is the text color
# background_normal and background_down are either
# white with '' or can be set to a png
# background_color tints whatever the background is

<CustButton@Button>:
    font_size: 32
    color: 0, 0, 0, 1
    size: 150, 50
    background_normal: ''
    background_down: 'bkgrd-down-color.png'
    background_color: .88, .88, .88, 1

# Position is x and y from the bottom left hand corner
# You can define the position based on the changing
# window sizes with root.x being the left most side
# and root.y being the bottom
<CustomWidget>:
    CustButton:
        text: "Random"
        pos: root.x, 200
    CustButton:
        text: "Buttons"
        pos: 200, root.y
    CustButton:
        text: "Buttons"
        pos: 200, 400

# ---------- KIVYTUT2.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# A Float layout positions and sizes objects as a percentage
# of the window size

class FloatingApp(App):

    def build(self):
        return FloatLayout()

flApp = FloatingApp()

flApp.run()

# ---------- FLOATING.KV ----------

# size_hint defines the widget width (0-1) representing
# a percentage of 100% and height of the window
<CustButton@Button>:
    font_size: 32
    color: 0, 0, 0, 1
    size: 150, 50
    background_normal: ''
    background_down: 'bkgrd-down-color.png'
    background_color: .88, .88, .88, 1
    size_hint: .4, .3

# pos_hint represents the position using either x, y, left,
# right, top, bottom, center_x, or center_y
<FloatLayout>:
    CustButton:
        text: "Top Left"
        pos_hint: {"x": 0, "top": 1}
    CustButton:
        text: "Bottom Right"
        pos_hint: {"right": 1, "y": 0}
    CustButton:
        text: "Top Right"
        pos_hint: {"right": 1, "top": 1}
    CustButton:
        text: "Bottom Left"
        pos_hint: {"left": 1, "bottom": 0}
    CustButton:
        text: "Center"
        pos_hint: {"center_x": .5, "center_y": .5}


# ---------- KIVYTUT3.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

# The Grid Layout organizes everything in a grid pattern

class GridLayoutApp(App):

    def build(self):
        return GridLayout()

glApp = GridLayoutApp()

glApp.run()

# ---------- GRIDLAYOUT.KV ----------

# Define the number of columns and rows
# Define the spacing between children in pixels

<GridLayout>:
    cols: 2
    rows: 2
    spacing: 10

    # Set the size by passing None to size_hint_x
    # and then pass the width

    Button:
        text: "1st"
        size_hint_x: None
        width: 200
    Button:
        text: "2nd"
    Button:
        text: "3rd"
        size_hint_x: None
        width: 200
    Button:
        text: "4th"

# ---------- KIVYTUT4.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# With a box layout we arrange widgets in a horizontal
# or vertical box

class BoxLayoutApp(App):

    def build(self):
        return BoxLayout()

blApp = BoxLayoutApp()

blApp.run()

# ---------- BOXLAYOUT.KV ----------

# Orientation defines whether widgets are stacked (vertical)
# or are placed side by side (horizontal)
# padding is the space between the widgets and the
# surrounding window
<BoxLayout>:
    orientation: "vertical"
    spacing: 10
    padding: 10

    # size_hint defines the percentage of space taken on the
    # x access and the percentage of space left over by the
    # other widgets
    Button:
        text: "1st"
        size_hint: .7, .5

    Button:
        text: "2nd"

    Button:
        text: "3rd"

# ---------- KIVYTUT5.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.stacklayout import StackLayout

# A stack layout arranges widgets vertically or horizontally
# as they best fit

class StackLayoutApp(App):

    def build(self):
        return StackLayout()

slApp = StackLayoutApp()

slApp.run()

# ---------- STACKLAYOUT.KV ----------

# orientation is lr-tb or left to right, top to bottom
# Other options are tb-lr, rl-tb, tb-rl, lr-bt, bt-lr,
# rl-bt, bt-rl
<StackLayout>:
    orientation: "lr-tb"
    spacing: 10
    padding: 10

    # size_hint defines the percentage of space taken on the
    # x access and the percentage of space left over by the
    # other widgets
    Button:
        text: "Q"
        size_hint: None, .15
        width: 100
    Button:
        text: "W"
        size_hint: None, .15
        width: 120
    Button:
        text: "E"
        size_hint: None, .15
        width: 140
    Button:
        text: "R"
        size_hint: None, .15
        width: 160
    Button:
        text: "T"
        size_hint: None, .15
        width: 180
    Button:
        text: "Y"
        size_hint: None, .15
        width: 200

# ---------- KIVYTUT6.PY ----------

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.pagelayout import PageLayout

# A page layout is used to create multi-page layouts
# that you can flip through

class PageLayoutApp(App):

    def build(self):
        return PageLayout()

plApp = PageLayoutApp()

plApp.run()

# ---------- PAGELAYOUT.KV ----------

<PageLayout>:
    Button:
        text: "Page 1"
    Button:
        text: "Page 2"
    Button:
        text: "Page 3"
