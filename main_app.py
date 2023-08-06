from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from instructions import *
from ruffier import *
from seconds import *

name = ''

P1 = 0
P2 = 0
P3 = 0
age = 0

class FirstScreen(Screen):
    def __init__(self, name='first'):
        super().__init__(name='first')
        instruction = Label(text = txt_instruction, font_size = "15sp")
        name_label = Label(text = "Введіть ім'я:")
        age_label = Label(text = "Введіть вік:")
        self.name_input = TextInput(text = " ")
        self.age_input = TextInput(text = " ")
        button_start = Button(text = "Почати")

        main_layout = BoxLayout(orientation = "vertical", padding = 30)
        inputing_info = BoxLayout(orientation = "horizontal")
        labels_layout = BoxLayout(orientation = "vertical", size_hint=(None, 0.3), width="400", pos_hint={"x" : 0.1, "y": 0})
        inputs_layout = BoxLayout(orientation = "vertical", size_hint=(None, 0.3), width="500", pos_hint={"x" : 0.25, "y": 0}, spacing = 10)
        button = BoxLayout(orientation = "vertical", size_hint=(None, 0.8), width="600", pos_hint={"x" : 0.2, "y": 0.5}, padding = 50)

        main_layout.add_widget(instruction)
        labels_layout.add_widget(name_label)
        labels_layout.add_widget(age_label)
        inputs_layout.add_widget(self.name_input)
        inputs_layout.add_widget(self.age_input)
        button.add_widget(button_start)

        inputing_info.add_widget(labels_layout)
        inputing_info.add_widget(inputs_layout)

        main_layout.add_widget(inputing_info)
        main_layout.add_widget(button)

        button_start.on_press = self.next2

        self.add_widget(main_layout)

    def next2(self):
        if self.name_input.text.strip() and self.age_input.text.strip():
            global name, age
            name = self.name_input.text.strip()
            age = int(self.age_input.text)
            self.manager.transition.direction = 'left'
            self.manager.current = 'second'
        else:
            return

class SecondScreen(Screen):
    def __init__(self, name='second'):
        super().__init__(name='second')
        instruction2 = Label(text=txt_test1)
        result_label = Label(text="Введіть результат:")
        self.result_input = TextInput(text=" ")
        self.result_input.disabled = True
        self.button_continue = Button(text="Почати")
        self.timer = Seconds(total=5, callback=self.timer_complete)

        main_layout = BoxLayout(orientation = "vertical")
        inputing_info = BoxLayout(orientation = "horizontal", size_hint=(None, 0.1), width="900", pos_hint={"x" : 0, "y": 0})
        button = BoxLayout(orientation = "horizontal", size_hint=(None, 0.5), width="600", pos_hint={"x" : 0.2, "y": 0.5}, padding = 50)

        main_layout.add_widget(instruction2)
        inputing_info.add_widget(result_label)
        inputing_info.add_widget(self.result_input)
        button.add_widget(self.timer)
        button.add_widget(self.button_continue)

        main_layout.add_widget(inputing_info)
        main_layout.add_widget(button)

        self.button_continue.on_press = self.start_timer

        self.add_widget(main_layout)

    def start_timer(self):
        if self.button_continue.text == "Почати":
            self.result_input.disabled = True
            self.button_continue.text = "Йде час"
            self.button_continue.disabled = True
            self.timer.start()

    def timer_complete(self):
        self.result_input.disabled = False
        self.button_continue.text = "Продовжити"
        self.button_continue.disabled = False
        self.button_continue.on_press = self.next3

    def next3(self):
        if self.result_input.text.strip():
            global P1
            P1 = int(self.result_input.text)
            self.manager.transition.direction = 'left'
            self.manager.current = 'third'
        else:
            return

class ThirdScreen(Screen):
    def __init__(self, name='third'):
        super().__init__(name='third')
        instruction2 = Label(text = txt_sits)
        self.button_continue = Button(text = "Почати")
        self.timer = Seconds(total=5, callback=self.timer_complete)

        main_layout = BoxLayout(orientation = "vertical")
        text_layout = BoxLayout(orientation = "vertical", size_hint=(None, 0.8), width="600", pos_hint={"x" : 0.2, "y": 0})
        button_layout = BoxLayout(orientation = "vertical", size_hint=(None, 0.4), width="600", pos_hint={"x" : 0.2, "y": 0.5}, padding = 50)

        text_layout.add_widget(instruction2)
        text_layout.add_widget(self.timer)
        button_layout.add_widget(self.button_continue)

        main_layout.add_widget(text_layout)
        main_layout.add_widget(button_layout)

        self.button_continue.on_press = self.start_timer

        self.add_widget(main_layout)

    def start_timer(self):
        if self.button_continue.text == "Почати":
            self.button_continue.text = "Йде час"
            self.button_continue.disabled = True
            self.timer.start()

    def timer_complete(self):
        self.button_continue.text = "Продовжити"
        self.button_continue.disabled = False
        self.button_continue.on_press = self.next4

    def next4(self):
        global name
        self.manager.transition.direction = 'left' 
        self.manager.current = 'forth'

