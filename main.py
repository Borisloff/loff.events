from parser import parser_load
from date import datenow, datesall, yearnow
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivymd.uix.navigationbar import MDNavigationItem
from kivy.properties import StringProperty

class BaseMDNavigationItem(MDNavigationItem):

    icon = StringProperty()
    text = StringProperty()

class LoffEventsApp(MDApp):

# ========== Общее ==========

    def build(self):
        self.root = Builder.load_file('interface.kv')
        self.theme_cls.theme_style = 'Dark'

        events_all = parser_load()
        dates = datesall()

        if events_all != 'error':

# ========== Сегодня ==========

            if dates[0] in events_all:

                for event in events_all[dates[0]]:
                    if event['type'] == 'holiday':
                        self.root.ids['card_today'].add_widget(
                            MDLabel(
                                text = event['name'],
                                size_hint_y = None,
                                height = dp(40)
                            )
                        )
                    else:
                        self.root.ids['card_today'].add_widget(
                            MDLabel(
                                text=f'{event["name"]} ({str(yearnow() - int(event["year"]))} {event['writing']})',
                                size_hint_y=None,
                                height=dp(40)
                            )
                        )

            else:
                self.root.ids['card_today'].add_widget(
                    MDLabel(
                        text = 'Нет событий',
                        size_hint_y = None,
                        height = dp(40)
                    )
                )


# ========== Завтра ==========

            if dates[1] in events_all:

                for event in events_all[dates[1]]:
                    if event['type'] == 'holiday':
                        self.root.ids['card_tomorrow'].add_widget(
                            MDLabel(
                                text=event['name'],
                                size_hint_y=None,
                                height=dp(40)
                            )
                        )
                    else:
                        self.root.ids['card_tomorrow'].add_widget(
                            MDLabel(
                                text=f'{event["name"]} ({str(yearnow() - int(event["year"]))} {event['writing']})',
                                size_hint_y=None,
                                height=dp(40)
                            )
                        )

            else:
                self.root.ids['card_tomorrow'].add_widget(
                    MDLabel(
                        text='Нет событий',
                        size_hint_y=None,
                        height=dp(40)
                    )
                )

# ========== Вчера ==========

            if dates[2] in events_all:

                for event in events_all[dates[2]]:
                    if event['type'] == 'holiday':
                        self.root.ids['card_yesterday'].add_widget(
                            MDLabel(
                                text=event['name'],
                                size_hint_y=None,
                                height=dp(40)
                            )
                        )
                    else:
                        self.root.ids['card_yesterday'].add_widget(
                            MDLabel(
                                text=f'{event["name"]} ({str(yearnow() - int(event["year"]))} {event['writing']})',
                                size_hint_y=None,
                                height=dp(40)
                            )
                        )

            else:
                self.root.ids['card_yesterday'].add_widget(
                    MDLabel(
                        text='Нет событий',
                        size_hint_y=None,
                        height=dp(40)
                    )
                )

# ========== Через неделю ==========

            if dates[3] in events_all:

                for event in events_all[dates[3]]:
                    if event['type'] == 'holiday':
                        self.root.ids['card_week_later'].add_widget(
                            MDLabel(
                                text=event['name'],
                                size_hint_y=None,
                                height=dp(40)
                            )
                        )
                    else:
                        self.root.ids['card_week_later'].add_widget(
                            MDLabel(
                                text=f'{event["name"]} ({str(yearnow() - int(event["year"]))} {event['writing']})',
                                size_hint_y=None,
                                height=dp(40)
                            )
                        )

            else:
                self.root.ids['card_week_later'].add_widget(
                    MDLabel(
                        text='Нет событий',
                        size_hint_y=None,
                        height=dp(40)
                    )
                )

        if events_all == 'error':

            self.root.clear_widgets()

            self.root.add_widget(
                MDLabel(
                    text = '''
Файл событий заполнен неправильно.
Он находиться в папке "Лофф.События" корневого расположения и называется "events.txt"

Формат списка:

* Строки, начинающиеся со знака «*»,
* являются служебными
07.01.1963 АБИШЕВ Тимур Кенесович
07.01.1775 ДУХОВАНИЧ Василий Иванович
08.01.1975 КАЛАБУХОВ Дмитрий Николаевич
08.01 День рыбака

Возможно два типа дат: дни рождения и дни праздников.

Формат дня рождения: 
07.01.1963 АБИШЕВ Тимур Кенесович
Формат праздника:
08.01 День рыбака
                    ''',
                    size_hint_y = None,
                    adaptive_height = True,
                    padding = dp(20)
                )
            )




        return self.root

LoffEventsApp().run()