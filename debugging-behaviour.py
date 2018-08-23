############################################################
# This code is to analyze the debugging-behaviour.csv file #
############################################################

import pandas as pd 

### Reading .csv files
debugging_behaviour = pd.read_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/debugging-behaviour.csv")

### Storing the values under DataFrame
df = pd.DataFrame(debugging_behaviour)

### Calculating total number of projects
# print "Total rows: " + str(len(df))

### Creating a unique list
unique_list = df.userName.unique()

### Calculating the total number of students
#print len(unique_list) # 176 unique students in the course

df_debugger = df[df.debugSessionCount != 0]

### Calculating projects that launch debugger at least once
# print len(df_debugger) # 406 projects have debugger launches

debugger_list = df_debugger.userName.unique()

### Calculating the students who use debugger at least once
# print len(debugger_list) # 147 students use debugger in at least one of their projects

### Dropping the debugSessionCount column
df_prnt_stmt = df.drop(columns=['debugSessionCount'])

# print df_prnt_stmt

### Adding both of the launches
df_prnt_stmt['totalLaunches'] = df_prnt_stmt['normalLaunches'] + df_prnt_stmt['testLaunches']

# print df_prnt_stmt

### Keeping only the rows with non-zero totalLaunches
df_prnt_stmt_nonzero = df_prnt_stmt[df_prnt_stmt.totalLaunches != 0]

### Calculating projects with at least one DPS
# print len(df_prnt_stmt_nonzero) # 224 projects have atleast a DPS in either a normalLaunch or a testLaunch 

prnt_stmt_list = df_prnt_stmt_nonzero.userName.unique()

# print len(prnt_stmt_list) # 126 students used DPS at least once (either in normalLaunch or testLaunch)

prnt_stmt_normal = df_prnt_stmt[df_prnt_stmt.normalLaunches != 0]
prnt_stmt_test = df_prnt_stmt[df_prnt_stmt.testLaunches != 0]

# print len(prnt_stmt_normal) # 164 projects have atleast one DPS launch in normal launches 
# print len(prnt_stmt_test) # 217 projects have atleast one DPS launch in test launches 

prnt_stmt_both = prnt_stmt_normal[prnt_stmt_normal.testLaunches != 0]

# print len(prnt_stmt_both) # 157 projects have atleast one DPS launch in both normal launches and test launches

### Calculating number of submissions for each projects 
df_p1 = df[df.assignment == 'Project 1']
df_p2 = df[df.assignment == 'Project 2']
df_p3 = df[df.assignment == 'Project 3']
df_p4 = df[df.assignment == 'Project 4']

# print len(df_p1) # 164 submissions for Project 1
# print len(df_p2) # 144 submissions for Project 2 
# print len(df_p3) # 134 submissions for Project 3
# print len(df_p4) # 125 submissions for Project 4
# 164 + 144 + 134 + 125 = 567 (total)

debug_df_p1 = df_p1[df_p1.debugSessionCount != 0]
debug_df_p2 = df_p2[df_p2.debugSessionCount != 0]
debug_df_p3 = df_p3[df_p3.debugSessionCount != 0]
debug_df_p4 = df_p4[df_p4.debugSessionCount != 0]

# print len(debug_df_p1) # 124 students have at least once used the debugger for Project 1
# print len(debug_df_p2) # 110 students have at least once used the debugger for Project 2
# print len(debug_df_p3) # 86 students have at least once used the debugger for Project 3
# print len(debug_df_p4) # 86 students have at least once used the debugger for Project 4

### Calculating mean values on non-zero debugSessionCount values for each projects
# print debug_df_p1["debugSessionCount"].mean() # 49.984 is the mean debugSessionCount (non-zero data points) for Project 1 
# print debug_df_p2["debugSessionCount"].mean() # 89.8 is the mean debugSessionCount (non-zero data points) for Project 2 
# print debug_df_p3["debugSessionCount"].mean() # 53.477 is the mean debugSessionCount (non-zero data points) for Project 3 
# print debug_df_p4["debugSessionCount"].mean() # 60.605 is the mean debugSessionCount (non-zero data points) for Project 4 

### Calculating DPS for normal launches 
df_p1_normal = df_p1[df_p1.normalLaunches != 0]
df_p2_normal = df_p2[df_p2.normalLaunches != 0]
df_p3_normal = df_p3[df_p3.normalLaunches != 0]
df_p4_normal = df_p4[df_p4.normalLaunches != 0]

# print len(df_p1_normal) # 62 students have at least one DPS in normal launches for Project 1
# print len(df_p2_normal) # 73 students have at least one DPS in normal launches for Project 2
# print len(df_p3_normal) # 29 students have at least one DPS in normal launches for Project 3
# print len(df_p4_normal) # 0 student have at least one DPS in normal launches for Project 4

### Calculating mean of all DPS for normal launches for each projects
# print df_p1_normal["normalLaunches"].mean() # 175.516 is mean number of DPS in normal launches for Project 1
# print df_p2_normal["normalLaunches"].mean() # 192.082 is mean number of DPS in normal launches for Project 2
# print df_p3_normal["normalLaunches"].mean() # 53.517 is mean number of DPS in normal launches for Project 3
# print df_p4_normal["normalLaunches"].mean() # 0 is mean number of DPS in normal launches for Project 4

### Calculating DPS for test launches 
df_p1_test = df_p1[df_p1.testLaunches != 0]
df_p2_test = df_p2[df_p2.testLaunches != 0]
df_p3_test = df_p3[df_p3.testLaunches != 0]
df_p4_test = df_p4[df_p4.testLaunches != 0]

# print len(df_p1_test) # 76 students have at least one DPS in test launches for Project 1
# print len(df_p2_test) # 95 students have at least one DPS in test launches for Project 2
# print len(df_p3_test) # 46 students have at least one DPS in test launches for Project 3
# print len(df_p4_test) # 0 student have at least one DPS in test launches for Project 4

### Calculating mean of all DPS for normal launches for each projects
# print df_p1_test["testLaunches"].mean() # 525.566 is mean number of DPS in test launches for Project 1
# print df_p2_test["testLaunches"].mean() # 786.347 is mean number of DPS in test launches for Project 2
# print df_p3_test["testLaunches"].mean() # 200.87 is mean number of DPS in test launches for Project 3
# print df_p4_test["testLaunches"].mean() # 0 is mean number of DPS in test launches for Project 4

### Outputting to files
# df_p1_normal.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_p1_normal.csv", index=False)


# df_prnt_stmt = df[df.normalLaunches != 0 or df.testLaunches != 0] # ValueError

# prnt_stmt_list = df_prnt_stmt.userName.unique()

# print len(prnt_stmt_list)
