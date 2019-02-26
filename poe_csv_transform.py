import csv

items = []

with open('poe_cur.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';')

		previous_occurence = None
		current_occurence = None
		current_item = []
		for index, row in enumerate(spamreader):
			if index > 0:
				if index == 1:
					previous_occurence = row[2]
				current_occurence = row[2]

				if current_occurence != previous_occurence:
					previous_occurence = row[2]
					items.append(current_item)
					current_item = []
					current_item.append(row)
					#new variable
				else:
					#still the same variable
					current_item.append(row)

the_zip = zip(*items)

with open('output_poe_cur.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')

    for row in the_zip:
    	spamwriter.writerow([item for sublist in row for item in sublist])