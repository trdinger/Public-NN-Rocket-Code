# IBM Time Series Classification version 1.0.0
# IBM Confidential
# Copyright IBM Corp., 2021

import pathlib
import ray
import sys
import pickle
import torch
import random
import numpy as np
from nnrocket.core.NNRocketRay import *
from utils.limits import *

def test_classification1():
    ray.shutdown()
    #ray.init(num_cpus=1)
    try:
        ray.init(address='auto')
    except ConnectionError:
        ray.init()

    seed = 0
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)

    current_dir=str(pathlib.Path().resolve())
    if "nnrocket" in current_dir:
        with open('../data/UEA-BasicMotions.pkl', 'rb') as f:
            (train_tensor,train_label,test_tensor,test_label)=pickle.load(f)
    else:
        with open(str(pathlib.Path().resolve())+'/nnrocket/data/UEA-BasicMotions.pkl', 'rb') as f:
            (train_tensor,train_label,test_tensor,test_label)=pickle.load(f)

    dim=train_tensor.shape[1]
    length=train_tensor.shape[2]
    kernel_size_list=[7,9,11]
    stride_size_list=[1,2]
    kernel_num=20000
    splits=1

    if str(ray.available_resources()).count('node:') > 2:
        # set maxjoblibthreads to the number of CPU cores
        limits = Limits()
        maxjoblibthreads=int(limits.get_cpu_limits_cores(limits.get_env()))
    else:
        #travis env, override maxjoblibthreads to 1
        maxjoblibthreads=1

    (seed, description, result, report, RC, classifier, xgbc)=rayenabled(seed,length,dim,kernel_num,kernel_size_list,
        stride_size_list,train_tensor,train_label,test_tensor,test_label,None,None,splits=splits,maxjoblibthreads=maxjoblibthreads)

    ray.shutdown()
    
    assert float(result) > 0.95

if __name__ == '__main__':
    test_classification1()
