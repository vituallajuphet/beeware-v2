"""
this is test
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class test(toga.App):

    def startup(self):


        

        box1 = toga.Box()
        box2 = toga.Box()
        box3 = toga.Box()
        box4 = toga.Box()
        box5 = toga.Box()
        box6 = toga.Box()

        main_box = toga.Box()

        Label1 = toga.Label("Unit 1")
        self.input_text = toga.TextInput()
        Label2 = toga.Label("Unit 2")
        self.input_text2 = toga.TextInput()
        self.input_text.style.width = 400
        self.input_text.style.padding_top = 10
        self.input_text2.style.width = 400
        self.input_text2.style.padding_top = 10

        Label3 = toga.Label("Result: ")
        box6.add(Label3)

        def button_handler(widget):
            Label3.text = "Result: {}!".format(input_text.value)

        button1 = toga.Button("Convert Unit", on_press=button_handler)
        button1.style.padding_top = 10

        box1.add(Label1)
        box2.add(self.input_text)
        box3.add(Label2)
        box4.add(self.input_text2)
        box5.add(button1)

        

        main_box.add(box1)
        main_box.add(box2)
        main_box.add(box3)
        main_box.add(box4)
        main_box.add(box5)

        main_box.style.update(direction=COLUMN)

        

        self.main_window = toga.MainWindow(title="Unit Converter")
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return test()
