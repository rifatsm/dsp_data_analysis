#####################################################
# This code is to analyze the consolidated.csv file #
#####################################################

### Importing libraries 

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 


### Calculating Correctness of the Kmeans algo:
def kmeans_correctness(clusters, X, y):
	kmeans = KMeans(n_clusters=clusters)
	kmeans.fit(X)

	correct = 0
	for i in range(len(X)):
	    predict_me = np.array(X[i].astype(float))
	    predict_me = predict_me.reshape(-1, len(predict_me))
	    prediction = kmeans.predict(predict_me)
	    if prediction[0] == y[i]:
	        correct += 1

	# print correct
	# print len(X)

	return float(correct)/float(len(X))


### Reading from files
consolidated = pd.read_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/consolidated.csv")

### Creating Dataframes 
df = pd.DataFrame(consolidated)

### Selecting specific sample size
df_p1 = df[df.assignment == 'Project 1']

# describe = df_p1.describe()

# print df_p1.head()

df_p1 = df_p1.drop(['userName', 'assignment', 'submissionTimeRaw', 'dueDateRaw', 'max.score.correctness', 'score.reftest', 'projectStartTime'], axis=1)
# df_p1.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_p1.csv", index=False)

score_array = []
score_threshold = 0.90
for index, row in df_p1.iterrows():
	if row['score'] >= score_threshold:
		score_array.append(1)
	else:
		score_array.append(0)

# print score_array

### Setting X and y values
X = np.array(df_p1.drop(['score'],1).astype(float))
y = score_array

### Running the Kmeans algo for different cluster size
for clust in range(1,20):
	print "clust: " + str(clust) + " " + str(kmeans_correctness(clust, X, y)*100) # The best result is for clust == 2 

### Append score_array to the dataframe
# df_out = df_p1
# df_out['score'] = score_array

# print df_out

# print describe

### Outputing to files 
# describe.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/describe.csv", index=True)
# df_out.to_csv("/Summer 2018/Dr. Cliff Shaffer's Lab/DSP vs Launch Times Analysis/df_out_2.csv", index=True)

