# August 6th 2018
# Author: Samuel Salemi
# University of Guelph Masters Graduate
# This module completes RRA for the model following Inverse Dynamics

import os
import opensim as osim
import sys
import shutil
import directories


def reduceResidualActuators():
    allDir = list(directories.main(directories))
    paramsDir = allDir[1]
    subID = allDir[4]
    subResultsDir = allDir[5]
    ikResultsDir = allDir[6]
    idResultsDir = allDir[7]
    rraResultsDir = allDir[9]

    # Input Files
    idData = idResultsDir + "/subject01_walk1_extLoads.xml"
    ikFileName = "subject01_walk1_ik.mot"
    ikFile = ikResultsDir + "/" + ikFileName

    # Set XML file Variables
    RRATasks = paramsDir + "/" + "RRATasks.xml"
    RRAActuatorsFile = paramsDir + "/" + "RRAActuators.xml"
    RRAActuators = "RRAActuators.xml"

    if os.path.exists(rraResultsDir):
        shutil.rmtree(rraResultsDir, ignore_errors=True)
    if not os.path.exists(rraResultsDir):
        os.mkdir(rraResultsDir)

    # Load Model
    aModel = osim.Model(subResultsDir + "/" + subID + ".osim")

    # initialize system
    aModel.initSystem()

    rraTool = osim.RRATool()
    rraTool.setModel(aModel)
    rraTool.setModelFilename(subID + ".osim")
    rraTool.setDesiredKinematicsFileName(ikFile)
    rraTool.setTaskSetFileName(RRATasks)
    rraTool.setExternalLoadsFileName(idData)
    rraTool.setStartTime(0.5)
    rraTool.setFinalTime(1.5)
    rraTool.setLowpassCutoffFrequency(6)

    # Force Set
    myForceSet = osim.ForceSet(aModel, RRAActuatorsFile)
    rraTool.setReplaceForceSet(False)
    shutil.copy(RRAActuatorsFile, rraResultsDir + "/" + RRAActuators)

    rraTool.setAdjustCOMToReduceResiduals(True)
    rraTool.setAdjustedCOMBody("torso")
    rraTool.setResultsDir(rraResultsDir)
    rraTool.setOutputModelFileName(rraResultsDir + "/" + subID + "_adjustedModel.osim")

    # Manually Replace Force Set
    modelForceSet = aModel.updForceSet()
    modelMuscles = osim.ForceSet(aModel.getForceSet())

    modelForceSet.clearAndDestroy()
    for i in range(myForceSet.getSize()):
        aModel.updForceSet().append(myForceSet.get(i))
    rraTool.run()


    rraTool.printToXML(rraResultsDir + "/" + "rraSetup.xml")

    rraModel = osim.Model(rraResultsDir + "/" + subID + "_adjustedModel.osim")
    rraModel.setName(subID + "_adjustedModel")

    rraModel.updForceSet().clearAndDestroy()
    for i in range(modelMuscles.getSize()):
        rraModel.updForceSet().append(modelMuscles.get(i))

    rraModel.printToXML(rraResultsDir + "/" + subID + "_adjustedModel.osim")

    return()
