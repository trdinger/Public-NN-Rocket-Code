# IBM Time Series Classification version 1.0.0
# IBM Confidential
# Copyright IBM Corp., 2021

import ray
import torch
import time

@ray.remote
def increment(x):
    return x + 1

def test_getput():
    ray.shutdown()
    ray.init()
    
    torcharray = torch.ones((100, 10, 200))
    objref = ray.put(torcharray)
    time.sleep(0.5)
    arrayfromray = ray.get(objref)

    ray.shutdown()
    assert torcharray.shape==arrayfromray.shape

def test_remotetask():
    ray.shutdown()
    ray.init()

    x = 100
    y = ray.get(increment.remote(x))
    
    ray.shutdown()
    assert y==x+1
