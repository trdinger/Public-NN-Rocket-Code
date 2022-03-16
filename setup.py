import os
import sys

from glob import glob
from setuptools import setup

long_description = '''The NNRocketRay library provides facilities for defining and running parallel 
NN-Rocket pipelines on top of Ray. The goal of this project is to provide a fast NN algorithm for representation learning of 
time series data sets to IBM external users.  For the full documentation see
[https://github.ibm.com/IBM-Research-AI/NN-Rocket_Early_Access](https://github.ibm.com/IBM-Research-AI/NN-Rocket_Early_Access).
'''

here = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(here, 'nnrocket', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup(
    name='NNRocket_Early_Access',
    version=version_ns['__version__'],
    packages=['nnrocket', 'nnrocket.core', 'nnrocket.tests'],
    install_requires=[
#        'ray[default,serve,k8s]>=1.3.0',
#        'setuptools>=52.0.0',
#        'sklearn>=0.0',
#        'scikit-learn>=0.24.1',
#        'pandas>=1.2.4',
#        'numpy>=1.18.5',
#        'pickle5>=0.0.11', 
#        'graphviz>=0.16',
    ],
    url='https://github.ibm.com/IBM-Research-AI/NN-Rocket_Early_Access',
    license='IBM',
    author='Representation Learning Team',
    author_email='dinger@us.ibm.com',
    description='NN-Rocket on Ray pipelines',
    python_requires='>=3.8',
    keywords=("ray pipelines"),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: IBM License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
        'Topic :: System :: Distributed Computing',
    ],
    project_urls={
        'Bug Reports': 'https://github.ibm.com/IBM-Research-AI/NN-Rocket_Early_Access/issues',
        'Source': 'https://github.ibm.com/IBM-Research-AI/NN-Rocket_Early_Access',
    },
)
