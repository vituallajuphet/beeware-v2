import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class test(toga.App):

    def startup(self):

        main_box = toga.Box()

        main_box2 = toga.Box()
        boxselection = toga.Box()
        box1 = toga.Box()
        box2 = toga.Box()
        box3 = toga.Box()
        box4 = toga.Box()
        box5 = toga.Box()
        box6 = toga.Box()

        main_box3 = toga.Box()
        box7 = toga.Box()

        # box selection

        Labelfirst = toga.Label("Select Convertion")
        def button_handler2(widget):
            main_box.remove(main_box2)
            # main_box.add(main_box3)
            # main_box.refresh()
            # main_box.refresh_sublayouts()
            # self.main_window.content = main_box
            

        buttonCurrency = toga.Button("Currency", on_press=button_handler2)

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

        button1 = toga.Button("Convert Units", on_press=button_handler)
        button1.style.padding_top = 10

        boxselection.add(Labelfirst)
        boxselection.add(buttonCurrency)
        

        box1.add(Label1)
        box2.add(self.input_text)
        box3.add(Label2)
        box4.add(self.input_text2)
        box5.add(button1)

        main_box2.add(boxselection)
        main_box2.add(box1)
        main_box2.add(box2)
        main_box2.add(box3)
        main_box2.add(box4)
        main_box2.add(box5)


        # new
        lbl1 = toga.Label("mainbox2")
        def button3_handler(widget):
            main_box.remove(main_box3)
            main_box.add(main_box2)
            main_box.refresh()
            main_box.refresh_sublayouts()
            self.main_window.content = main_box   
            
        button3 = toga.Button("Backed", on_press=button3_handler)

        box7.add(lbl1)
        box7.add(button3)
        main_box3.add(box7)
        
        main_box.add(main_box2)

        main_box.style.update(direction=COLUMN)
        main_box2.style.update(direction=COLUMN)
        main_box3.style.update(direction=COLUMN)

        self.main_window = toga.MainWindow(title="Unit Converter")
        self.new_window = toga.MainWindow(title="New Window")
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return test()
