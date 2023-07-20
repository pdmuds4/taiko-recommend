import scipy.spatial.distance as distance
from scipy.stats import rankdata
import numpy as np
from var import Var
from db import DB 
from dataaccess import DataAccess


def tovector(columns):
    return [list(i[1:6]) for i in columns]
    

def dist(input, other, rank):
    input_v = np.array(tovector(input))[0]
    other_v = np.array(tovector(other))
    dists = np.array([distance.euclidean(input_v, o) for o in other_v])
    rank_index = [np.where(rankdata(dists)==r+1)[0][0] for r in range(rank)]
    return rank_index
    

def result(rank, title, master=False, level=None):
    da = DataAccess()
    input = da.get_song(title, master, level)
    other = da.get_other(title)
    rank_index = dist(input, other, rank)
    return [other[i] for i in rank_index]


# if __name__ =="__main__":
#     a = DataAccess
#     print(result(5, 'Vixtory', master=True))



        


