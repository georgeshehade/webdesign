from sklearn.cluster import KMeans
import numpy as np
from multiprocessing.dummy import Pool
import functools

def find_opt_clusters(n_clusters, algo, X):
    """
    Function find optimal number of clusters using kmeans and
    --------
    Params:
        -n_clusters     :'The number of clusters to try'
        -algo        :'Give cluster algorithm object as argument'
        -X              :'Datapoints to cluster on'

    --------
    Returns: silhoutte score
    """
    from sklearn.metrics import silhouette_score # import silhoutte score to calculate optimal n_clusters
   
    # Minum 11 people in database for this to work
    algo.set_params(**{"n_clusters":n_clusters}) # set number of clusters
    labels = algo.fit_predict(X) # fit and predict
    score = silhouette_score(X, labels)
    return score

def initialize_centroids(data): # data will be a numpy array
    """
    Function optimizes best cluster number using muliprocessing
    -----------------
    Returns: cluster_centroids
    """
    kmeanstest = KMeans()
    clusters = [x for x in range(3, 11)] # here we test the number of clusters inbetween 2/10

    # here we implement parallelization for speed reasons to find optimal solution
    pool = Pool()
    results = pool.map(functools.partial(find_opt_clusters, kmeans=kmeanstest, X=data), clusters)
    pool.close()
    pool.join()

    # here we define the number of clusters for the real training
    n_clusters = clusters[results.index(min(results))]

    kmeans = KMeans(n_clusters=n_clusters).fit(data)

    centroids = kmeans.cluster_centers_
    return centroids


