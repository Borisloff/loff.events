from parser import parser_dump, parser_load
from date import datenow, datesall
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.metrics import dp

class LoffEventsApp(MDApp):

    def build(self):
        self.root = Builder.load_file('interface.kv')

        for date, writing in datesall().items():
            
            card = MDCard(
                    radius = dp(40),
                    style = 'outlined',
                    height = dp(100),
                    padding = dp(20),
                    size_hint_x = None, 
                    width = dp(150),
                    on_release = lambda x, d=date: self.date_selection(d)
                    )
            
            card.add_widget(
                MDLabel(
                    text=writing
                )
            )

            self.root.ids['dates_card'].add_widget(card)

            print(date)

        return self.root

    def date_selection(self, date):

        print(parser_load()[date])

        try:

            self.root.ids['events'].clear_widgets()

            for i in parser_load()[date]:
                
                card = MDCard(
                        radius = dp(40),
                        style = 'outlined',
                        height = dp(100),
                        padding = dp(20),
                        size_hint_x = None, 
                        width = dp(150),
                        on_release = lambda x, event=i: self.event_selection(event)
                        )

                card.add_widget(
                    MDLabel(
                        text=i['name']
                    )
                )
                self.root.ids['events'].add_widget(card)

        except:
            print('error')

LoffEventsApp().run()