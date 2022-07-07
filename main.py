#  coding=gbk
import os
from profit_type import profit_type
from TagScraping import tag_scraping


types = \
    [
        "[Free For Profit]",
        "[Free]",
        "[Free For Non-Profit]"
    ]

profit_types = \
    [
        profit_type(types[0], "x"),
        profit_type(types[1], "x"),
        profit_type(types[2], "x")
    ]

# AsksForInputs
type_beat_artist_one = input("Artist 1: ")
type_beat_artist_two = input("Artist 2: ")
type_beat_artist_three = input("Artist 3: ")
name = input("What is the beat called? ")
producer = input("Which tag? For example: \"Prod. by Crics\"... ")


# Chose profit type
def which_profit(profit_types):
    print("Choose by typing \"x\"")
    for profit in profit_types:
        askprofit = input(profit.type)
        if askprofit == profit.access:
            chosen_profit = profit.type
    print("Your beat is: " + chosen_profit)
    return chosen_profit


# Save return in var
chosen_profit = which_profit(profit_types)

# final beat name as variable
final_beat_name_var = chosen_profit + " " + type_beat_artist_one + " X " + type_beat_artist_two + " X " + type_beat_artist_three + " Type Beat | " + name + " | (" + producer + ")"

# Searching for Tags and saving them in var tags
tags = tag_scraping(final_beat_name_var)

# saving description as var
description = type_beat_artist_one + " X " + type_beat_artist_two + " X " + type_beat_artist_three + " Type Beat | " + name + " | (" + producer + ")" + "\n" + tags

# Writing in files (needs to be done with the "with open" command else throws error)
save_path = "/Users/soeren/Documents/Coding/Python/BeatFormatter/Output"
file_name_beatname = f"{name} final_beat_name.txt"
file_name_description = f"{name} final_beat_description.txt"

# Creating files and writing in them (based on save_path and variable file name)
with open(os.path.join(save_path, file_name_beatname), 'w') as f:
    f.write(final_beat_name_var)

with open(os.path.join(save_path, file_name_description), 'w') as g:
    g.write(description)

# Results
print("Your YouTube title should be: \n" + final_beat_name_var)
print("Use this tags for best engagement: \n" + tags)
