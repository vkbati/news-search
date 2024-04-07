import csv
def gen_csv(articles):
    with open("../search_output.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'url', 'publishedAt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for article in articles['articles']:
            writer.writerow({key: article[key] for key in fieldnames})