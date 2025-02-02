import plotly.graph_objects as charts

# Labels for the sankey chart (from a view)
sourceLabels = ['Hirvi', 'Peura'] # Where the meat is coming from
targetLabels = ['Ryhmä 1', 'Ryhmä 2', 'Ryhmä 3'] # What group has received meat
allLabels = sourceLabels + targetLabels # All labels for the chart in a single list
print(allLabels)

# Simulation Data (list of tuples), in relity the data should come from the database view 
dBdata = [('Hirvi', 'Ryhmä 1', 100),
    ('Hirvi', 'Ryhmä 2', 200),
    ('Hirvi', 'Ryhmä 3', 100),
    ('Peura', 'Ryhmä 2', 50)
    ]

# Define colors for meat sources (animals) -> for sending nodes ie. left side boxes in the chart
sourceNodeColors = ['rgba(128, 128, 128, 0.75)', 'rgba(150, 50, 0, 0.75)' ] # Alpha (opacity) 0 - 1 

# Define colors for meat targets (group) -> for receiving nodes ie. right side boxes in the chart
targetNodeColors = ['red', 'orange', 'green'] # CSS named colors

# All label colors in a single list for the chart
allColors = sourceNodeColors + targetNodeColors 

rows = len(dBdata)
print(rows)
# Empty lists for label indexses and values
sankeySources = []
sankeyTargets = []
sankeyValues = []

# Create Indexes for sankey chart
for row in dBdata:
    tupleSource = row[0]
    tupleTarget = row[1]
    tupleValue = row[2]
    sourceIx = allLabels.index(tupleSource)
    targetIx = allLabels.index(tupleTarget)
    sankeySources.append(sourceIx)
    sankeyTargets.append(targetIx)
    sankeyValues.append(tupleValue)

print(sankeySources)

figure = charts.Figure(data=[charts.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = allLabels,
      color = allColors
    ),
    link = dict(
      source = sankeySources, 
      target = sankeyTargets,
      value = sankeyValues,
      color = 'rgba(255, 128, 0, 0.5)'
  ))])

figure.update_layout(title_text="Lihanjakotilanne", font_size=24)
figure.show()