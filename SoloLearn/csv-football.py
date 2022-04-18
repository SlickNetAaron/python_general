#/usr/bin/env python3

# read csv into dict
# set smallest_diff to 10,000
# calculate the diff of each team
# if team_diff < smallest_diff, set that team to lowest 
# return team with lowest diff and diff
# ?? How to account for plural teams with smallest diff? ??

import csv
import pandas

def write_csv_data(filename):
    with open(filename, 'w') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter=',')
        csv_writer.writerow(["Team","Games","Wins","Losses","Draws","Goals For","Goals Against"])
        csv_writer.writerow(["Liverpool FC",38,32,3,3,85,33])
        csv_writer.writerow(["Norwich City FC",38,5,27,6,26,75])
        csv_writer.writerow(["Arsenal",38,26,9,3,79,36])


def import_csv_data(filename):
    with open(filename, 'r', newline='') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        line = 0
        for row in csv_reader:
            if line == 0:
                print(f'fields are {" ".join(row)}')
            print(row.items())
            line += 1
            # if row['Team'] == 'Team':
            
            # print(f'{row["Team"]}')

df = pandas.read_csv('csv-football.csv', index_col='Team')
# print(df['Goals For'][0])
# print(df[['Goals For', 'Goals Against']])

df['Score Diff'] = abs(df['Goals For'] - df['Goals Against'])
min_diff = df['Score Diff'].min()
team_min_diff = df[(df['Score Diff'] == min_diff)]

for row in range(len(team_min_diff)):
    print(f"The {team_min_diff.index[row]} team had the lowest differential with {team_min_diff['Goals For'][row]} goals made and {team_min_diff['Goals Against'][row]} goals against ")

# write_csv_data('csv-football.csv')
# import_csv_data('csv-football.csv')