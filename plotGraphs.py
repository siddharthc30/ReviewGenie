import plotly
import plotly.graph_objects as go
import json

#funciton for plotting the pie chart of sentiment of whole product reviews
def plot_pie(overall_sentiment):
    labels = ['Negative', 'positive', 'Neutral']
    values = [overall_sentiment['positive_score'], overall_sentiment['negative_score'], overall_sentiment['neutral_score']]

    fig = go.Figure(data =[go.Pie(labels = labels, values = values)])
    piejson = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    #fig.show()
    return piejson


#Function for plotting bar graph for the opinion and its trait
def plot_bar(opinion):
    words = list(opinion.keys())
    positive = []
    negative = []
    for op in opinion.values():
       positive.append(op[0])
       negative.append(op[1])  

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x = words,
        y = positive,
        name = 'Positive opinion'
    ))

    fig.add_trace(go.Bar(
        x = words,
        y = negative,
        name = 'Negative opinion'
    ))

    fig.update_layout(barmode = 'group', bargap = 0.2, bargroupgap = 0.15)
    barjson = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    #fig.show()
    return barjson



