import WarpedVisualStim.StimulusRoutines as stim
from WarpedVisualStim.DisplayStimulus import DisplaySequence
from WarpedVisualStim.MonitorSetup import Monitor, Indicator

mon = Monitor(resolution=(1200, 1920), dis=15., mon_width_cm=52., mon_height_cm=32.)
ind = Indicator(mon)
uc = stim.UniformContrast(mon, ind, duration=10., color=-1.)
ss = stim.StimulusSeparator(mon, ind)
cs = stim.CombinedStimuli(mon, ind)
cs.set_stimuli([ss, uc, ss])
# ds = DisplaySequence(log_dir='C:/data')
ds = DisplaySequence(log_dir='~')
ds.set_stim(cs)
ds.trigger_display()