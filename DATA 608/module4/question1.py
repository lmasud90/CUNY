import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import dash_table_experiments as dtbl
from scipy import stats

# start the dash app
app = dash.Dash()

df = pd.read_csv('./Data/riverkeeper_data_2013.csv')
df['EnteroNo'] = df['EnteroCount']

# https://stackoverflow.com/questions/13682044/pandas-dataframe-remove-unwanted-parts-from-strings-in-a-column
df['EnteroNo'] = df['EnteroCount'].map(lambda x: x.lstrip('<>'))

#Convert EnteroCount to int
df['EnteroCount'] = df['EnteroCount'].values.astype(np.int64)
df['Entero Count'] = df['EnteroCount']
df['Dt'] = pd.to_datetime(df.Date)

df = df.sort_values(by=['Dt'],ascending=0)
#Get distinct dates
sDates = df.Date.unique()


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    html.H2('Water Information System', style={
            'textAlign': 'center',
    }),
    html.Label('Pick a date:'),
    dcc.Dropdown(
        id='field-dropdown',
        options=[{'label': d, 'value': d} for d in sDates],
        value=sDates[0],
        clearable=False
    ),
    html.Div([   dtbl.DataTable(
        rows=[{}],
        row_selectable=False,
        filterable=False,
        sortable=False,
        editable=False,
        selected_row_indices=[],
        id='table'
    ),
    html.Div(id='data')
    ])
])

@app.callback(
    dash.dependencies.Output('table', 'rows'),
    [dash.dependencies.Input('field-dropdown', 'value')])
    
def update_date(date):
    updates = pd.DataFrame()
    start_date = pd.to_datetime(date)
    filtered = df[df['Dt'] <= start_date]

    for site in filtered.Site.unique():
        filtered_site = filtered[filtered['Site'] == site]

        lastSample = max(pd.to_datetime(filtered_site.Date))
        lastSample = pd.to_datetime(lastSample)
        eMaxDf = filtered_site[filtered_site['Dt'] == lastSample]
        eMax = max(eMaxDf['EnteroCount'])
        
        if eMax > 110:
            safety = "Yes"
            
        if ((len(filtered_site) >= 5) and (eMax <= 110)):
            gMean = stats.gmean(filtered_site.loc[:,"EnteroCount"])
            if gMean > 30:
                safety = "No"
            else:
                safety = "Yes"

        #Mark it safe
        if ((len(filtered_site) < 5) and (eMax <= 110)):
                safety = "Yes"

        data = {'Site':site, 'Safe To Kayak':safety, 'Last Sample Date':lastSample.strftime('%m/%d/%Y')}
        updates = updates.append(data, ignore_index=True)
    
    if (len(updates) == 0):
        data = {'Site':'', 'Enterococcus Count':'', 'Safe To Kayak':'', 'Last Sample Date':''}
        updates = updates.append(data, ignore_index=True)

    cols = ['Site','Safe To Kayak', 'Last Sample Date']
    updates = updates[cols]
    return(updates.to_dict('records'))


if __name__ == '__main__':
    app.run_server(debug=True)