
# Visualise Iris data with Seaborn


import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# Plot histogram of sepal length dimension in stacked bar
iris=pd.read_csv("iris.csv")

# hue is the class separation
sns.histplot(data=iris,  x="SepalLengthCm", hue=iris["Species"], multiple="stack")
plt.show()

# Plot histogram of classes of sepal length dimension in three sub plots
g = sns.FacetGrid(iris, col="Species")
g.map(sns.histplot, "SepalLengthCm")
plt.show()

# Scatter plot between speal length vs petal length
g = sns.FacetGrid(iris, hue="Species")
g.map(sns.scatterplot, "SepalLengthCm", "SepalWidthCm", alpha=.7)
g.add_legend()
plt.show()


### Plot histograms and scatter plots for all dimensions in one single figure
g = sns.PairGrid(iris, hue="Species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.show()
