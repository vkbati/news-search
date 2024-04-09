import os
import csv

def gen_csv(articles, topic: str, filename="search_output.csv"):
    '''
    :param articles:
    :param filename: Specify the filename for the output CSV file. Default is "search_output.csv"

    Function for generating csv file
    '''
    # Create the directory if it does not exist
    output_directory = "outputs_csv"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Generates new file name if one exists
    file_path = os.path.join(output_directory, filename)
    if os.path.exists(file_path):
        filename_parts = os.path.splitext(filename)
        filename = filename_parts[0] + "_" + topic + "_new" + filename_parts[1]
        file_path = os.path.join(output_directory, filename)

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'url', 'publishedAt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for article in articles['articles']:
            writer.writerow({key: article.get(key, '') for key in fieldnames})