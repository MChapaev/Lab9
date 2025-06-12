import csv
from pathlib import Path


def read_csv(path):
    with open(path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        print('Заголовки: ', header)

        for row in csv_reader:
            print(row)


# Main
def main():
    path = Path('__file__').resolve().parent / 'CSV' / '12 - 1.csv'
    read_csv(path)


if __name__ == '__main__':
    main()
