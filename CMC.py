import os
import opensim as osim
import sys
import shutil
import directories

def computedMuscleControl():
    allDir = list(directories.main(directories))
    paramsDir = allDir[1]
    subID = allDir[4]
    subResultsDir = allDir[5]
    ikResultsDir = allDir[6]
    idResultsDir = allDir[7]
    rraResultsDir = allDir[9]
    cmcResultsDir = allDir[10]
    # Input Files
    idData = idResultsDir + "/subject01_walk1_extLoads.xml"
    rraKinematics = rraResultsDir + "/" + "_kinematics_q.sto"
    adjustedModel = rraResultsDir + "/" + subID + "_adjustedModel.osim"
    # Set XML file Variables
    cmcTasks = paramsDir + "/" + "cmcTasks.xml"
    cmcActuators = paramsDir + "/" + "cmcActuators.xml"
    cmcControlConstraints = paramsDir + "/" + "cmcControlConstraints.xml"
    osimGUI = paramsDir + "/" + "osimGUI.xml"
    if os.path.exists(cmcResultsDir):
        shutil.rmtree(cmcResultsDir, ignore_errors=True)
    if not os.path.exists(cmcResultsDir):
        os.mkdir(cmcResultsDir)

    # Load Model
    aModel = osim.Model(adjustedModel)

    # initialize system
    aModel.initSystem()

    cmcTool = osim.CMCTool()
    cmcTool.setModel(aModel)
    cmcTool.setModelFilename(subID + ".osim")
    cmcTool.setDesiredKinematicsFileName(rraKinematics)
    cmcTool.setTaskSetFileName(cmcTasks)
    cmcTool.setExternalLoadsFileName(idData)
    cmcTool.setConstraintsFileName(cmcControlConstraints)
    cmcTool.setStartTime(0.8)
    cmcTool.setFinalTime(1.2)
    cmcTool.setLowpassCutoffFrequency(-1)
    cmcTool.setMaxDT(1)
    cmcTool.setMinDT(0.0000000001)
    cmcTool.setErrorTolerance(0.00001)

    # Force Set
    myForceSet = osim.ForceSet(aModel, cmcActuators)
    cmcTool.setReplaceForceSet(False)
    cmcTool.setResultsDir(cmcResultsDir)

    # Manually append Force Set
    modelForceSet = aModel.updForceSet()
    for i in range(myForceSet.getSize()):
        aModel.updForceSet().append(myForceSet.get(i))

    cmcTool.run()
    cmcTool.printToXML(cmcResultsDir + "/" + "cmcSetup.xml")
    return()
