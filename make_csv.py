# converts the TSV file to a CSV file to be used for the GitHub page.
import io
import csv
new_data = []
with open("riddle-arnold.tsv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter = "\t")
    for row in reader:
        row[0] = row[0].lower()
        new_row = f'"{row[0]}","<div style=""margin-left:1em"">{row[1]}</div>"'
        new_data.append(new_row)
g = io.open("data/riddle-arnold_for_web.csv", "w", encoding="utf-8", newline="\n")
for row in new_data:
    g.write(row+"\r\n")
