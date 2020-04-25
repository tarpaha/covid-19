#! python3
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='Covid-19 data filtering tool')
    parser.add_argument('input', help='csv file with global cases from https://github.com/CSSEGISandData/COVID-19')
    parser.add_argument('country', help='country to filter')
    parser.add_argument('output', help='csv file with in form year,month,day,cases,...')
    return parser.parse_args()

def read_input_rows(filename):
    with open(filename, 'r') as f:
        return [line.split(',') for line in f.readlines()]

def get_dates(dates_row):
    return [parse_datetime(dt) for dt in  dates_row[4:]]

def parse_datetime(dt):
    return [int(x) for x in dt.split('/')]

def get_country_cases(rows, country):
    country_rows = [row for row in rows if row[1] == country]
    if not country_rows:
        raise Exception(f'Cannot find data row for country {country}')
    print(f'Summing {len(country_rows)} provinces for country {country}')
    return calculate_country_cases(country_rows)
    return [int(cell) for cell in country_cases[4:]]

def calculate_country_cases(country_rows):
    country_cases = [int(case) for case in country_rows[0][4:]]
    for row_id in range(1, len(country_rows)):
        row = [int(case) for case in country_rows[row_id][4:]]
        for col in range(len(country_cases)):
            country_cases[col] += row[col]
    return country_cases

def compile_data(dates, cases):
    if len(dates) != len(cases):
        raise Exception(f'Dates count = {len(dates)} differs from cases count = {len(cases)}')
    data = []
    for dt, case in zip(dates, cases):
        data += [dt[2], dt[0], dt[1], case]
    return data

def write_data(filename, data):
    with open(filename, 'w') as f:
        f.write(','.join(str(v) for v in data))

if __name__== '__main__' :
    args = parse_args()
    try:
        rows = read_input_rows(args.input)
        dates = get_dates(rows[0])
        cases = get_country_cases(rows, args.country)
        data = compile_data(dates, cases)
        write_data(args.output, data)
        print(f'{len(cases)} records saved')
    except Exception as ex:
        print(f'Error: {str(ex)}')
        exit(1)
