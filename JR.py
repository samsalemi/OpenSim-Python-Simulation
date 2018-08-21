def run(setup,resultsDirectory):
    import os
    import re
    import shutil
    import opensim as osim
    import directories

    allDir = list(directories.main(directories))
    paramsDir = allDir[1]
    subID = allDir[4]
    subResultsDir = allDir[5]
    # ikResultsDir = allDir[6]
    # idResultsDir = allDir[7]
    # soResultsDir = allDir[8]
    # cmcResultsDir = allDir[10]
    # jrResultsDir = allDir[11]

    # # actuatorFile = paramsDir + "/soActuators.xml"
    # # genericSetupSO = paramsDir + "/" + "setupSO.xml"
    # ikFileName = "subject01_walk1_ik.mot"
    # ikFile = ikResultsDir + "/" + ikFileName
    # # soForces = soResultsDir + "/" + "subject01_walk1_StaticOptimization_force.sto"
    # if os.path.exists(jrResultsDir):
    #     shutil.rmtree(jrResultsDir, ignore_errors=True)
    # if not os.path.exists(jrResultsDir):
    #     os.mkdir(jrResultsDir)

    # # Load Model
    aModel = osim.Model(subResultsDir + "/" + subID + ".osim")
    # # initialize system
    aModel.initSystem()
    # # Initialize External Loads File from Generic File
    # extLoads = idResultsDir + "/subject01_walk1_extLoads.xml"
    # # Get .mot data to determine time range
    # motCoordsData = osim.Storage(ikFile)
    # # Get initial and final time
    # initial_time = motCoordsData.getFirstTime()
    # final_time = motCoordsData.getLastTime()

    # Analyze Tool Setup for Static Optimization
    analyzeTool = osim.AnalyzeTool(setup)
    analyzeTool.setModel(aModel)
    analyzeTool.setResultsDir(resultsDirectory)
    analyzeTool.run()

    # analyzeTool = osim.AnalyzeTool(cmcJrSetup)
    # analyzeTool.setExternalLoadsFileName(extLoads)
    # analyzeTool.setInitialTime(initial_time)
    # analyzeTool.setFinalTime(final_time)
    # analyzeTool.setLowpassCutoffFrequency(6)
    # analyzeTool.setOutputPrecision(20)

    # myForceSet = osim.ForceSet(aModel, actuatorFile)
    # for i in range(myForceSet.getSize()):
    #     aModel.updForceSet().append(myForceSet.get(i))
    # print(aModel.getForceSet().getSize())

    # analysisSet = analyzeTool.getAnalysisSet()
    # myForceSetArray = analyzeTool.getForceSetFiles()
    # myForceSetArray.set(0, "")
    # analyzeTool.setReplaceForceSet(False)
    # analyzeTool.setForceSetFiles(myForceSetArray)

    # # Joint Reaction Analysis
    # jrTool = osim.JointReaction(jrSetup)
    # analysisSet.cloneAndAppend(jrTool)

    # # Set coordinates
    # coordtype = "mot"
    # if coordtype == "mot":
    #     analyzeTool.setStatesFileName("")
    #     analyzeTool.setCoordinatesFileName(ikFile)
    # elif coordtype == "states":
    #     analyzeTool.setStatesFileName(ikFile)
    #     analyzeTool.setCoordinatesFileName("")

    # analyzeTool.verifyControlsStates()
    # analyzeTool.setResultsDir(jrResultsDir)
    # # analyzeTool.printToXML(paramsDir +"/setupJR.xml")
    # analyzeTool.run()
    return()
    os.system('cls' if os.name == 'nt' else 'clear')
