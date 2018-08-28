# August 20th 2018
# Author: Samuel Salemi
# University of Guelph Masters Candidate
# This script is the main function for all OSIM scripts to date

import scaling
import IK
import ID
import SO
import prePlot
import plot
import readTRC
import RRA
import CMC
import directories
import JR

allDir = list(directories.main(directories))
paramsDir = allDir[1]
idResultsDir = allDir[7]
soResultsDir = allDir[8]
cmcResultsDir = allDir[10]
jrResultsDir = allDir[11]

scaling.scale()
# IK.inverseKinematics()
# ID.inverseDynamics()

# Static Optimization
"""
input parameters 
time - t0 & t1
"""
# t0 = 0
# t1 = 2
# SO.run(t0,t1)

# # readTRC.plot()
# RRA.reduceResidualActuators()
"""
inputs 
Knee, hip, ankle actuators
subresults directories for the above^
"""
knee = paramsDir + "/" + "cmcKneeActuators.xml"
hip = paramsDir + "/" + "cmcHipActuators.xml"
ankle = paramsDir + "/" + "cmcAnkleActuators.xml"
genCmc = paramsDir + "/" + "cmcActuators.xml"

kneeSubResults = cmcResultsDir + "/" + "knee"
hipSubResults = cmcResultsDir + "/" + "hip"
ankleSubResults = cmcResultsDir + "/" + "ankle"
genCmcResults = cmcResultsDir

cmcActuators = genCmc 
resultsDirectory = genCmcResults
# CMC.computedMuscleControl(cmcActuators,resultsDirectory)

"""
inputs
setup - staticOptimization, cmc 
resultsDirectory - soResultsDir, cmcResultsDir
"""
setupSoJr = paramsDir + "/" + "setupSoJr.xml"
setupCmcJr = paramsDir + "/" + "setupCmcJr.xml"
# JR.run(setupCmcJr,cmcResultsDir)

# Write excel file for dataman
"input parameters"
ID = idResultsDir + "/" + "subject01_walk1_id.sto"
SO = soResultsDir + "/" + "subject01_walk1_StaticOptimization_force.sto"
soJR = soResultsDir + "/" + "_Gait2354 Joint RXN_ReactionLoads.sto"
cmcJR = cmcResultsDir + "/" + "_Gait2354 Joint RXN_ReactionLoads.sto"
filename = ID

# Write Function
# prePlot.write(filename)
# Plotting Function 
# plot.run(filename)
