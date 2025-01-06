# -*- coding: utf-8 -*-
"""
the minimum script to run 10 seconds of black screen
"""

import matplotlib.pyplot as plt
import WarpedVisualStim.StimulusRoutines as stim
from WarpedVisualStim.MonitorSetup import Monitor, Indicator
from WarpedVisualStim.DisplayStimulus import DisplaySequence

# Initialize Monitor object
mon = Monitor(resolution=(1200, 1920), dis=15., mon_width_cm=52., mon_height_cm=32.)
ind = Indicator(mon)
ds = DisplaySequence(log_dir='C:/data', is_by_index=True, display_screen=1)
dgc = stim.DriftingGratingMultipleCircle(monitor=mon, indicator=ind, background=0.,
                                 coordinate='degree', center_list=[(10., 90.),(0., 80.)], sf_list=(0.02,),
                                 tf_list=(4.0, 2.0), dire_list=(45.,), con_list=(0.8,), radius_list=(20.,),
                                 block_dur=2., midgap_dur=1., iteration=3, pregap_dur=2.,
                                 postgap_dur=3., is_blank_block=True, is_random_start_phase=False)
ds.set_stim(dgc)
ds.trigger_display()
plt.show()