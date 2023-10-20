import csv

def createCSV (json, outputPath = "output.csv"):
    fieldnames = json[0].keys()

    with open(outputPath, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader() 

        for item in json:
            writer.writerow(item)

    return True

