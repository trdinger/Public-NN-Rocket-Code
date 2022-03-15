# IBM Time Series Classification version 1.0.0
# IBM Confidential
# Copyright IBM Corp., 2021

import sys
sys.path.append("../../")
from utils.limits import Limits

def test_get_env():
    l = Limits()
    env = l.get_env()
    assert env is not None

def test_get_memory_limits_gig():
    l = Limits()
    env = l.get_env()
    mem = l.get_memory_limits_gig(env)
    assert mem is not None

def test_get_cpu_limits_cores():
    l = Limits()
    env = l.get_env()
    cores = l.get_cpu_limits_cores(env)
    assert cores is not None

def test_get_gpu_limits_count():
    l = Limits()
    count = l.get_gpu_limits_count()
    assert count is not None

def test_get_gpu_memory_gig():
    l = Limits()
    mem = l.get_gpu_memory_gig()
    assert mem is not None

def test_get_limits():
    l = Limits()
    l_dict = l.get_limits()
    assert l_dict is not None


if __name__ == '__main__':
    test_get_env()
    test_get_memory_limits_gig()
    test_get_cpu_limits_cores()
    test_get_gpu_limits_count()
    test_get_gpu_memory_gig()
    test_get_limits()
