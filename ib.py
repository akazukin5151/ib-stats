'''
You can find+replace "Group" with "Levels" to switch from G[1...6] to HL/SL and vice versa
'''

import altair as alt
import pandas as pd

data = pd.read_csv("/Users/Yuitere/Nextcloud/Maths/IB Stats/ib stats.csv")

selection = alt.selection_multi(fields=['Group'])
color = alt.condition(selection,
                      alt.Color('Group:N', legend=None),
                      alt.value('lightgray'))
#

chart = alt.Chart(data).mark_point().encode(
    x=alt.X("Number of candidates:Q", scale=alt.Scale(type='log', base=10)),
    y="Mean score",
    color=color
).properties(
    width=180,
    height=250
).facet(
    column="Group"
).interactive()

legend = alt.Chart(data).mark_point().encode(
    y=alt.Y("Group", axis=alt.Axis(orient='right')),
    color=color
).add_selection(
    selection
)

chart = alt.hconcat(chart, legend)
chart.save('/Users/Yuitere/Nextcloud/Maths/IB Stats/ib.html')
