#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:06:19 2020

@author: ethanbaietti
"""
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

career = pd.read_excel("Lebron_Career.xlsx")
playoffs = pd.read_excel("Lebron_Playoffs.xls")

#Series of Necessary numbers

data_career = career.loc[17, ["MP","PTS", "AST", "TRB"]]
data_current = career.loc[16, ["MP","PTS", "AST", "TRB"]]
data_playoffs = playoffs.loc[13, ["MP","PTS", "AST", "TRB"]]

graph_df = pd.concat([data_career, data_current, data_playoffs], axis=1)

#Change Column Names

colnames = ['Career (Regular Season)', '19-20 Season', 'Career (Playoffs)']
graph_df.columns = colnames

#Graph

bar_width = 0.3
x = np.arange(len(data_career))

fig, ax = plt.subplots()
group1 = ax.bar(x, data_career, bar_width, color = "purple", label = "Career - Regular Season")
group2 = ax.bar(x + bar_width, data_playoffs, bar_width, color = "gold", label = "Career - Playoffs")
group3 = ax.bar(x + bar_width*2, data_current, bar_width,color = "black", label = "2019 - 2020 Season")

ax.set_title('Lebron James Box Score Averages')
ax.set_xticks(x + bar_width)
ax.set_yticks(range(0,55,5))
ax.set_xticklabels(['MPG','PPG', 'AST', 'RBD'])
ax.legend()

def autolabel(groups):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for group in groups:
        height = group.get_height()
        ax.annotate('{}'.format(height),
                    xy=(group.get_x() + group.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(group1)
autolabel(group2)
autolabel(group3)

plt.show()



