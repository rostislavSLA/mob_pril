from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


Builder.load_string("""
<Demo>:
    cols: 10
""")


class CustomButton(Button):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(f"\nCustomButton.on_touch_down: text={self.text}")
            self.parent.remove_widget(self)    # remove a widget / button
            # self.parent.clear_widgets()    # remove all children / buttons
            return True    # consumed on_touch_down & stop propagation / bubbling
        return super(CustomButton, self).on_touch_down(touch)


class Demo(GridLayout):

    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        self.create_buttons()

    def create_buttons(self):
        for i in range(100):
            self.add_widget(CustomButton(id="Button" + str(i), text="Button"+str(i)))


class TestApp(App):

    def build(self):
        return Demo()


if __name__ == "__main__":
    TestApp().run()