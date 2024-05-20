import random
import plotly.graph_objects as go

# Set the number of rolls
num_rolls = 100

# Initialize a list to store the results of each roll
roll_results = [0] * 13

# Simulate rolling two dice and storing the results
for i in range(num_rolls):
    roll = random.randint(1, 6) + random.randint(1, 6)
    roll_results[roll] += 1

# Create a bar chart using Plotly
fig = go.Figure(data=[go.Bar(x=list(range(2, 13)), y=roll_results[1:])])
fig.update_layout(title='Simulation of Rolling Two Dice',
                  xaxis_title='Sum of Two Dice',
                  yaxis_title='Number of Occurrences')

# Save the chart to an HTML file
fig.write_html('dice_rolls.html', auto_open=True)