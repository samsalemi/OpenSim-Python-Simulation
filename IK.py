# June 11 2018
# Author: Samuel Salemi
# The script runs inverse kinematics trials for the Gait2354 Model.
# Inverse Kinematics Following Scaling

def inverseKinematics():
    import os
    import re
    import shutil
    import opensim as osim
    import directories

    # Global Directories
    allDir = list(directories.main(directories))
    parentDir = allDir[0]
    paramsDir = allDir[1]
    subID = allDir[4]
    subResultsDir = allDir[5]
    ikResultsDir = allDir[6]

    # Clear Inverse Kinematics Folder
    if os.path.exists(ikResultsDir):
        shutil.rmtree(ikResultsDir, ignore_errors=True)
    if not os.path.exists(ikResultsDir):
        os.mkdir(ikResultsDir)

    # Input settings File
    genericSettings = paramsDir + "/setupIK.xml"

    # Input trc File
    dataFiles = parentDir + "/data/osDemo"
    ikMarkerFileName = "subject01_walk1.trc"
    ikMarkerFile = dataFiles + "/" + ikMarkerFileName
    shutil.copy(ikMarkerFile, ikResultsDir + "/" + ikMarkerFileName)

    # Load scaled Model
    aModel = osim.Model(subResultsDir + "/" + subID + ".osim")

    # Import Inverse Kinematics Tool
    ikTool = osim.InverseKinematicsTool(genericSettings)

    # Tell IK tool to use loaded model
    ikTool.setModel(aModel)

    # Get scaled marker file + data
    markerData = osim.MarkerData(ikMarkerFile)
    # Get Initial and Final Time
    initial_time = markerData.getStartFrameTime()
    final_time = markerData.getLastFrameTime()
    # set IK tool for this trial
    ikName = re.sub('.trc', '', ikMarkerFileName)

    ikTool.setName(ikName)
    ikTool.setMarkerDataFileName(ikMarkerFile)
    ikTool.setStartTime(initial_time)
    ikTool.setEndTime(final_time)
    ikTool.setOutputMotionFileName(ikResultsDir + "/" + ikName + "_ik.mot")

    # Run IK
    ikTool.run()
    ikTool.printToXML(ikResultsDir + "/" + "setupIK.xml")
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    return()