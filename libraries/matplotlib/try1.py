import matplotlib.pyplot as plt
import csv
from collections import Counter

with open('data.csv') as csvfile:
    csv_reader = csv.DictWriter(csvfile)
    language_counter = Counter()
    for row in csvfile:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

print(language_counter)

