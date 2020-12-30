from crichighlights import CricHighlights


if __name__ == '__main__':
    # Create instance
    ch = CricHighlights()

    # Fetch live match data
    print(ch.get_live_matches())
