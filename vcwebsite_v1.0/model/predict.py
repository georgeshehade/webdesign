import sqlite3
from scipy.spatial import distance

# vectorized_words = db values as a dict


def create_datapoint(comp_values):

  datapoint = []
  for value in comp_values:
    datapoint.append(list(vectorized_words[value]))

  return np.mean(datapoint, axis = 0)

datapoint = create_datapoint(comp_values)

# we get cluster centroids from database
#cluster_centroids = extract centroids from db

# here we calculate the closest distance to centroid
distances = {}
for idx, cluster in enumerate(cluster_centroids):
    # cluster = [cluster[i] for i in range(len(cluster))]

    dst = distance.euclidean(cluster, datapoint)

    distances[str(idx)] = dst

minval = min(distances, key=distances.get)
