from crichighlights import CricHighlights
from demo.services.notification import notification_factory
from demo.utils import htmltagremover


class Demo:
    @staticmethod
    def __show_live_matches():
        matches = CricHighlights.get_live_matches()

        for match in matches:
            print(match.get('match_desc') + ' - ' + match.get('series_name') + ' (Match ID: ' + match.get(
                'match_id') + ')')

        print()

    @staticmethod
    def __show_match_highlights():
        match_id = input("Enter the Match ID: ")

        if not CricHighlights.match_did_start(match_id):
            print('The match is yet to start!\n')
            return

        for highlight in CricHighlights.get_highlights(match_id):
            print(highlight.get('comm'))

        print()

    @staticmethod
    def __send_match_highlights():
        match_id = input("Enter the Match ID: ")

        if not CricHighlights.match_did_start(match_id):
            print('The match is yet to start!\n')
            return

        for highlight in CricHighlights.get_highlights(match_id):
            print(highlight.get('comm'))

            message = highlight.get('comm')

            # Skip if message is None.
            if message is None:
                continue

            # Remove HTML tag.
            htmltagremover.remove(message)

            # Send message to Telegram.
            notification_service = notification_factory.get_notification_service()
            notification_service.send(message)

        print()

    @staticmethod
    def __show_menu():
        print('1) Show live matches')
        print('2) Show match highlights')
        print('3) Send match highlights')
        print('4) Exit')

        choice = int(input("Enter your choice: "))

        switcher = {
            1: Demo.__show_live_matches,
            2: Demo.__show_match_highlights,
            3: Demo.__send_match_highlights,
            4: exit
        }

        function = switcher.get(choice, None)

        if function:
            try:
                print()
                function()
            except Exception as e:
                print(repr(e))

    @staticmethod
    def run():
        while True:
            Demo.__show_menu()
