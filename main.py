import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Airline Companies: "))
        self.airline_companies = TextInput(multiline=False)
        self.add_widget(self.airline_companies)

        self.add_widget(Label(text="Customers: "))
        self.customers = TextInput(multiline=False)
        self.add_widget(self.customers)

        self.add_widget(Label(text="Administrators: "))
        self.administrators = TextInput(multiline=False)
        self.add_widget(self.administrators)

        self.add_widget(Label(text="Flights Per Company: "))
        self.flights_per_company = TextInput(multiline=False)
        self.add_widget(self.flights_per_company)

        self.add_widget(Label(text="Tickets Per Customer: "))
        self.tickets_per_customer = TextInput(multiline=False)
        self.add_widget(self.tickets_per_customer)

        self.add_widget(Label(text="Countries: "))
        self.countries = TextInput(multiline=False)
        self.add_widget(self.countries)


class MyApp(App):
    def build(self):
       return MyGrid()


if __name__ == "__main__":
    MyApp().run()
