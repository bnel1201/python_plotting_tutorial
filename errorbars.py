# %%
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
from openpyxl.chart import Reference
from openpyxl.chart.data_source import NumDataSource
from openpyxl.chart.data_source import NumRef
from openpyxl.chart.error_bar import ErrorBars
from openpyxl.chart.series_factory import SeriesFactory
from openpyxl.chart import BarChart

from notebooks import utils


# %%
ngroups = 6

means = [utils.random_heights() for i in range(ngroups)]
stds = [utils.random_heights()/10 for i in range(ngroups)]
names = utils.random_names(means[0])


# %%
z = dict()
dicts = [{f'group {i} mean': mean, f'group {i} std': std} for mean, std, i in zip(means, stds, range(len(means)))]
[z.update(d) for d in dicts]
df = pd.DataFrame(z, index = names)
df


# %%
cols = df.columns.tolist()
cols


# %%
rearrange_cols = [*cols[0::2], *cols[1::2]]
rearrange_cols


# %%
rearranged_df = df[rearrange_cols]


# %%
wb = Workbook()
ws = wb.active

for r in dataframe_to_rows(rearranged_df, index=True, header=True):
    ws.append(r)


# %%
name_ref = Reference(ws, min_col=1, min_row=3, max_col=1, max_row=len(means[0])+2)
col_idx = 2
mean_refs = [Reference(ws, min_col=i, min_row=3, max_col=i, max_row=len(means[0])+2) for i in range(col_idx, col_idx+ngroups)]
col_idx += ngroups
std_refs = [Reference(ws, min_col=i, min_row=3, max_col=i, max_row=len(means[0])+2) for i in range(col_idx, col_idx+ngroups)]


# %%
means_series = [SeriesFactory(mean_ref, title=f'group {i}') for i, mean_ref in enumerate(mean_refs)]


# %%
for i, std_ref in enumerate(std_refs):
    eBarsNumDataSource = NumDataSource(NumRef(std_ref))
    means_series[i].errBars = ErrorBars(errDir='y', errValType='cust', plus=eBarsNumDataSource, minus=eBarsNumDataSource)

# %%
chartObj = BarChart()
[chartObj.append(means) for means in means_series]
chartObj.title = 'Cytokine array results'
chartObj.set_categories(name_ref)
chartObj.y_axis.title = "Relative Intensity"
chartObj.x_axis.title = "Cytokine"

# %%
ws.add_chart(chartObj, 'B12')

# %%
wb.save('sampleChart.xlsx')
