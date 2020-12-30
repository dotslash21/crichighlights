import re
import requests
import time
from math import ceil
from typing import List, Generator


class CricHighlights:

    def __init__(self):
        pass

    @staticmethod
    def __crawl(url: str) -> dict:
        try:
            response = requests.get(url).json()
            return response
        except Exception:
            raise

    @staticmethod
    def __match_did_end(match_id: str) -> bool:
        """Method to check if the match has ended.

        Args:
            match_id (str): The ID of the match.

        Returns:
            bool: True if the match has ended, False otherwise.

       """

        url = 'http://mapps.cricbuzz.com/cbzios/match/' + match_id

        # fetch data from the endpoint.
        data = CricHighlights.__crawl(url)
        status = data.get('header').get('status')

        # Check the match status to determine match end
        regex = re.compile(r'\bwon\b | \blost\b | \bdraw\b', flags=re.I | re.X)
        matches = regex.findall(status)
        if matches:
            return True

        return False

    @staticmethod
    def __splice_highlight(highlights: dict, last_timestamp: int) -> List[dict]:
        """Method to splice out the latest highlights from a list of highlights.

        Args:
            highlights (dict): The highlights of the match.
            last_timestamp (int): The timestamp of the last received highlight.

        Yields:
            dict: The list of new highlight data.

       """

        low = 0
        high = len(highlights) - 1

        # Check if there has been new update.
        if int(highlights[low].get('timestamp')) == last_timestamp:
            return []

        # Perform binary search to find the number of new highlight updates.
        while low < high:
            mid = low + ceil((high - low) / 2.0)
            curr_timestamp = int(highlights[mid].get('timestamp'))

            if curr_timestamp > last_timestamp:
                low = mid
            else:
                high = mid - 1

        return highlights[:low + 1]

    @staticmethod
    def get_live_matches() -> List[dict]:
        """Method to fetch the current live match list.

        Returns:
            List[dict]: List of live match data.

        """

        # Endpoint for getting live matches.
        url = "http://mapps.cricbuzz.com/cbzios/match/livematches"

        # fetch data from the endpoint.
        data = CricHighlights.__crawl(url)

        # Extract the match data and return the relevant information
        matches = data['matches']
        result = []
        for match in matches:
            result.append({
                'match_id': match.get('match_id'),
                'series_id': match.get('series_id'),
                'series_name': match.get('series_name'),
                'match_desc': match.get('header').get('match_desc'),
                'status': match.get('header').get('status'),
                'type': match.get('header').get('type'),
                'team1': {
                    'name': match.get('team1').get('name'),
                    's_name': match.get('team1').get('s_name')
                },
                'team2': {
                    'name': match.get('team2').get('name'),
                    's_name': match.get('team2').get('s_name')
                }
            })
        return result

    @staticmethod
    def get_highlights(match_id: str) -> Generator[dict, None, None]:
        """Method to get match highlights.

        Args:
            match_id (str): The ID of the match.

        Yields:
            dict: The highlight data.

       """

        url = 'http://mapps.cricbuzz.com/cbzios/match/' + match_id + '/commentary'

        # Check if the match already ended.
        if CricHighlights.__match_did_end(match_id):
            # fetch data from the endpoint.
            data = CricHighlights.__crawl(url)
            highlights = data.get('comm_lines')

            # yield the highlights
            for highlight in reversed(highlights):
                yield highlight

            # Raise StopIteration
            return

        # Keep fetching highlights until match end.
        last_timestamp = 0  # Track the timestamp of the last received highlight.
        while not CricHighlights.__match_did_end(match_id):
            # fetch data from the endpoint.
            data = CricHighlights.__crawl(url)
            highlights = data.get('comm_lines')

            # Yield any new received highlight.
            new_highlights = CricHighlights.__splice_highlight(highlights, last_timestamp)
            for highlight in reversed(new_highlights):
                yield highlight

            # Update the last_timestamp.
            last_timestamp = int(highlights[0].get('timestamp'))

            # Wait for 10 seconds before fetching data again.
            time.sleep(10)
