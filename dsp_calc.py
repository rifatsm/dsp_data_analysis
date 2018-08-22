###################################################################################################
# This code is to calculate the Diagnostic Print Statements lifespan compared to the launch times #
###################################################################################################

import pandas as pd 

### Reading .csv files
concat = pd.read_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_concat.csv")

### Storing the values under DataFrame
df_concat = pd.DataFrame(concat)

def count_printy_launches(usergroup):
	count_list = []
	# count_list.append('DSPCount')
	### Looping through the data
	count = 0
	for index, row in usergroup.iterrows():
		if row['Subtype'] == 'Temporary':
			if row['Subsubtype'] == 'Insertion':
				count = count + 1
			elif row['Subsubtype'] == 'Deletion':
				count = count - 1
		# print row['PrintStatements'], row['Subsubtype']
		count_list.append(count)

	series = pd.Series(count_list)
	usergroup['DSPCount'] = series.values
	return usergroup

results = df_concat.groupby(['userName', 'assignment']).apply(count_printy_launches)

### Output the values in .csv file
results.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_launches_dsp_calc.csv", index=False)


