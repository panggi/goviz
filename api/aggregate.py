import pandas as pd
import numpy as np
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta
import sys

class Agg:
    def __init__(self):
        gojek = MongoClient().gojek
        self.data = pd.DataFrame(
                [c for c in gojek.clean.find({}, {
                    '_id': 0,
                    'cancelTime': 1,
                    'dispatchTime': 1,
                    'latOrigin': 1,
                    'longOrigin': 1
                    })])

        self.data['idTime'] = self.data.cancelTime.fillna(self.data.dispatchTime)
        self.data['isCancel'] = self.data.cancelTime.notnull()
        self.data.drop(['cancelTime', 'dispatchTime'], axis=1, inplace=True)
        self.data.dropna(how='any', inplace=True)

    def aggregate(self, req):
        lat0 = req['lat_from']
        long0 = req['long_from']
        lat1 = req['lat_to']
        long1 = req['long_to']
        time0 = req['time_from']
        time1 = req['time_to']
        cell = req['n_items']**0.5

        day = datetime(2015,11,23)
        start = day + timedelta(hours=time0)
        end = day + timedelta(hours=time1)
        df = self.data[(self.data.idTime > start) &
                (self.data.idTime < end) &
                (self.data.latOrigin > lat0) &
                (self.data.latOrigin < lat1) &
                (self.data.longOrigin > long0) &
                (self.data.longOrigin < long1)].copy()

        # compare each location to a grid and calc which cell it's closest to
        x = np.linspace(df.latOrigin.min(), df.latOrigin.max(), cell)
        y = np.linspace(df.longOrigin.min(), df.longOrigin.max(), cell)
        dx = np.abs(np.subtract.outer(df.latOrigin.values, x))
        dy = np.abs(np.subtract.outer(df.longOrigin.values, y))

        df['x'] = x[dx.argmin(axis=-1)]
        df['y'] = y[dy.argmin(axis=-1)]

        count = df.groupby(['x','y']).latOrigin.count()
        count[:] = (count.astype(float)/count.max())**0.2
        return [[k[0], k[1], v] for k, v in count.iteritems()]

