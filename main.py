#Rolling dice
#Getting frequency of each dice side
#clculated frequency will be Bar plotted

# Importing the Libraries
from typing import Text
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

# Flipping the dice and Calculating dice Frequencies
rolls = [random.randrange(1, 7) for i in range(100)]
values, frequencies = np.unique(rolls, return_counts=True)

# Creating the Initial Bar Plot
title = f"rolling dice {len(rolls):,} Times"
sns.set_style("darkgrid")
axes = sns.barplot(x=values, y=frequencies, palette="bright")

# Setting the Window Title and Labeling the x- and y-Axes
axes.set_title(title)
axes.set_ylim(top=max(frequencies) * 1.30)

axes.set(xlabel="Dice Value", ylabel="Frequency")
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
plt.show()