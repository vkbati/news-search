import csv
import os
def gen_csv(articles, topic: str, filename="../search_output.csv"):
    '''
    :param articles:
    :param filename: Specify the filename for the output CSV file. Default is "../search_output.csv"

    Function for generating csv file
    '''
    # Generates new file name if one exists
    if os.path.exists(filename):
        filename_parts = os.path.splitext(filename)
        filename = filename_parts[0] + "_" + topic + "_new" + filename_parts[1]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'url', 'publishedAt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for article in articles['articles']:
            writer.writerow({key: article[key] for key in fieldnames})