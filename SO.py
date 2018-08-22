# June 19 2018
# Author: Samuel Salemi
# University of Guelph Masters Candidate
# The script runs Static Optimization trials for the Gait2354 Model.


def run(initial_time, final_time):
    """
    inputs
    initial time 
    final time
    actuator file = soActuators
    kinematics file = subject01_walk1_ik.mot

    outputs
    

    """

    import os
    import re
    import shutil
    import opensim as osim
    import directories

    allDir = list(directories.main(directories))
    paramsDir = allDir[1]
    subID = allDir[4]
    subResultsDir = allDir[5]
    ikResultsDir = allDir[6]
    idResultsDir = allDir[7]
    soResultsDir = allDir[8]

    actuatorFile = paramsDir + "/soActuators.xml"
    genericSetupSO = paramsDir + "/" + "setupSO.xml"
    ikFileName = "subject01_walk1_ik.mot"
    ikFile = ikResultsDir + "/" + ikFileName

    if os.path.exists(soResultsDir):
        shutil.rmtree(soResultsDir, ignore_errors=True)
    if not os.path.exists(soResultsDir):
        os.mkdir(soResultsDir)

    # Load Model
    aModel = osim.Model(subResultsDir + "/" + subID + ".osim")
    pelvisIndex = aModel.getBodySet().getIndex("pelvis")
    pelvisCOM_Vec3 = osim.Vec3()
    aModel.getBodySet().get(pelvisIndex).getMassCenter(pelvisCOM_Vec3)

    # add reserve actuators
    myForceSet = osim.ForceSet(aModel, actuatorFile)
    # print(aModel.getForceSet().getSize())

    FX = osim.PointActuator.safeDownCast(myForceSet.get(0))
    FX.set_point(pelvisCOM_Vec3)
    FY = osim.PointActuator.safeDownCast(myForceSet.get(1))
    FY.set_point(pelvisCOM_Vec3)
    FZ = osim.PointActuator.safeDownCast(myForceSet.get(2))
    FZ.set_point(pelvisCOM_Vec3)

    for i in range(myForceSet.getSize()):
        aModel.updForceSet().append(myForceSet.get(i))
    print(aModel.getForceSet().getSize())

    # initialize system
    aModel.initSystem()
    # Initialize External Loads File from Generic File
    extLoads = idResultsDir + "/subject01_walk1_extLoads.xml"

    # Get .mot data to determine time range
    # motCoordsData = osim.Storage(ikFile)

    # Get initial and final time
    # initial_time = motCoordsData.getFirstTime()
    # final_time = motCoordsData.getLastTime()

    # Analyze Tool Setup
    analyzeTool = osim.AnalyzeTool(genericSetupSO)
    analyzeTool.setInitialTime(initial_time)
    analyzeTool.setFinalTime(final_time)
    analyzeTool.setResultsDir(soResultsDir)
    analyzeTool.setModelFilename("")
    analyzeTool.setName(re.sub('_ik.mot', '', ikFileName))
    myForceSetArray = analyzeTool.getForceSetFiles()
    myForceSetArray.set(0, "")
    analyzeTool.setReplaceForceSet(False)
    analyzeTool.setForceSetFiles(myForceSetArray)

    # Set coordinates
    coordtype = "mot"
    if coordtype == "mot":
        analyzeTool.setStatesFileName("")
        analyzeTool.setCoordinatesFileName(ikFile)
    elif coordtype == "states":
        analyzeTool.setStatesFileName(ikFile)
        analyzeTool.setCoordinatesFileName("")

    analyzeTool.setExternalLoadsFileName(extLoads)
    analyzeTool.setModel(aModel)
    analyzeTool.run()

    analyzeTool.printToXML(soResultsDir + "/" +
                           re.sub('ik.mot', 'outSetupSO.xml', ikFileName))
    aModel.printToXML(soResultsDir + "/" + subID + "_soActuators.osim")
    os.system('cls' if os.name == 'nt' else 'clear')
    return()
