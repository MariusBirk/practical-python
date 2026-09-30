# pcost.py
#
# Exercise 1.27
import os

data = []

path = "/Users/sarahvroonland/Documents/Marius - Claude Code/Practical Python course/practical-python/Work/Data/portfolio.dat"

positions = []

with open(path, "rt") as f:
    next(f)
    for line in f:
        row = line.split()
        position = float(row[1]) * float(row[2])
        positions.append(position)

print(positions)

value = sum(positions)

print(value)
