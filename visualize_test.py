import pandas as pd
from plotnine import ggplot, aes, geom_segment, theme_minimal, labs, theme, element_rect, element_line
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the CSV file into a DataFrame
df = pd.read_csv('./rapid_data/NHDFlowline_San_Guad/reach_info.csv')
# Strip leading and trailing spaces from column names
df.columns = df.columns.str.strip()

print(df)

# Create a static plot
plot = (ggplot(df, aes(x='Start Longitude', y='Start Latitude'))
        + geom_segment(aes(xend='End Longitude', yend='End Latitude'), color='blue')
        + theme_minimal()
        + labs(title='River Network', x='Longitude', y='Latitude')
        + theme(
            plot_background=element_rect(fill='white'),
            panel_background=element_rect(fill='white'),
        ))

# Display the plot
print(plot)

# # Prepare the figure and axis for animation
# fig, ax = plt.subplots()
# ax.set_xlim(df['Longitude'].min() - 0.01, df['Longitude'].max() + 0.01)
# ax.set_ylim(df['Latitude'].min() - 0.01, df['Latitude'].max() + 0.01)
# line, = ax.plot([], [], 'bo-', markersize=8)

# def init():
#     line.set_data([], [])
#     return line,

# def update(frame):
#     subset = df.iloc[:frame+1]
#     line.set_data(subset['Longitude'], subset['Latitude'])
#     return line,

# # Create the animation
# ani = FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True, repeat=False)

# # Save the animation as a GIF
# ani.save('/mnt/data/river_flow.gif', writer='imagemagick', fps=1)

# plt.show()

