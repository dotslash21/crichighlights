# CricHighlights

Python library for getting real-time ball-by-ball updates of a live cricket match.

## Usage

### is_match_id_valid(match_id: str)
CODE:
```python
from crichighlights import CricHighlights

print(CricHighlights.is_match_id_valid('30555'))
print(CricHighlights.is_match_id_valid('0'))
```
OUTPUT:
```text
True
False
```
  
### match_did_end(match_id: str)
CODE:
```python
from crichighlights import CricHighlights

print(CricHighlights.match_did_end('30555'))
```
OUTPUT:
```text
True
```
  
### match_did_start(match_id: str)
CODE:
```python
from crichighlights import CricHighlights

print(CricHighlights.match_did_start('30555'))
```
OUTPUT:
```text
True
```
  
### get_live_matches()
CODE:
```python
from crichighlights import CricHighlights

print(CricHighlights.get_live_matches())
```
OUTPUT:
```text
[{'match_id': '30555', 'series_id': '3213', 'series_name': 'India tour of Australia 2020-21', 'match_desc': '2nd Test', 'status': 'IND won by 8 wkts', 'type': 'TEST', 'team1': {'name': 'Australia', 's_name': 'AUS'}, 'team2': {'name': 'India', 's_name': 'IND'}}, {'match_id': '30859', 'series_id': '3275', 'series_name': 'Pakistan tour of New Zealand 2020-21', 'match_desc': '1st Test', 'status': 'NZ won by 101 runs', 'type': 'TEST', 'team1': {'name': 'New Zealand', 's_name': 'NZ'}, 'team2': {'name': 'Pakistan', 's_name': 'PAK'}}, {'match_id': '31623', 'series_id': '3327', 'series_name': 'Sri Lanka tour of South Africa 2020-21', 'match_desc': '1st Test', 'status': 'RSA won by an innings and 45 runs', 'type': 'TEST', 'team1': {'name': 'South Africa', 's_name': 'RSA'}, 'team2': {'name': 'Sri Lanka', 's_name': 'SL'}}, {'match_id': '31727', 'series_id': '3248', 'series_name': 'Big Bash League 2020-21', 'match_desc': '20th Match', 'status': 'HBH won by 1 run', 'type': 'T20', 'team1': {'name': 'Hobart Hurricanes', 's_name': 'HBH'}, 'team2': {'name': 'Brisbane Heat', 's_name': 'BRH'}}, {'match_id': '30925', 'series_id': '3290', 'series_name': 'Super Smash 2020-21', 'match_desc': '5th Match', 'status': 'CD won by 45 runs', 'type': 'T20', 'team1': {'name': 'Central Districts', 's_name': 'CD'}, 'team2': {'name': 'Northern Knights', 's_name': 'NK'}}, {'match_id': '30930', 'series_id': '3290', 'series_name': 'Super Smash 2020-21', 'match_desc': '6th Match', 'status': 'Starts in 7 hrs 14 mins', 'type': 'T20', 'team1': {'name': 'Central Districts', 's_name': 'CD'}, 'team2': {'name': 'Auckland', 's_name': 'AKL'}}, {'match_id': '31728', 'series_id': '3248', 'series_name': 'Big Bash League 2020-21', 'match_desc': '21st Match', 'status': 'Starts in 14 hrs 49 mins', 'type': 'T20', 'team1': {'name': 'Adelaide Strikers', 's_name': 'ADS'}, 'team2': {'name': 'Perth Scorchers', 's_name': 'PRS'}}]
```
  
### get_highlights(match_id: str)
CODE:
```python
from crichighlights import CricHighlights

print(next(CricHighlights.get_highlights('30555')))
```
OUTPUT:
```text
{'timestamp': '1609213547645', 'o_no': '14.6', 'i_id': '4', 'score': '69', 'comm': "Labuschagne to Rahane, 3 runs, fuller and outside off, Rahane leans into the drive and places it through the gap at cover. Looked like it be a boundary, but it's hauled back in. Three more and India just a run away now"}
```
