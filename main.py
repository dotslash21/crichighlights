from crichighlights import CricHighlights


def show_live_matches():
    matches = CricHighlights.get_live_matches()

    for match in matches:
        print(match.get('match_desc') + ' - ' + match.get('series_name') + ' (Match ID: ' + match.get('match_id') + ')')

    print()


def show_match_highlights():
    match_id = input("Enter the Match ID: ")

    for highlight in CricHighlights.get_highlights(match_id):
        print(highlight.get('comm'))

    print()


def show_menu():
    print('1) Show live matches')
    print('2) Show match highlights')
    print('3) Exit')

    choice = int(input("Enter your choice: "))

    switcher = {
        1: show_live_matches,
        2: show_match_highlights,
        3: exit
    }

    function = switcher.get(choice, None)

    if function:
        print()
        function()


if __name__ == '__main__':
    while True:
        show_menu()
