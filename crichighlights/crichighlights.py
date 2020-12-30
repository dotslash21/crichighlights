from typing import List

import requests


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
