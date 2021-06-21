from vcwebsite.models import User, Values
from vcwebsite import db
from vcwebsite.clustering.cluster import initialize_centroids
from vcwebsite.clustering.clusterhandler import ClusterHandler
from shutil import copyfile
import os
import sys
import numpy as np
import pandas as pd

# Todo change datahandler file name and Datahandler class name to administrator.
class Datahandler:
    def __init__(self):
        # Creates clusterhandler object so we can use its attributes
        # for training and storing/extracting content from database
        self.clusterhandler = ClusterHandler(db)

    def create_database(self):
        """Build all database tables"""
        db.create_all()

    def drop_database(self):
        """Drop all database tables"""
        db.drop_all()

    def remove_database(self):
        """Completely remove sqllite database from host"""
        if os.path.exists("site.db"):
            os.remove("site.db")
        else:
            print("database already removed")

    def make_backup(self):
        """Create a new backupfile call backupsite.db"""
        cwd = os.getcwd()
        if sys.platform.startswith('win'):
            copyfile(cwd + "\\Value-Connection\\source\\vcwebsite_v1.1\\vcwebsite\\site.db", cwd + "\\Value-Connection\\source\\vcwebsite_v1.1\\vcwebsite\\backupsite.db")

        else:
            copyfile(cwd + '/vcwebsite/site.db', cwd + '/vcwebsite/backupsite.db')


    def train_cluster_model(self):
        """Trains new centroids and stores them in /data/cluster_centroids.csv"""
        # Collect datapoints from database
        datapoints = self.clusterhandler.get_datapoints()

        data = initialize_centroids(datapoints)
        df = pd.DataFrame(data=data.astype(float))

        if sys.platform.startswith('win'):
            df.to_csv('Value-Connection/source/vcwebsite_v1.1/vcwebsite/data/cluster_centroids.csv', sep=' ', header=False, float_format='%.8f', index=False)
        else:
            df.to_csv(os.getcwd() + '/vcwebsite/data/cluster_centroids.csv', sep=' ', header=False, float_format="%.8f", index=False)

    # def update_user_clusters(self):
    #     datapoints = self.clusterhandler.get_datapoints_w_username()
    #     names = [x[0] for x in datapoints]
    #     datapoints = [x[1:] for x in datapoints]
    #     centroids = self.clusterhandler.get_centroids()
