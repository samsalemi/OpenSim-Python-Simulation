# June 11 2018
# Author: Samuel Salemi
# University of Guelph Masters Graduate
# The script runs inverse dynamics trials for the Gait2354 Model

def inverseDynamics():
    import os
    import re
    import shutil
    import opensim as osim
    import directories

    allDir = list(directories.main(directories))
    parentDir = allDir[0]
    paramsDir = allDir[1]
    subID = allDir[4]
    subResultsDir = allDir[5]
    ikResultsDir = allDir[6]
    idResultsDir = allDir[7]

    # Clear Inverse Dynamics Folder
    if os.path.exists(idResultsDir):
        shutil.rmtree(idResultsDir, ignore_errors=True)
    if not os.path.exists(idResultsDir):
        os.mkdir(idResultsDir)

    # Input data files
    genericExtLoads = paramsDir + "/externalLoads.xml"
    motData = parentDir + "/data/osDemo/subject01_walk1_grf.mot"
    motFileName = "subject01_walk1_grf.mot"
    # saveDir = subResultsDir + "/" + subID + "motionFile.mot"
    ikFileName = "subject01_walk1_ik.mot"
    ikFile = ikResultsDir + "/" + ikFileName

    # Copy GRF File over to Current Directory
    shutil.copy(motData, idResultsDir + "/" + motFileName)

    # Load Inverse Kinematics Model
    aModel = osim.Model(subResultsDir + "/" + subID + ".osim")

    # initialize system
    aModel.initSystem()

    # Initialize External Loads File from Generic File
    extLoads = osim.ExternalLoads(aModel, genericExtLoads)

    # Initialize idTool
    idTool = osim.InverseDynamicsTool()
    idTool.setLowpassCutoffFrequency(6.0)
    idTool.setInputsDir(idResultsDir)
    idTool.setResultsDir(idResultsDir)
    idTool.setModel(aModel)
    idTool.setModelFileName(subResultsDir + "/" + subID + ".osim")
    # Get .mot data to determine time range
    motCoordsData = osim.Storage(ikFile)
    # Get initial and final time
    initial_time = motCoordsData.getFirstTime()
    final_time = motCoordsData.getLastTime()

    # Creat output ID
    idFileName = re.sub('ik.mot', 'id.sto', ikFileName)
    # Customize and save external loads ile
    extLoads.setName(motFileName)
    extLoads.setDataFileName(motData)
    extLoads.setExternalLoadsModelKinematicsFileName(ikFile)
    extLoads.printToXML(idResultsDir + "/" +
                        re.sub('ik.mot', 'extLoads.xml', ikFileName))

    # Setup idTool
    idTool.setName(motFileName)
    idTool.setCoordinatesFileName(ikFile)
    idTool.setStartTime(initial_time)
    idTool.setEndTime(final_time)
    # Must be relative to output directory, not full path!
    idTool.setOutputGenForceFileName(idFileName)
    idTool.setExternalLoadsFileName(
        idResultsDir + "/" + re.sub('ik.mot', 'extLoads.xml', ikFileName))
    # Can comment out if not needed in GUI
    idTool.printToXML(idResultsDir + "/" +
                    re.sub('ik.mot', 'setupID.xml', ikFileName))

    # Run idTool
    idTool.run()
    os.system('cls' if os.name == 'nt' else 'clear')
    return()
