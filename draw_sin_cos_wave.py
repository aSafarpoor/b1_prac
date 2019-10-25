import numpy as np

import matplotlib.pyplot as plot

 

# Get x values of the cosine wave

phase = np.arange(0, 3.14, 0.02);

 

# Amplitude of the cosine wave is cosine of a variable like time

amplitude   = np.cos(phase)+np.sin(phase)

 

# Plot a cosine wave using time and amplitude obtained for the cosine wave

plot.plot(phase, amplitude)

 

# Give a title for the cosine wave plot

plot.title('wave')

 

# Give x axis label for the cosine wave plot

plot.xlabel('phase')

 

# Give y axis label for the cosine wave plot

plot.ylabel('Amplitude = cosine(time)')

 

# Draw the grid for the graph

plot.grid(True, which='both')

 

plot.axhline(y=0, color='b')

 

# Display the cosine wave plot

plot.show()