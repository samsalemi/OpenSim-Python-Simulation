# August 20th 2018
# Author: Samuel Salemi
# University of Guelph Masters Candidate
# This module runs a plotting program for several different OpenSim tools

def run(filename):
        
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    import directories

    allDir = list(directories.main(directories))
    idResultsDir = allDir[7]
    soResultsDir = allDir[8]
    cmcResultsDir = allDir[10]
    
# Plotting Function
# Plot Inverse Dynamincs STO file
    if filename == idResultsDir + "/" + "subject01_walk1_id.sto":
        data = idResultsDir + "/" + "idData.csv"
        df = pd.read_csv(data, usecols=['time', 'pelvis_tilt_moment',
                                        'pelvis_list_moment', 'pelvis_rotation_moment'], index_col='time')

        df.plot(title='Inverse Dynamics')
        fig = plt.gcf()
        plt.savefig(idResultsDir + "/" + "idFigure")

# Static Optimization
    if filename == soResultsDir + "/" + "subject01_walk1_StaticOptimization_force.sto":
        data = soResultsDir + "/" + "soData.csv"
        df = pd.read_csv(data, usecols=['time', 'glut_med1_r',
                                        'glut_med2_r', 'glut_med3_r'], index_col='time')
        df.plot(title='Static Optimization')
        fig = plt.gcf()
        fig.savefig(soResultsDir + "/" + "soFigure")

# Plot so Joint RXN Loading STO file
    if filename == soResultsDir + "/" + "_Gait2354 Joint RXN_ReactionLoads.sto":
        data = soResultsDir + "/" + "soJrData.csv"
        df = pd.read_csv(data, usecols=['time', 'ground_pelvis_on_pelvis_in_ground_fx',
                                        'ground_pelvis_on_pelvis_in_ground_fy', 'ground_pelvis_on_pelvis_in_ground_fz'], index_col='time')
        df.plot(title='Joint RXN Load')
        fig = plt.gcf()
        fig.savefig(soResultsDir + "/" + "soJrFigure")

# Plot so Joint RXN Loading STO file
    if filename == cmcResultsDir + "/" + "_Gait2354 Joint RXN_ReactionLoads.sto":
        data = cmcResultsDir + "/" + "cmcJrData.csv"
        df = pd.read_csv(data, usecols=['time', 'ground_pelvis_on_pelvis_in_ground_fx',
                                        'ground_pelvis_on_pelvis_in_ground_fy', 'ground_pelvis_on_pelvis_in_ground_fz'], index_col='time')
        df.plot(title='Joint RXN Load')
        fig = plt.gcf()
        fig.savefig(cmcResultsDir + "/" + "cmcJrFigure")


    os.system('cls' if os.name == 'nt' else 'clear')
    return()
