from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class TopBarSubMenu(BoxLayout):
    def __init__(self, title, **kwargs):
        super(TopBarSubMenu, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50

        # Back button
        self.back_button = Button(text="< Back", size_hint_x=None, width=100)
        self.add_widget(self.back_button)

        # Title in the middle
        self.title_label = Label(text=title)
        self.add_widget(self.title_label)

        # Settings and Help buttons on the right
        self.settings_button = Button(text="Settings", size_hint_x=None, width=100)
        self.add_widget(self.settings_button)

        self.help_button = Button(text="Help", width=100)
        self.add_widget(self.help_button)


class TopBarMenu(BoxLayout):
    def __init__(self, title,**kwargs):
        super(TopBarMenu, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50

        # Title in the middle
        self.title_label = Label(text=title)
        self.add_widget(self.title_label)

        # Settings and Help buttons on the right
        self.settings_button = Button(text="Settings", size_hint_x=None, width=100)
        self.add_widget(self.settings_button)
