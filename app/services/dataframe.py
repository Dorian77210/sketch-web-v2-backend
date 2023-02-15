import pandas as pd
from sklearn.cluster import KMeans
import json
from pandas import json_normalize

import numpy as np

from io import StringIO

class DataFrameService:

    def kmeans(csvData, clusters: int):
        input_data = pd.read_csv(StringIO(csvData), sep=',')
        k = KMeans(n_clusters=clusters, init="k-means++", n_init=10, max_iter=300)
        k.fit(input_data.values)

        result = {
            'centroids': np.array([k.cluster_centers_]).tolist(),
            'labels': np.array([k.labels_]).tolist()
        }

        return result