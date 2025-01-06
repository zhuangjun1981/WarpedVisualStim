from WarpedVisualStim.DisplayLogAnalysis import DisplayLogAnalyzer

import argparse
from WarpedVisualStim.tools import FileTools as ft
parser = argparse.ArgumentParser(description='Posthoc analysis on display_log files') 
parser.add_argument('-i', '--input', help='<Required> Absolute path to display_log (.pkl) file', type=ft.validate_file, required=True)
args = parser.parse_args()

dla = DisplayLogAnalyzer(args.input)
stim_dict = dla.get_stim_dict()
pd_onsets_seq = dla.analyze_photodiode_onsets_sequential(stim_dict, pd_thr=-0.5)
pd_onsets_combined = dla.analyze_photodiode_onsets_combined(pd_onsets_seq)

print(pd_onsets_combined)