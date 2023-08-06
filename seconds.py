from kivy.clock import Clock
from kivy.uix.label import Label

class Seconds(Label):
    def __init__(self, total, callback, **kwargs):
        self.total = total
        self.current = 0
        self.callback = callback
        my_text = "Пройшло секунд: " + str(self.current)
        super().__init__(text=my_text)

    def restart(self, total, callback, **kwargs):
      self.done = False
      self.total = total
      self.current = 0
      self.callback = callback
      self.text = "Пройшло секунд: " + str(self.current)
      self.start()

    def start(self):
      Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current += 1
        self.text = "Пройшло секунд: " + str(self.current)
        if self.current >= self.total:
          self.callback()
          return False
