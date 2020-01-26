import WarpedVisualStim.StimulusRoutines as stim
from WarpedVisualStim.DisplayStimulus import DisplaySequence
from WarpedVisualStim.MonitorSetup import Monitor, Indicator

mon = Monitor(resolution=(1200, 1920), dis=15., mon_width_cm=52., mon_height_cm=32.)
ind = Indicator(mon)
uc = stim.UniformContrast(mon, ind, duration=10., color=-1.)
ss = stim.StimulusSeparator(mon, ind)
cs = stim.CombinedStimuli(mon, ind)
cs.set_stimuli([ss, uc, ss])
ds = DisplaySequence(log_dir='C:/data')
# ds = DisplaySequence(log_dir='/home/zhuangjun1981')
ds.set_stim(cs)
log_path, log_dict = ds.trigger_display()

# convert log to .nwb
import os
import WarpedVisualStim.DisplayLogAnalysis as dla
import NeuroAnalysisTools.NwbTools as nt
log_folder, log_fn = os.path.split(log_path)
log_nwb_path = os.path.splitext(log_path)[0] + '.nwb'
save_f = nt.RecordedFile(filename=log_nwb_path, identifier=os.path.splitext(log_fn)[0], description='')
stim_log = dla.DisplayLogAnalyzer(log_path)
save_f.add_visual_display_log_retinotopic_mapping(stim_log=stim_log)
save_f.close()
