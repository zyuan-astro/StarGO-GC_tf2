import numpy as np
from math import *

                          
                            

def normalization(inputs):

    inputs_norm = np.empty_like(inputs)
    
    for i in range(inputs.shape[1]):
        
        norm_range = np.max(inputs[:,i])-np.min(inputs[:,i])
        inputs_norm[:,i] = (inputs[:,i]-np.min(inputs[:,i]))/norm_range
        
        
    return inputs_norm





def normalization_2sigma(inputs):

    inputs_norm = np.empty_like(inputs)
    for i in range(inputs.shape[1]):
        
        norm_range = np.percentile(inputs[:,i],97.5)-np.percentile(inputs[:,i],2.5)
        inputs_norm[:,i] = (inputs[:,i]-np.percentile(inputs[:,i],2.5))/norm_range
        
        
    return inputs_norm




def normalization_3sigma(inputs):

    inputs_norm = np.empty_like(inputs)
    for i in range(inputs.shape[1]):
        
        norm_range = np.percentile(inputs[:,i],99.85)-np.percentile(inputs[:,i],0.15)
        inputs_norm[:,i] = (inputs[:,i]-np.percentile(inputs[:,i],0.15))/norm_range
        
        
    return inputs_norm








