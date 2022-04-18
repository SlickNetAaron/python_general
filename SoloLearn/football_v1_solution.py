# From https://realpython.com/python-interview-problem-parsing-csv-files/
# Not my original work. Just followed solution.

import csv

def parse_next_line(csv_file):
    for line in csv.DictReader(csv_file):
        yield line

def get_name_and_diff(team_stats):
    diff = int(team_stats["Goals For"]) - int(team_stats["Goals Against"])
    return team_stats["Team"], abs(diff)

def get_min_score_difference(filename):
    with open(filename, "r", newline="") as csv_file:
        min_diff = 10000
        min_team = None
        for line in parse_next_line(csv_file):
            team, diff = get_name_and_diff(line)
            if diff < min_diff:
                min_diff = diff
                min_team = team
    return min_team, min_diff