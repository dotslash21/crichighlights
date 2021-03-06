import re
import time
from math import ceil
from typing import List, Generator

import requests

MAX_NUM_HIGHLIGHTS = 20


class CricHighlights:

    def __init__(self):
        pass

    @staticmethod
    def __crawl(url: str) -> dict:
        """Method to fetch data from a given URL.

        Args:
            url (str): The URL to fetch data from.

        Returns:
            dict: The fetched JSON data as Python dict.

        Raises:
            Exception: Error occurred while fetching the data.

       """

        try:
            response = requests.get(url).json()
            return response
        except Exception as e:
            raise e

    @staticmethod
    def __splice_highlight(highlights: dict, last_timestamp: int) -> List[dict]:
        """Method to splice out the latest highlights from a list of highlights.

        Args:
            highlights (dict): The highlights of the match.
            last_timestamp (int): The timestamp of the last received highlight.

        Returns:
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

        # Check update count overflow
        count = low + 1
        if count > MAX_NUM_HIGHLIGHTS:
            count = MAX_NUM_HIGHLIGHTS

        return highlights[:count]

    @staticmethod
    def is_match_id_valid(match_id: str) -> bool:
        """Method to check if the match id is valid.

        Args:
            match_id (str): The ID of the match.

        Returns:
            bool: True if the match id is valid, False otherwise.

        Raises:
            Exception: Error occurred while fetching the data.

       """

        url = 'http://mapps.cricbuzz.com/cbzios/match/' + match_id

        try:
            # fetch data from the endpoint.
            data = CricHighlights.__crawl(url)

            # Perform check
            if match_id != data.get('match_id'):
                return False

            return True
        except Exception as e:
            raise e

    @staticmethod
    def match_did_end(match_id: str) -> bool:
        """Method to check if the match has ended.

        Args:
            match_id (str): The ID of the match.

        Returns:
            bool: True if the match has ended, False otherwise.

        Raises:
            Exception: Error occurred while fetching the data.

       """

        url = 'http://mapps.cricbuzz.com/cbzios/match/' + match_id

        try:
            # fetch data from the endpoint.
            data = CricHighlights.__crawl(url)
            status = data.get('header').get('status')

            # Check the match status to determine match end
            regex = re.compile(r'\bwon\b | \blost\b | \bdraw\b', flags=re.I | re.X)
            matches = regex.findall(status)
            if matches:
                return True

            return False
        except Exception as e:
            raise e

    @staticmethod
    def match_did_start(match_id: str) -> bool:
        """Method to check if the match has started.

        Args:
            match_id (str): The ID of the match.

        Returns:
            bool: True if the match has started, False otherwise.

        Raises:
            Exception: Error occurred while fetching the data.

       """

        url = 'http://mapps.cricbuzz.com/cbzios/match/' + match_id

        try:
            # fetch data from the endpoint.
            data = CricHighlights.__crawl(url)
            state = data.get('header').get('state')

            if state == 'preview':
                return False

            return True
        except Exception as e:
            raise e

    @staticmethod
    def get_live_matches() -> List[dict]:
        """Method to fetch the current live match list.

        Returns:
            List[dict]: List of live match data.

        Raises:
            Exception: Error occurred while fetching the data.

        """

        # Endpoint for getting live matches.
        url = "http://mapps.cricbuzz.com/cbzios/match/livematches"

        try:
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
        except Exception as e:
            raise e

    @staticmethod
    def get_highlights(match_id: str) -> Generator[dict, None, None]:
        """Method to get match highlights.

        Args:
            match_id (str): The ID of the match.

        Yields:
            dict: The highlight data.

        Raises:
            Exception: Error occurred while fetching the data.

       """

        url = 'http://mapps.cricbuzz.com/cbzios/match/' + match_id + '/commentary'

        try:
            # Stop if the provided match id is not valid
            if not CricHighlights.is_match_id_valid(match_id):
                return

            # Keep fetching highlights until match end.
            last_timestamp = 0  # Track the timestamp of the last received highlight.
            while not CricHighlights.match_did_end(match_id) or last_timestamp == 0:
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
        except Exception as e:
            raise e
