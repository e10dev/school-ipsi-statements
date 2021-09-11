import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 180,
    delta = {'reference': 200},
    domain = {'x': [0.25, 1], 'y': [0.08, 0.25]},
    title = {'text': "작년대비지원자"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 300]},
        'threshold': {
            'line': {'color': "black", 'width': 2},
            'thickness': 0.75,
            'value': 170},
        'steps': [
            {'range': [0, 150], 'color': "gray"},
            {'range': [150, 250], 'color': "lightgray"}],
        'bar': {'color': "black"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 35,
    delta = {'reference': 50},
    domain = {'x': [0.25, 1], 'y': [0.4, 0.6]},
    title = {'text': "금일지원자"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 100]},
        'threshold': {
            'line': {'color': "black", 'width': 2},
            'thickness': 0.75,
            'value': 50},
        'steps': [
            {'range': [0, 25], 'color': "gray"},
            {'range': [25, 75], 'color': "lightgray"}],
        'bar': {'color': "black"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 237,
    delta = {'reference': 210},
    domain = {'x': [0.25, 1], 'y': [0.7, 0.9]},
    title = {'text' :"현재지원자"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 300]},
        'threshold': {
            'line': {'color': "black", 'width': 2},
            'thickness': 0.75,
            'value': 210},
        'steps': [
            {'range': [0, 150], 'color': "gray"},
            {'range': [150, 250], 'color': "lightgray"}],
        'bar': {'color': "black"}}))
fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})

fig.show()