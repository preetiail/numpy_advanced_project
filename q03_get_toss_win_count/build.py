# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution


def get_toss_win_count(team):
    i1=ipl_matches_array[ipl_matches_array[:,5]==team]
    #result=np.bincount(np.unique(i1[:,0]).astype(int))     
    result=np.count_nonzero(np.unique(i1[:,0]))
    return result



