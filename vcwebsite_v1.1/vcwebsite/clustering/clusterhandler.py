import os
import importlib
from vcwebsite.models import User, Values
import json
import numpy as np
import pandas as pd
from scipy.spatial import distance
import sys
import os

class ClusterHandler():
    def __init__(self, db=None, Values=None, User=None, current_user=None):
        """
        Class: ClusterHandler manages the connections
               between the algorithms and databases

            constructor contains:
                -self.db            :'Connection to our sql database'
                -self.current_user  :'Info of current user on website'
                -self.User          :'Database table for all users'
                -self.Values        :'Database table for all values'
        ------
        Methods:
            -store_values       :'params:values'
            -create_datapoint   :'params:value1, value2, value3'
            -store-datapoint    :'params:datapoint'
            -get_datapoint      :'params:None'
            -get_centroids      :'params:None'
            -min_dist           :'params:datapoint, centroids'
            -All_cluster_no     :'params:None'
            -store_cluster      :'params:cluster_mapping'
            -One_cluster_no     :'params:datapoint, name'

        """
        self.db = db
        self.current_user = current_user
        self.User = User
        self.Values = Values

    def store_values(self, values):
        """
        Function: stores values in values table in database"
        -------
        Params:
            -values     :'[value1, value2, value3]'
        """
        updated = Values.query.filter_by(comp_name=self.current_user.username)
        updated.update(dict(value1=values[0], value2=values[1], value3=values[2]))
        self.db.session.commit()

    def create_datapoint(self, value1, value2, value3):
        """
        Function: Calculate mean of the value points
        load in WordVec values from /data/vectorized_words.json to process
        -------
        Params:
            -value1     :'WordVec'
            -value2     :'WordVec'
            -value3     :'WordVec'
        -------
        Returns: Datapoint
        """
        if sys.platform.startswith('win'):
            with open('Value-Connection/source/vcwebsite_v1.1/vcwebsite/data/vectorized_words.json', 'r') as f:
                vectorized_dict = json.load(f)

        else:
            with open(os.getcwd() + '/vcwebsite/data/vectorized_words.json', 'r') as f:
                vectorized_dict = json.load(f)

        values = [value1, value2, value3]
        datapoint = []
        for value in values:
            datapoint.append(list(vectorized_dict[value]))

        return np.mean(datapoint, axis=0)


    def store_datapoint(self, datapoint):
        """
        Function: Makes connection to database and update current users datapoints
        -------
        Params:
            -datapoint      :'list of datapoints [p1, p2, p2]'
        """
        updated = User.query.filter_by(username=self.current_user.username)
        updated.update(dict(datapoint1=datapoint[0], datapoint2=datapoint[1], datapoint3=datapoint[2]))
        self.db.session.commit()

    def get_datapoints(self):
        """
        Function: Makes connection to database and collects all datapoints from User table
        -------
        Returns: numpy array of all datapoints
        """
        datapoints = []
        # sql call to queue datapoints
        datapoint = self.db.session.execute("SELECT user.datapoint1, user.datapoint2, user.datapoint3 FROM User")
        for data in datapoint:
            datapoints.append(list(data)) # convert data tuple to list and append to datapoint

        return np.array(datapoints) # convert to np array

    def get_datapoints_w_username(self):
        """
        Function: Makes connection to database and collects all usernames and datapoints
        -------
        Returns: array with all user,datapoints like [['joop', 0.32, 0.42, 0.51],['henk', 0.30, 0.34, 0.80]]
        """
        datapoints = []
        # sql call to queue datapoints with username
        datapoint = self.db.session.execute("SELECT user.username, user.datapoint1, user.datapoint2, user.datapoint3 FROM User")
        for data in datapoint:
            datapoints.append(list(data))

        return np.array(datapoints)


    def get_centroids(self):
        """
        Function: Read cluster centroids from /data/cluster_centroids.csv
        -------
        Returns: all centroids as list
        """
        if sys.platform.startswith('win'):
            centroids = pd.read_csv('Value-Connection/source/vcwebsite_v1.1/vcwebsite/data/cluster_centroids.csv')
        else:
            centroids = pd.read_csv(os.getcwd() + '/vcwebstite/data/cluster_centroids.csv')

        centroids = centroids.values.tolist()
        centroids = [i[0].split(" ") for i in centroids]
        for idx1, c1 in enumerate(centroids):
            for idx2, c2 in enumerate(c1):
                centroids[idx1][idx2] = float(centroids[idx1][idx2])


        #logging can be removed later
        with open("log.txt", "a+") as f:
            f.write("centroids = " + str(centroids))

        return centroids


    def min_dist(self, datapoint, centroids):
        """
        Function: Calculate minimal distance between datapoint and each centroid
        -------
        Params:
            -datapoint      :'array for datapoint'
            -centroids      :'array of arrays for centroids (all cluster centroids)'
        -------
        Returns: minimal distance index (cluster_no)
        """
        distances = []

        for centre in centroids:
            distances.append(distance.euclidean(centre, datapoint))

        return distances.index(min(distances))

    # This function will create a dictionary which will map a dict of comp_names and cluster_centroids
    def All_cluster_no(self):
        """
        Function: Creates cluster mapping for all users using the min_dist method
        -------
        Returns: cluster mapping    {'name': centre_no}
        """
        # here all the pairs will be stored
        cluster_mapping = {}

        # here we get the datapoints
        datapoints = self.get_datapoints_w_username()
        # here we get the cluster centroids
        centroids = self.get_centroids()

        # Nested function to calculate distances

        for datapoint in datapoints:
            cluster_mapping[datapoint[0]] = self.min_dist(datapoint[1:], centroids)

        return cluster_mapping


    def store_cluster(self, cluster_mapping):
        """
        Function: Makes connection to database and update cluster in User column
        -------
        Params:
            -cluster_mapping        -{'name':centre_no}
        """
        for name, cluster_no in cluster_mapping.items():
            updated = User.query.filter_by(username=name)
            updated.update(dict(cluster=cluster_no))
            self.db.session.commit()


    def One_cluster_no(self, datapoint, name):
        """
        Function: Creates cluster mapping for current user using the min_dist method
        -------
        Params:
            -datapoint          :'current datapoint of user'
            -name               :'current username'
        """
        # here we handle the naming from current user
        name = str(name).split("'")
        name = name[1]

        centroids = self.get_centroids()
        clustermapping = {name:self.min_dist(datapoint, centroids)}
        self.store_cluster(cluster_mapping=clustermapping)
