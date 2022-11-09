import data_csv
from dict_in_list import *
import charts


def run():
    result_data = data_csv.information_from_csv("./data.csv")
    labels, values = dict_in_list(result_data)
    charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()