#! python3
import datetime
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='Covid-19 graph tool')
    parser.add_argument('input', help='csv file with in form year,month,day,cases,...')
    parser.add_argument('caption', help='caption to show above graph')
    parser.add_argument('output', help='png file with graph')
    return parser.parse_args()

def read_csv(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.read().split(',')]

def read_and_parse_csv(filename):
    values = read_csv(filename)
    dates = []
    cases = []
    for i in range(0, len(values), 4):
        dates.append(datetime.datetime(2000 + values[i], values[i+1], values[i+2]))
        cases.append(values[i+3])
    return (dates, cases)

def logistic_function(L, k, x0, x):
    return L / (1 + np.exp(-k * (x - x0)))

def get_logistic_coeffs(dates, cases):
    def difference(coeffs):
        sum = 0
        start_date = dates[0]
        for date in dates:
            day = (date - start_date).days
            teor = logistic_function(coeffs[0], coeffs[1], coeffs[2], day)
            pract = cases[day]
            sum += (teor - pract)**2
        return sum
    minim = minimize(difference, [0, 0, 0])
    return minim.x

def plot_cases(dates, cases):
    plt.plot(dates, cases, 'ro', label='Infection cases')

def plot_approximation(dates, cases):
    days = range(180)
    coeffs = get_logistic_coeffs(dates, cases)
    dates_range = [dates[0] + datetime.timedelta(days=day) for day in days]
    logistic_values = [logistic_function(coeffs[0], coeffs[1], coeffs[2], day) for day in days]
    plt.plot(dates_range, logistic_values, label='Logistic curve approximation')
    
    derivative = np.diff(logistic_values)
    max_id = np.where(derivative == np.amax(derivative))[0][0]
    plt.annotate(
        dates_range[max_id].strftime('%d-%b-%Y'),
        xy=(dates_range[max_id], logistic_values[max_id]), xycoords='data',
        xytext=(0.6, 0.6), textcoords='axes fraction',
        arrowprops=dict(facecolor='black', width=2, headwidth=8, shrink=0.05),
        horizontalalignment='left', verticalalignment='top')

def plot(dates, cases, caption, filename):
    plt.figure(figsize=(15,8))
    plt.title(caption, Size=20)
    plot_cases(dates, cases)
    plot_approximation(dates, cases)
    plt.legend()
    plt.grid()
    plt.savefig(filename)

if __name__== '__main__' :
    args = parse_args()
    try:
        (dates, cases) = read_and_parse_csv(args.input)
        plot(dates, cases, args.caption, args.output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
        exit(1)
