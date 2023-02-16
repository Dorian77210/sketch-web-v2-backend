import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import numpy as np
from io import StringIO

class DataFrameService:

    def kmeans(csvData, clusters: int):
        input_data = pd.read_csv(StringIO(csvData), sep=',')
        x_scaled = preprocessing.scale(input_data)

        k = KMeans(n_clusters=clusters, init="k-means++", n_init=10, max_iter=300)
        k.fit(x_scaled)

        result = {
            'centroids': np.array([k.cluster_centers_]).tolist(),
            'labels': np.array(k.labels_).tolist()
        }

        return result

    def elbowMethod(csvData, maxCluster: int):
        input_data = pd.read_csv(StringIO(csvData), sep=',')
        x_scaled = preprocessing.scale(input_data)

        result = {
            'clusters': [],
            'inertias': []
        }

        for i in range(1, maxCluster):
            kmeans = KMeans(i)
            kmeans.fit(x_scaled)
            result['clusters'].append(i)
            result['inertias'].append(kmeans.inertia_)

        return result
