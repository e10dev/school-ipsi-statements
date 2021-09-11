import plotly.express as px
data = dict(
    character=["모집인원", "Cain", "관심인원", "상담완료", "상담예정", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "모집인원", "모집인원", "관심인원", "관심인원", "모집인원", "모집인원", "Awan", "모집인원" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig =px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
)
fig.show()