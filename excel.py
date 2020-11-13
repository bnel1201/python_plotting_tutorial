from openpyxl import Workbook
from openpyxl.chart import BarChart, Series, Reference
import numpy as np
import pandas as pd


def write_to_barchart(df, filename="untitled.xlsx", xlabel='samples', ylabel='value', title=''):
    names = tuple(df.columns)
    rows = np.array(df)
    wb = Workbook(write_only=True)
    ws = wb.create_sheet()

    ws.append(names)

    for row in rows:
        ws.append(list(row))

    chart1 = BarChart()
    chart1.type = "col"
    chart1.style = 10
    chart1.title = title
    chart1.y_axis.title = ylabel
    chart1.x_axis.title =  xlabel

    data = Reference(ws, min_col=2, min_row=1, max_row=len(rows), max_col=len(rows[0]))
    cats = Reference(ws, min_col=1, min_row=2, max_row=len(rows))
    chart1.add_data(data, titles_from_data=True)
    chart1.set_categories(cats)
    chart1.shape = 4
    ws.add_chart(chart1, "A10")

    wb.save(filename)


def main():
    df = pd.read_csv("random_data.csv")
    write_to_barchart(df, filename="excel_export.xlsx")

if __name__ == '__main__':
    main()
