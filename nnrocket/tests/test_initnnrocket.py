# IBM Time Series Classification version 1.0.0
# IBM Confidential
# Copyright IBM Corp., 2021

import pathlib
import ray
import sys
from nnrocket.core.NNRocketRay import NNRocketPipeline

def test_create_default():
    length=1039
    dim = 10
    kernel_size_list=[7,9,11]
    stride_size_list=[1,2]
    kernel_num=20000
    RC = NNRocketPipeline(length,dim,kernel_num,kernel_size_list,stride_size_list)
    spec = RC.debug()

    assert len(spec) > 10

def test_create_jobliboption():
    length=139
    dim = 49
    kernel_size_list=[7,9,11]
    stride_size_list=[1,2]
    kernel_num=30000
    maxjoblibthreads = 10
    RC = NNRocketPipeline(length,dim,kernel_num,kernel_size_list,stride_size_list,maxjoblibthreads=maxjoblibthreads)
    spec = RC.debug()

    assert len(spec) > 10
