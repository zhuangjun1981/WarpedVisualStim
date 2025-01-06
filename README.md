# WarpedVisualStim package
  
by Jun Zhuang
&copy; 2019 Allen Institute
email: junz&lt;AT&gt;alleninstitute&lt;DOT&gt;org
  
The WarpedVisualStim package is a self-contained module
for display spherically corrected visual stimuli on a flat
screen in visual physiology experiments. It is a wrapper of 
the "[psychopy](https://www.psychopy.org/)" package.
  
The visual stimuli generation and display is implemented in the modules
`MonitorSetup.py`, `StimulusRoutines.py` and `DisplayStimulus.py`.
These modules allow you to display flashing circle, sparse noise,
locally sparse noise, drifting grading circle, static grading circle
and others with spherical correction. The method for spherical
correction is the same as Marshel et al. 2011 (2). These stimulus
routines are highly customizable and designed to give the user
significant flexibility and control in creative experimental design.
  
It can also interact with a National Instrument equipment to receive 
trigger and emit timing signals.
  
Please check the '\examples' folder for
example scripts of visual stimulation.

### Contributors:
* Jun Zhuang @zhuangj
* John Yearseley @yearsj
* Derric Williams @derricw
* Sumiya Kuroda @sumiya-kuroda

### Level of support
We are planning on occasional updating this tool with no fixed schedule. Community involvement is encouraged through both issues and pull requests.

#### Language:

1. python 3.7


#### Install:
```
cd <package_path>
conda env create --name warpedvisualstim python=3.7
activate warpedvisualstim (Windows)
source activate warpedvisualstim (Mac or Linux)
python setup.py install
pip install psychopy
pip install pytest
```


#### Dependencies:
1. pytest
2. numpy
3. scipy
4. matplotlib
5. h5py
6. pillow
7. psychopy
8. pyglet
9. OpenCV
10. scikit-image
11. tifffile
12. PyDAQmx
13. configobj
14. sphinx, version 1.6.3 or later (just for documentation)
15. numpydoc, version 0.7.0 (just for documentation)

for detailed installation instructions see the
install page in documentation (`doc` branch).

#### Issues:

1. Most image analysis parameters are defined as number of pixels, not microns.
2. Works in windows, but not fully tested on Mac and Linux.