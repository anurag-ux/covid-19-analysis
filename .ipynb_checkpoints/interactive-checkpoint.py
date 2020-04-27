import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def setup():
    global df
    global st_x
    global conf_y
    df=pd.read_csv('covid_19_india.csv')
    df['Date']=pd.to_datetime(df['Date'],format="%d/%m/%y")
    st_x=[]
    conf_y=[]
    for state in df['State/UnionTerritory'].unique():
        st_x.append(df[df['State/UnionTerritory']==state]['Date'])
        conf_y.append(df[df['State/UnionTerritory']==state]['Confirmed'])
def show_graph(state):
    fig1 = go.Figure()
    fig1.update_layout(title="Confirmed Cases",xaxis_title="Date",yaxis_title="Number of Cases",font=dict( family="Courier New, monospace",size=18,color="#096291" ))
    if(state!='all'):
        st=state.split()
        for s in st:
            i=np.where(df['State/UnionTerritory'].unique()==s)[0][0]
            fig1.add_trace(go.Scatter(x=st_x[i],y=conf_y[i],mode='lines+markers',name=df['State/UnionTerritory'].unique()[i]))
    else:
        for i in range(35):
            fig1.add_trace(go.Scatter(x=st_x[i],y=conf_y[i],mode='lines+markers',name=df['State/UnionTerritory'].unique()[i]))
    fig1.show()
if __name__ == "__main__":
    state=input('Enter State name(s) or type all to view every state ')
    setup()
    show_graph(state)
