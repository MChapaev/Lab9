import pandas as pd
import re
from pathlib import Path


def parse_time_to_seconds(time_str):
    time_str = time_str.lower()
    hours = minutes = seconds = 0

    hour_match = re.search(r'(\d+)\s*ч', time_str)
    minute_match = re.search(r'(\d+)\s*мин', time_str)
    second_match = re.search(r'(\d+)\s*сек', time_str)

    if hour_match:
        hours = int(hour_match.group(1))
    if minute_match:
        minutes = int(minute_match.group(1))
    if second_match:
        seconds = int(second_match.group(1))

    return hours * 3600 + minutes * 60 + seconds


file_path = Path('__file__').resolve().parent / 'CSV' / '12 - 1.csv'
df = pd.read_csv(file_path)
df_clean = df[df['Состояние'] == 'Завершено'].copy()

df_clean['Оценка'] = df_clean['Оценка/10,00'].str.replace(',', '.').astype(float)
df_clean['Время (сек)'] = df_clean['Затраченное время'].apply(parse_time_to_seconds)
df_clean['ФИО'] = df_clean['Фамилия'].str.strip().str.title() + ' ' + df_clean['Имя'].str.strip().str.title()

df_passed = df_clean[df_clean['Оценка'] >= 6.00]
min_time = df_passed['Время (сек)'].min()
fastest_passed = df_passed[df_passed['Время (сек)'] == min_time]
fastest_sorted = fastest_passed.sort_values(by='ФИО')[['ФИО', 'Оценка', 'Время (сек)']]


# Main
def main():
    print(fastest_sorted.to_string(index=False))


if __name__ == '__main__':
    main()
