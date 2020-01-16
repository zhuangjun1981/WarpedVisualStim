import os
import unittest
import shutil
import numpy as np
# from ..tools import FileTools as gt

import WarpedVisualStim.tools.FileTools as gt
import WarpedVisualStim.StimulusRoutines as stim
import WarpedVisualStim.MonitorSetup as ms
import WarpedVisualStim.DisplayStimulus as ds


class TestLogger(unittest.TestCase):

    def setUp(self):

        self.curr_folder = os.path.dirname(os.path.realpath(__file__))

        self.save_folder = os.path.join(self.curr_folder, 'test_data')

        # Initialize Monitor object
        self.mon = ms.Monitor(resolution=(1200, 1920), dis=15., mon_width_cm=52., mon_height_cm=32.)

        # Initialize Inicator object
        self.ind = ms.Indicator(self.mon)

        # Initialize DisplaySequence object
        self.player = ds.DisplaySequence(log_dir=self.save_folder)

    def test_save_log(self):
        save_path = os.path.join(self.save_folder, 'test_log.hdf5')
        log_dict = {}
        logger = gt.Logger(log_dict=log_dict, save_path=save_path)
        logger.save_log()
        logger.save_log()

        _ = [os.remove(os.path.join(self.save_folder, f)) for f in
             os.listdir(self.save_folder) if 'test_log' in f and f[-5:] == '.hdf5']

    def test_save_log_uc(self):

        # Initialize UniformContrast object
        uc = stim.UniformContrast(monitor=self.mon, indicator=self.ind, duration=10., color=-1.)
