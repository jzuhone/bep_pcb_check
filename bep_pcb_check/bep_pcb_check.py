#!/usr/bin/env python

"""
========================
bep_pcb_check
========================

This code generates backstop load review outputs for checking the ACIS
DPA temperature 1DPAMZT.  It also generates DPA model validation
plots comparing predicted values to telemetry for the previous three
weeks.
"""
from __future__ import print_function

# Matplotlib setup                                                                                                                                              
# Use Agg backend for command-line (non-interactive) operation                                                                                                   
import matplotlib
matplotlib.use('Agg')

import numpy as np
import xija
import sys
from acis_thermal_check.main import ACISThermalCheck
from acis_thermal_check.utils import calc_off_nom_rolls, get_options
import os

model_path = os.path.abspath(os.path.dirname(__file__))

MSID = dict(bep_pcb='TMP_BEP_PCB')
# This is the Yellow High IPCL limit.
# 05/2014 - changed from 35.0 to 37.5
YELLOW = dict(bep_pcb=44.0)
# This is the difference between the Yellow High IPCL limit and 
# the Planning Limit. So the Planning Limit is YELLOW - MARGIN
#
# 12/5/13 - This value was changed from 2.5 to 2.0 to reflect the new 
# 1DPAMZT planning limit of 33 degrees C
# 05/19/14 this is changed from 2.0, to 3.0.  2 degress for the normal
#          padding for model error and an additional degree because
#          the total change is being done in increments. We will back
#          this off from 3 degrees to two after a few months trial 
#          testing.  So for now the planning limit will be 34.5 deg. C.
# 09/19/14 - Set MARGIN to 2.0 so that the Planning Limit is now 
#            35.5 deg. C
MARGIN = dict(bep_pcb=2.0)
# 12/5/13 - Likewise the 1DPAMZT validation limits were reduced to 2.0 
#           from 2.5 for the 1% and 99% quantiles
VALIDATION_LIMITS = {'TMP_BEP_PCB': [(1, 2.0),
                                       (50, 1.0),
                                       (99, 2.0)],
                     'PITCH': [(1, 3.0),
                               (99, 3.0)],
                     'TSCPOS': [(1, 2.5),
                                (99, 2.5)]
                     }
HIST_LIMIT = [20.]

def calc_model(model_spec, states, start, stop, T_bep=None, T_bep_times=None):
    model = xija.ThermalModel('bep_pcb', start=start, stop=stop,
                              model_spec=model_spec)
    times = np.array([states['tstart'], states['tstop']])
    model.comp['sim_z'].set_data(states['simpos'], times)
    model.comp['eclipse'].set_data(False)
    model.comp['tmp_bep_pcb'].set_data(T_bep, T_bep_times)
    model.comp['roll'].set_data(calc_off_nom_rolls(states), times)
    for name in ('ccd_count', 'fep_count', 'vid_board', 'clocking', 'pitch'):
        model.comp[name].set_data(states[name], times)

    model.make()
    model.calc()
    return model

bep_pcb_check = ACISThermalCheck("tmp_bep_pcb", "bep_pcb", MSID,
                                  YELLOW, MARGIN, VALIDATION_LIMITS,
                                  HIST_LIMIT, calc_model)

def main():
    opt, args = get_options("TMP_BEP_PCB", "bep_pcb", model_path)
    try:
        bep_pcb_check.driver(opt)
    except Exception as msg:
        if opt.traceback:
            raise
        else:
            print("ERROR:", msg)
            sys.exit(1)

if __name__ == '__main__':
    main()
