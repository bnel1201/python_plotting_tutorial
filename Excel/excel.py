from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
from openpyxl.chart import Reference
from openpyxl.chart.data_source import NumDataSource, NumRef
from openpyxl.chart.error_bar import ErrorBars
from openpyxl.chart.series_factory import SeriesFactory
from openpyxl.chart import BarChart

from notebooks.utils import make_fake_dataframe


def to_excel_barchart(df, filename="untitled.xlsx", xlabel='samples', ylabel='value', title=''):
    """
    Takes every column of a dataframe and plots it as an excel barchart series
    """
    wb = Workbook()
    ws = wb.active

    for r in dataframe_to_rows(df, index=True, header=True):
        ws.append(r)

    chart1 = BarChart()
    chart1.type = "col"
    chart1.style = 10
    chart1.title = title
    chart1.y_axis.title = ylabel
    chart1.x_axis.title = xlabel

    data = Reference(ws, min_col=2, min_row=3, max_row=len(df)+2, max_col=len(df.columns))
    name_ref = Reference(ws, min_col=1, min_row=3, max_col=1, max_row=len(df) + 2)
    chart1.add_data(data, titles_from_data=True)
    chart1.set_categories(name_ref)
    chart1.shape = 4
    ws.add_chart(chart1, "A10")

    wb.save(filename)


def to_excel_error_barchart(df, filename="untitled.xlsx", xlabel='samples', ylabel='value', title=''):
    """
    Assumes that DataFrame `df` is organized as:
            | group 1 measure | group 1 measure error | group 2 measure | group 2 measure error | ...
    sample 1|                 |                       |                 |                       | ...
    sample 2|                 |                       |                 |                       | ...
    sample 3|                 |                       |                 |                       | ...
    .
    .
    .

    Then all groups are plotted in a single cluster, with a cluster for every sample provided
    """
    cols = df.columns.tolist()
    ngroups = len(cols[0::2])

    rearrange_cols = [*cols[0::2], *cols[1::2]]
    rearranged_df = df[rearrange_cols]

    wb = Workbook()
    ws = wb.active

    for r in dataframe_to_rows(rearranged_df, index=True, header=True):
        ws.append(r)

    name_ref = Reference(ws, min_col=1, min_row=3, max_col=1, max_row=len(df) + 2)
    col_idx = 2
    mean_refs = [Reference(ws, min_col=i, min_row=3, max_col=i, max_row=len(df) + 2) for i in range(col_idx, col_idx+ngroups)]
    col_idx += ngroups
    std_refs = [Reference(ws, min_col=i, min_row=3, max_col=i, max_row=len(df) + 2) for i in range(col_idx, col_idx+ngroups)]

    series_names = list(df.columns)[0::2]
    means_series = [SeriesFactory(mean_ref, title=name) for mean_ref, name in zip(mean_refs, series_names)]

    for i, std_ref in enumerate(std_refs):
        eBarsNumDataSource = NumDataSource(NumRef(std_ref))
        means_series[i].errBars = ErrorBars(errDir='y', errValType='cust', plus=eBarsNumDataSource, minus=eBarsNumDataSource)

    chartObj = BarChart()
    [chartObj.append(means) for means in means_series]
    chartObj.title = title
    chartObj.set_categories(name_ref)
    chartObj.y_axis.title = ylabel
    chartObj.x_axis.title = xlabel

    ws.add_chart(chartObj, 'B12')

    wb.save(filename)


def main():
    df = make_fake_dataframe()
    to_excel_barchart(df, filename="barchart.xlsx")

    to_excel_error_barchart(df, filename="error_barchart.xlsx", xlabel='Cytokines', ylabel='Relative Intensity', title='Cytokine Array')


if __name__ == '__main__':
    main()
