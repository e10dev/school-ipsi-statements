import plotly.graph_objects as go

months = ['심인고', '영남고', '제일여상', '동지여고', '달성고', '상서고',
          '중산고', '경화여고', '경원고', '대구여상', '상주고', '구미전자공고']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=months,
    y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
    name='2021년도',
    marker_color='Cadetblue'
))
fig.add_trace(go.Bar(
    x=months,
    y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
    name='2020년도',
    marker_color='lightsalmon'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()