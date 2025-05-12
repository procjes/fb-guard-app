# main.py
from kivy.app import App
from kivy.uix.label import Label
import guard

class FBGuardApp(App):
    def build(self):
        # Execute CLI workflow immediately
        guard.main()
        return Label(text='✅ Operation complete. See logs.')

if __name__ == '__main__':
    FBGuardApp().run()
  
