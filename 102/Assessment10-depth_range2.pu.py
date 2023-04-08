import csv

# Open the original CSV file and create a new CSV file for the parsed data
with open('formations.csv', 'r') as original_file, open('formations_parsed.csv', 'w', newline='') as parsed_file:
    # Create a CSV reader and writer
    reader = csv.reader(original_file)
    writer = csv.writer(parsed_file)

    # Read the header row from the original file and add the new column headers
    header = next(reader)
    new_header = header + ['Start Depth', 'End Depth', 'Difference in Depth', 'Age of Formation']
    writer.writerow(new_header)

    rows = []
    for row in reader:
        rows.append(row)
    
    depths = []
    forma = []
    for row in rows:
        for item in row:
            temp = item[0]
            if temp.isdigit() == True:
                depths.append(item)
            if temp.isdigit() == False:
                forma.append(item)

    diffs = []
    start_depth = []
    end_depth = []
    for i in depths:
        temp = i.split("-")
        if temp[0] == 0:
            temp1 = float(temp[0])
            temp1 = f'{temp1:.1f}'
        else:
            temp1 = float(temp[0])
            temp2 = float(temp[1])
        start_depth.append(temp1)
        end_depth.append(temp2)
        difference = float(temp[1]) - float(temp[0])
        difference = f'{difference:.2f}'
        diffs.append(difference)

    type_form = []
    for i in start_depth:
        if float(i) < 700:
            type_form.append("Paleocene")
        else:
            type_form.append("Cretaceous")

    rows = []
    for i in range(4):
        row = []
        row.append(depths[i])
        row.append(start_depth[i])
        row.append(end_depth[i])
        row.append(diffs[i])
        row.append(forma[i])
        row.append(type_form[i])
        rows.append(row)

    writer.writerow(rows[0])
    writer.writerow(rows[1])
    writer.writerow(rows[2])
    writer.writerow(rows[3])
