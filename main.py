import re
import requests

import secrets
from crichighlights import CricHighlights


def show_live_matches():
    matches = CricHighlights.get_live_matches()

    for match in matches:
        print(match.get('match_desc') + ' - ' + match.get('series_name') + ' (Match ID: ' + match.get('match_id') + ')')

    print()


def show_match_highlights():
    match_id = input("Enter the Match ID: ")

    if not CricHighlights.match_did_start(match_id):
        print('The match is yet to start!\n')
        return

    for highlight in CricHighlights.get_highlights(match_id):
        print(highlight.get('comm'))

    print()


def send_message_telegram(message):
    url = 'https://api.telegram.org/bot' + secrets.BOT_KEY + '/sendMessage'

    requests.post(url, data={"chat_id": secrets.CHAT_ID, "text": message})


def send_match_highlights():
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
        regex = re.compile(r'<.*?>')
        message = regex.sub('', message)

        # Send message to Telegram.
        send_message_telegram(message)

    print()


def show_menu():
    print('1) Show live matches')
    print('2) Show match highlights')
    print('3) Send match highlights')
    print('4) Exit')

    choice = int(input("Enter your choice: "))

    switcher = {
        1: show_live_matches,
        2: show_match_highlights,
        3: send_match_highlights,
        4: exit
    }

    function = switcher.get(choice, None)

    if function:
        try:
            print()
            function()
        except Exception as e:
            print(repr(e))


if __name__ == '__main__':
    while True:
        show_menu()
