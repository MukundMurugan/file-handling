import csv
import json

# Read data from text file
with open('data.txt', 'r') as file:
    lines = file.readlines()

# Process data
total_age = 0
num_people = 0
people_data = []
for line in lines[1:]:  # Skip header line
    parts = line.strip().split(', ')
    name, age, country = parts
    total_age += int(age)
    num_people += 1
    people_data.append({'name': name, 'age': int(age)})

# Calculate average age
average_age = total_age / num_people

# Write to CSV
with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Age'])
    for person in people_data:
        csv_writer.writerow([person['name'], person['age']])

# Write to JSON
with open('output.json', 'w') as jsonfile:
    json.dump({'average_age': average_age}, jsonfile)