class ForthScreen(Screen):
    def __init__(self, name='forth'):
        super().__init__(name='forth')
        instruction = Label(text = txt_test3)
        result_before_label = Label(text = "Результат:")
        result_after_label = Label(text = "Результат після відпочинку:")
        self.what_to_do = Label(text = " ")
        self.result_before_input = TextInput(text = " ")
        self.result_after_input = TextInput(text = " ")
        self.result_before_input.disabled = True
        self.result_after_input.disabled = True
        self.button_end = Button(text = "Почати")
        self.timer = Seconds(total=5, callback=self.timer_middle)

        main_layout = BoxLayout(orientation = "vertical")
        information_giving = BoxLayout(orientation = "horizontal", padding = 30)
        timer_info = BoxLayout(orientation = "horizontal", padding = 10)
        inputing_info = BoxLayout(orientation = "horizontal")
        labels_layout = BoxLayout(orientation = "vertical", size_hint=(None, 0.3), width="400", pos_hint={"x" : 0.1, "y": 0})
        inputs_layout = BoxLayout(orientation = "vertical", size_hint=(None, 0.3), width="500", pos_hint={"x" : 0.25, "y": 0}, spacing = 10)
        button = BoxLayout(orientation = "vertical", size_hint=(None, 0.8), width="600", pos_hint={"x" : 0.2, "y": 0.5}, padding = 50)

        information_giving.add_widget(instruction)
        timer_info.add_widget(self.what_to_do)
        timer_info.add_widget(self.timer)
        labels_layout.add_widget(result_before_label)
        labels_layout.add_widget(result_after_label)
        inputs_layout.add_widget(self.result_before_input)
        inputs_layout.add_widget(self.result_after_input)
        button.add_widget(self.button_end)

        inputing_info.add_widget(labels_layout)
        inputing_info.add_widget(inputs_layout)

        main_layout.add_widget(information_giving)
        main_layout.add_widget(timer_info)
        main_layout.add_widget(inputing_info)
        main_layout.add_widget(button)

        self.button_end.on_press = self.start_timer

        self.add_widget(main_layout)

    def start_timer(self):
        if self.button_end.text == "Почати":
            self.what_to_do.text = "Міряйте пульс"
            self.button_end.text = "Йде час"
            self.button_end.disabled = True
            self.result_before_input.disabled = True
            self.result_after_input.disabled = True
            self.timer.start()

    def timer_middle(self):
        if self.button_end.text == "Йде час":
            self.what_to_do.text = "Впишіть перший результат"
            self.button_end.text = "Чекайте 30 секунд"
            self.result_before_input.disabled = False
            self.timer.restart(total=10, callback=self.timer_last_middle)

    def timer_last_middle(self):
        if self.button_end.text == "Чекайте 30 секунд":
            self.what_to_do.text = "Міряйте пульс"
            self.button_end.text = "Йде час"
            self.timer.restart(total=5, callback=self.timer_complete)

    def timer_complete(self):
        self.button_end.text = "Продовжити"
        self.what_to_do.text = "Впишіть другий результат"
        self.result_after_input.disabled = False
        self.button_end.disabled = False
        self.button_end.on_press = self.next_end

    def next_end(self):
        if self.result_before_input.text.strip() and self.result_after_input.text.strip():
            global P2, P3
            P2 = int(self.result_before_input.text)
            P3 = int(self.result_after_input.text)
            self.manager.transition.direction = 'left'
            self.manager.current = 'final'
        else:
            return

class FinalScreen(Screen):
    def __init__(self, name='final'):
        super().__init__(name='final')
        self.result_label = Label(text="", font_size = "15sp")

        main_layout = BoxLayout(orientation='vertical', padding=370, spacing=25)

        main_layout.add_widget(self.result_label)

        self.on_enter = self.before

        self.add_widget(main_layout)

    def before(self):
        global name, P1, P2, P3, age
        result_text = test(name, P1, P2, P3, age)

        self.result_label.text = str(result_text)

class Application(App):
    def build(self):
        sm = ScreenManager()
        m = FirstScreen()
        sm.add_widget(m)
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(ForthScreen())
        sm.add_widget(FinalScreen())
        return sm

app = Application()
app.run()