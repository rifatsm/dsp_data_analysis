###################################################################################################
# This code is to calculate the Diagnostic Print Statements lifespan compared to the launch times #
###################################################################################################

import pandas as pd 

### Reading .csv files
concat = pd.read_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_concat.csv")

### Storing the values under DataFrame
df_concat = pd.DataFrame(concat)

### Output the values in .csv file
df_concat.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_launches_dsp_calc.csv", index=False)