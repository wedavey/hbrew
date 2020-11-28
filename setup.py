from setuptools import find_packages, setup
from glob import iglob
import os

# paths
TOPDIR = os.path.dirname(__file__)
HBREW = os.path.join(TOPDIR,'hbrew')
SCRIPTS = os.path.join(TOPDIR, 'scripts')
SHARE = os.path.join(HBREW, 'share')

# scripts
script_exts = ['*.py', '*.sh']
scripts = [p for ext in script_exts for p in
           iglob(os.path.join(SCRIPTS,'**',ext), recursive=True)]
# data
data_exts = ['*.py', '*.yml']
data = [os.path.relpath(f, HBREW) for ext in data_exts
        for f in iglob(os.path.join(SHARE,'**',ext),recursive=True)]

# requirements
install_requires=[
    "matplotlib",
    "numpy",
    "pandas",
    "pyyaml",
    "scikit-learn",
    "scipy",
    "seaborn",
    "ipykernel", 
    "ipython", 
    "jupyter", 
    "notebook"
]

setup(
    name='hbrew',
    description='Dominating brew plots n shit',
    long_description=open(os.path.join(TOPDIR, 'README.md')).read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wedavey/hbrew',
    author='Will Davey',
    author_email='wedavey@gmail.com',
    #license=None,
    packages=find_packages(include=['hbrew']),
    package_data={'hbrew':data},
    python_requires=">=3.7",
    install_requires=install_requires,
    #extras_require=extras_requires,
    scripts=scripts,
    version='0.1.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
