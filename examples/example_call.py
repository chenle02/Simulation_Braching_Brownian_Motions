#!/usr/bin/env python3
#
# By Le Chen
# chenle02@gmail.com / le.chen@auburn.edu
# Created at Fri Jan 26 11:36:39 AM EST 2024
#

import simulation_super_brownian_motions.super_bm_simulation as sbm

# Create an instance of the class
instance = sbm.Branching_BM()

# Use the instance and its methods
instance.simulate()
instance.plot_paths()
