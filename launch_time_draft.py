import pandas as pd 

### Reading .csv files
launches = pd.read_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/launches_new.csv")
print_stmt = pd.read_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/print-stmt.csv")

### Printing for debugging
# print(launches)
# print(print_stmt)

### Storing the values under DataFrame
df_launches = pd.DataFrame(launches)
df_print_stmt = pd.DataFrame(print_stmt)

### Setting indices to the dataframes
df_launches = df_launches.set_index(['userName', 'assignment'])
df_print_stmt = df_print_stmt.set_index(['userId', 'CASSIGNMENTNAME'])

### Sorting by columns
df_launches = df_launches.sort_values(by=['userName', 'assignment', 'time'])
df_print_stmt = df_print_stmt.sort_values(by=['userId', 'CASSIGNMENTNAME', 'time'])

### Output the values in .csv file
df_launches.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_launches_draft.csv")
df_print_stmt.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_print_stmt.csv")