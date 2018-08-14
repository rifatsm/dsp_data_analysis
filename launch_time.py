############################################################################################
# This code is to create a sorted & concatenated .csv from launches.csv and print-stmt.csv #
############################################################################################

import pandas as pd 

### Reading .csv files
launches = pd.read_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/launches_new.csv")
print_stmt = pd.read_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/print-stmt.csv")

### Storing the values under DataFrame
df_launches = pd.DataFrame(launches)
df_print_stmt = pd.DataFrame(print_stmt)

### Renaming to match the same column names
df_print_stmt = df_print_stmt.rename(columns={"userId":"userName", "CASSIGNMENTNAME":"assignment"})

### Concatenate dataframes 
df_concat = pd.concat([df_launches, df_print_stmt])

### Sorting concatenated values by time
df_concat = df_concat.sort_values(by=['userName', 'assignment', 'time'])

### Setting indices to the dataframe
df_concat = df_concat.set_index(['userName', 'assignment'])

### Output the values in .csv file
df_launches.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_launches.csv", index=False)
df_print_stmt.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_print_stmt.csv", index=False)
df_concat.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_concat.csv")