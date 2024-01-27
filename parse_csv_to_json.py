import csv
import json

def parse_csv_to_json(csv_file, json_file_template, rows_per_file=1):
	data = parse_csv(csv_file)
	write_to_json(data, json_file_template, rows_per_file)

def parse_csv(csv_file):
	data = {}

	with open (csv_file, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		for row in csvReader:
			key = row['customerID']
			data[key] = row
	return data

def write_to_json(data, json_file_template, rows_per_file):
	file_idx=0
	for item in data:
		write_file_tmp = json_file_template + str(file_idx) + ".json"
		with open(write_file_tmp, 'w', encoding='utf-8') as jsonf:
			jsonf.write(json.dumps(data[item], indent=4))
		file_idx+=1

csv_file = "./data/csv/customer_churn.csv"
json_file_template = "./data/json/customer_churn_"

parse_csv_to_json(csv_file,json_file_template)