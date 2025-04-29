# DRA-coupling

Electrophysiological recordings reveal photoreceptor coupling in the dorsal rim areas of honeybee and bumblebee eyes
====================
This repository contains files relevant to the manuscript ["_Electrophysiological recordings reveal photoreceptor coupling in the dorsal rim areas of honeybee and bumblebee eyes FAKE LINK_"](https://biorxiv/fake_link) by George Kolyfetis, Gregor Belušič and James Foster (2025).
The source code is [electrophysiology analysis FAKE LINK](https://github.com/JJFosterLab/DRA-coupling/tree/master/elphys_scripts), written in ```Python``` by George Kolyfetis.  Raw data (```.wcp``` files) and analysis are available from [Figshare](https://doi.org/10.6084/m9.figshare.28890938.v1). 
### Contributions:
All scripts written by GE Kolyfetis. Data collected by G Belušič. All analysis performed by GE Kolyfetis.

# File Manifest
## [WCP file processing FAKE LINK](https://github.com/JJFosterLab/DRA-coupling/tree/master/elphys_scripts/WCP_file_processing)
Scripts for organisation, plotting and analysis of raw millivolt data recorded to WCP files during electrophysiological experiments.  ```import_wcp.py```, ```import_wcp_split.py```, ```import_wcp_DNmodel.py``` and ```import_wcp_split_gaussian.py``` process raw data according to relevant experimental conditions.
## [Hill curve transformation FAKE LINK](https://github.com/JJFosterLab/DRA-coupling/tree/master/elphys_scripts/Hill_curve_transformation)
Scripts for converting raw millivolt data  to sensitivity.
```hill_transformation_pol_sensitivity.py``` and ```hill_transformation_contour_likelihood_gaussians.py```.
## ETC
More types of script.

# System Requirements
## Hardware requirements
Requires only a standard computer with enough RAM to support the in-memory operations.

## Software requirements
### OS Requirements
All analysis was performed on *Linux*: _Whatever version George uses_

### Package Dependencies

```
neo
scipy
statsmodels
Matplotlib
numpy
pandas
seaborn
mpl_toolkits
subprocess
skimage
os
sys
```

# Installation Guide:

### Install from Github
```
git clone https://github.com/JJFosterLab/DRA-coupling
```
