# ---------- KIVY TUTORIAL PT 4  ----------

# In this part of my Kivy tutorial I'll show how to use
# the ListView, ListAdapter and how to create a toolbar

# ---------- studentdb.py  ----------

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class StudentListButton(ListItemButton):
    pass


class StudentDB(BoxLayout):

    # Connects the value in the TextInput widget to these
    # fields
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_student(self):

        # Get the student name from the TextInputs
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

        # Add the student to the ListView
        self.student_list.adapter.data.extend([student_name])

        # Reset the ListView
        self.student_list._trigger_reset_populate()

    def delete_student(self, *args):

        # If a list item is selected
        if self.student_list.adapter.selection:

            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text

            # Remove the matching item
            self.student_list.adapter.data.remove(selection)

            # Reset the ListView
            self.student_list._trigger_reset_populate()

    def replace_student(self, *args):

        # If a list item is selected
        if self.student_list.adapter.selection:

            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text

            # Remove the matching item
            self.student_list.adapter.data.remove(selection)

            # Get the student name from the TextInputs
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

            # Add the updated data to the list
            self.student_list.adapter.data.extend([student_name])

            # Reset the ListView
            self.student_list._trigger_reset_populate()


class StudentDBApp(App):
    def build(self):
        return StudentDB()


dbApp = StudentDBApp()

dbApp.run()

# ---------- studentdb.kv  ----------

# Reference studentdb.py
#: import main studentdb
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

StudentDB:

<StudentDB>:
    orientation: "vertical"
    first_name_text_input: first_name
    last_name_text_input: last_name
    student_list: students_list_view
    padding: 10
    spacing: 10

    BoxLayout:
        size_hint_y: None
        height: "40dp"

        Label:
            text: "First Name"
        TextInput:
            id: first_name
        Label:
            text: "Last Name"
        TextInput:
            id: last_name

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Button:
            text: "Submit"
            size_hint_x: 15
            on_press: root.submit_student()
        Button:
            text: "Delete"
            size_hint_x: 15
            on_press: root.delete_student()
        Button:
            text: "Replace"
            size_hint_x: 15
            on_press: root.replace_student()

    # Define starting data and point to the ListItemButton
    # in the Python code
    ListView:
        id: students_list_view
        adapter:
            ListAdapter(data=["Doug Smith"], cls=main.StudentListButton)

# ---------- kivytut.py  ----------

import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class SampGridLayout(GridLayout):
    pass

class SampleApp(App):

    def build(self):
        return SampGridLayout()

sample_app = SampleApp()
sample_app.run()

# ---------- sample.kv  ----------

<SampGridLayout>:
    rows: 2

    BoxLayout:
        size_hint_y: None
        height: 30
        spacing: 10

        # Make the background for the toolbar white
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Button:
            background_normal: 'open.png'
            background_down: 'open_dn.png'
            size_hint_x: None
            width: 30
        Button:
            background_normal: 'disk.png'
            background_down: 'disk_dn.png'
            size_hint_x: None
            width: 30
        Button:
            background_normal: 'exit.png'
            background_down: 'exit_dn.png'
            size_hint_x: None
            width: 30
