# DRA-coupling

Electrophysiological recordings reveal photoreceptor coupling in the dorsal rim areas of honeybee and bumblebee eyes
====================
This repository contains files relevant to the manuscript ["_Electrophysiological recordings reveal photoreceptor coupling in the dorsal rim areas of honeybee and bumblebee eyes FAKE LINK_"](https://biorxiv/fake_link) by George Kolyfetis, Gregor Belušič and James Foster (2025).
The source code is [electrophysiology analysis FAKE LINK](https://github.com/JJFosterLab/DRA-coupling/tree/master/elphys_scripts), written in ```Python``` by George Kolyfetis.  Raw data (```.wcp``` files) and analysis are available from [Figshare](https://doi.org/10.6084/m9.figshare.28890938.v1). 
### Contributions:
All scripts written by GE Kolyfetis. Data collected by G Belušič. All analysis performed by GE Kolyfetis.

# File Manifest
## [WCP file processing FAKE LINK](https://github.com/JJFosterLab/DRA-coupling/tree/master/elphys_scripts/WCP_file_processing)
Scripts for organisation, plotting and analysis of raw millivolt data recorded to WCP files during electrophysiological experiments.  ```import_wcp_split_DNmodel.py```, ```responses_localmaxima.py``` and ```stavenga_spec_sensitivities.py``` process raw data according to relevant experimental conditions.
## [Hill curve transformation FAKE LINK](https://github.com/JJFosterLab/DRA-coupling/tree/master/elphys_scripts/Hill_curve_transformation)
Scripts for converting raw millivolt data  to sensitivity.
```hill_transformation_pol_sensitivity.py```, ```hill_transformation_spec_sensitivity``` and ```hill_transformation_contour_likelihood_gaussians.py```.
## ETC
[Statistical Analysis scripts FAKE LINK](https://github.com/JJFosterLab/DRA-coupling/tree/master/elphys_scripts/Statistical_Analyses)
These scripts were used for all statistical analyses.
```2_way_ANOVA_ShapiroWilk_TukeyHSD_KruskalWallis_Dunns.py```, ```FWHM_vs_polsens_model_table.py```
[Visualization scripts FAKE LINK](https://github.com/JJFosterLab/DRA-coupling/tree/master/elphys_scripts/Visualization)
These scripts were used only for data visualization.
```FWHM_vs_polsens.py```, ```cos2_pol_sensitivities_multiple.py```, ```boxplot_polsens_FHM.py```, ```heatmap_delays_smoothed_opacity.py```

# System Requirements
## Hardware requirements
Requires only a standard computer with enough RAM to support the in-memory operations.

## Software requirements
### OS Requirements
All analysis was performed on *Linux 20.04*

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
