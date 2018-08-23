#####################################################
# This code is to analyze the consolidated.csv file #
#####################################################

### Importing libraries 

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

### Reading from files
consolidated = pd.read_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/consolidated.csv")

### Creating Dataframes 
df = pd.DataFrame(consolidated)

### Selecting specific sample size
df_p1 = df[df.assignment == 'Project 1']

describe = df_p1.describe()

# print describe

### Outputing to files 
# describe.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/describe.csv", index=True)

