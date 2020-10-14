# hbrew 

Dominating brew plots n shit

## Quick start

### Prerequisites 

- **conda** (anaconda / miniconda) - follow the 
[installation instructions](https://conda.io/docs/user-guide/install/index.html) 
for your platform and select python 3 version.

After installing update `conda` from the `conda-forge` repo: 
```
conda update conda -c conda-forge 
```

### Install

Fork [wedavey/hbrew](https://github.com/wedavey/hbrew) then install 
from github:
```bash
git clone git@github.com:<your-user-name>/hbrew.git
conda env create -f hbrew/env.yml -n hbrew
conda activate hbrew
cd hbrew; python setup.py develop
```

