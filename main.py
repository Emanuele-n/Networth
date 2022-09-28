from kivy.app import App
from kivymd.app import MDApp
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3


class OpeningScreen(Screen):

    def on_plus(self):
        # open window for input
        # Create database
        conn = sqlite3.connect('first_db.db')

        # Crate a cursor
        c = conn.cursor()

        # Add a record
        c.execute("INSERT INTO customers VALUES(:first)",
                  {
                      'first': self.root.ids.word_input.text
                  })

        # Clear input box
        self.root.ids.word_input.text = ''
        print('here')

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Plus clicked")
        pass

    def on_minus(self):
        print("Minus clicked")

    pass


class NetWorthScreen(Screen):
    pass


class MonthlyBalanceScreen(Screen):
    pass


class WindowManager(ScreenManager):
    def submit(self):
        # Create database
        conn = sqlite3.connect('first_db.db')

        # Crate a cursor
        c = conn.cursor()

        # Add a record
        c.execute("INSERT INTO customers VALUES(:first)",
                  {
                      'first': self.root.ids.word_input.text
                  })

        # Clear input box
        self.root.ids.word_input.text = ''

        # Commit changes and close connection
        conn.commit()
        conn.close()
    pass


class NetWorth(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(OpeningScreen(name='open'))
        sm.add_widget(NetWorthScreen(name='networth'))
        sm.add_widget(NetWorthScreen(name='month'))

        # Create/connect database
        conn = sqlite3.connect('first_db.db')

        # Create a cursor
        c = conn.cursor()

        # Create a table
        c.execute("CREATE TABLE if not exists customers(name text, last_name text)")
        # Commit changes and close connection
        conn.commit()
        conn.close()
        return sm

    def show_records(self):
        # Create database
        conn = sqlite3.connect('first_db.db')

        # Crate a cursor
        c = conn.cursor()

        # Add a record
        c.execute("SELECT * FROM customers ")
        records = c.fetchall()

        word = ''

        # Loop through records
        for record in records:
            word = f'{word}\n{record}'
            self.root.ids.word_label.text = f'{word}'

        # Commit changes and close connection
        conn.commit()
        conn.close()
        pass

    pass


NetWorth().run()
