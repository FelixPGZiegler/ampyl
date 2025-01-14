[![Build/Test](https://github.com/mthansen/ampyl/workflows/Build/Test/badge.svg)](https://github.com/mthansen/ampyl/actions?query=workflow%3ABuild%2FTest)
![Build Doc](https://github.com/mthansen/ampyl/workflows/Build%20Doc/badge.svg)
[![codecov](https://codecov.io/gh/mthansen/ampyl/branch/main/graph/badge.svg?token=IR43OJAV6T)](https://codecov.io/gh/mthansen/ampyl)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<img src="/doc/ampyl-logo.png" width="25%">

A Python package to relate finite-volume data to amplitudes.

The name AmPyL ("am-pie-ell") stands for **Am**plitdues via **Py**thon from finite-volume (**L**). The package requires python version 3.8.x or newer.

- **Website:** https://github.com/mthansen/ampyl
- **Documentation:** https://mthansen.github.io/ampyl/
- **Examples:** [tutorials](./tutorials)
- **Bug reports:** https://github.com/mthansen/ampyl/issues

### Authors

Copyright (C) 2022, Maxwell T. Hansen

## Installation

The NumPy package is required to use AmPyL. The latest version AmPyL can be installed locally, e.g. using `pip`:

```python
git clone https://github.com/mthansen/ampyl
cd ampyl
pip install .

python
import numpy
import ampyl
```

## Example

```python
import numpy as np
import ampyl

# single 3-particle channel
fc = ampyl.FlavorChannel(3)
fcs = ampyl.FlavorChannelSpace(fc_list=[fc])
fvs = ampyl.FiniteVolumeSetup()
tbis = ampyl.ThreeBodyInteractionScheme()

qcis = ampyl.QCIndexSpace(fcs=fcs, fvs=fvs,
                          tbis=tbis,
                          Emax=5.0, Lmax=6.0)
qc = ampyl.QC(qcis=qcis)

k_params = qcis.default_k_params()
# k_params default is [[[0.0]], [0.0]]
# first entry is the scattering length
# second entry is kdf (3-body
# interaction):
k_params[0][0][0] = 0.1
qc.get_value(E=3.03181, L=5.0,
             k_params=k_params,
             irrep=('A1PLUS', 0))
qc.get_value(E=3.03182, L=5.0,
             k_params=k_params,
             irrep=('A1PLUS', 0))
# Returns small values with opposite signs,
# indicating the solution is between the
# energies provided.
```
