import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output, State
import base64
import pandas as pd
import io
import datetime
import plotly.graph_objects as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

app.layout = html.Div([
    dcc.Store(id='store'),
    dbc.Row(
        dbc.Col([
            dcc.Upload([html.Div([
                html.H5('Arraste os arquivos aqui, ou clique')
                ])
            ], id='upload', style = {'borderStyle' : 'dashed'}, multiple=True),
            html.Br()],
            style = {'textAlign': 'center'}, width=4
        ), justify = 'center' #Final da coluna 1
    ), # Final da linha 1
    dbc.Row([
        dbc.Col(
            dbc.Jumbotron(id = 'tab')
        ), # Final da coluna 1
        dbc.Col(
            dbc.Jumbotron(dcc.Graph(id='grafico'))
        ) # Final da coluna 2
    ]) # Final da linha 2
], style = {'padding': '10px 20px 10px 20px'}
)


def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        df = pd.read_csv(
            io.StringIO(decoded.decode('utf-8')), header = 0)
    except:
        return html.Div([
            'There was an error processing this file.'
        ])
    return df

@app.callback(Output('store', 'data'),
              Input('upload', 'contents'),
              State('store', 'data'))
def my_data(cont, dat):
    if cont is not None:
        conteudos = [parse_contents(c) for c in cont]
        par = pd.concat(conteudos, ignore_index= True).to_dict('list')
        if dat is not None:
            tot = {i : dat[i]+par[i] for i in dat.keys()}
            return tot
        else:
            return par
    else:
        return dash.no_update

@app.callback(Output('grafico', 'figure'),
              Input('store', 'data'))
def upload(dat):
    if dat is not None:
        grafico = go.Figure(data=[go.Histogram(x=dat['Total'])])
        return grafico
    else:
        return dash.no_update

@app.callback(Output('tab', 'children'),
              Input('store', 'data'))
def update_output(dat):
    if dat is not None:
        df_par=pd.DataFrame.from_dict(dat)
        tabela = dbc.Table.from_dataframe(
                df_par, striped=True, bordered=True, hover=True)
        return html.Div([tabela], style={'height': '450px', 'overflowY': 'auto'})
    else:
        return dash.no_update

if __name__ == "__main__":
    app.run_server(debug=True)
