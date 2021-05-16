import csv
with open('log.csv', "r+") as f:
    lines = f.readlines()
lines.pop()
with open('log.csv', "w+") as f:
    f.writelines(lines)