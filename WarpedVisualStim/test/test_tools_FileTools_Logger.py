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

        log_dict[5] = 'hello'
        log_dict['next_dict'] = {(3, 4): [1, 2, 3],
                                 'str_list': ['1', '2', '3']}
        log_dict['nan'] = np.nan
        log_dict['None'] = None
        log_dict['bool'] = [False, True]

        log_dict['third_dict'] = {'forth_dict': {'fifth_dict': {'a': 0, 0:'a'}}}

        # print(log_dict)
        # print(save_path)

        logger = gt.Logger(log_dict=log_dict, save_path=save_path)
        logger.save_log()
        logger.save_log()

        # _ = [os.remove(os.path.join(self.save_folder, f)) for f in
        #      os.listdir(self.save_folder) if 'test_log' in f and f[-5:] == '.hdf5']

    def test_save_locally_sparse_noise(self):

        lsn = stim.LocallySparseNoise(monitor=self.mon, indicator=self.ind,
                                      min_distance=20., background=0., coordinate='degree',
                                      grid_space=(10., 10.), probe_size=(10., 10.),
                                      probe_orientation=0., probe_frame_num=6, subregion=[-10., 10., 0., 30.],
                                      sign='ON', iteration=1, pregap_dur=0.1, postgap_dur=0.2,
                                      is_include_edge=True, repeat=1)

        seq_lsn, dict_lsn = lsn.generate_movie_by_index()

        save_path = os.path.join(self.save_folder, 'LSN_log.hdf5')
        logger = gt.Logger(log_dict=dict_lsn, save_path=save_path)
        logger.save_log()

        # _ = [os.remove(os.path.join(self.save_folder, f)) for f in
        #      os.listdir(self.save_folder) if 'LSN_log' in f and f[-5:] == '.hdf5']

    def test_save_log_uc(self):

        # Initialize UniformContrast object
        uc = stim.UniformContrast(monitor=self.mon, indicator=self.ind, duration=1., color=-1.)

        self.player.set_stim(uc)
        self.player.trigger_display()

        fns = [f for f in os.listdir(os.path.join(self.save_folder, 'visual_display_log'))
               if 'UniformContrast-MTest-Name-000-notTriggered-complete.hdf5' in f]

        for fn in fns:
            print('deleting {} ...'.format(fn))
            os.remove(os.path.join(self.save_folder, 'visual_display_log', fn))




