import csv

example = [
    {
        "name": "Item 1",
        "price": 10.99,
        "quantity": 5
    },
    {
        "name": "Item 2",
        "price": 5.99,
        "quantity": 3
    }
]

def createCSV (json, outputPath = "output.csv"):
    fieldnames = json[0].keys()

    with open(outputPath, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader() 

        for item in json:
            writer.writerow(item)

    return True

