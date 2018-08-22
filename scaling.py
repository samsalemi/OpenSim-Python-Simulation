# June 7 2018
# Author: Samuel Salemi
# University of Guelph Masters Candidate
# This script determines scaling factors and places them on model Gait2354


def scale():
    import os
    import opensim as osim
    import shutil
    import directories
    
    # Global Directories
    allDir = list(directories.main(directories))
    parentDir = allDir[0]
    paramsDir = allDir[1]
    genericDir = allDir[2]
    subID = allDir[4]
    subResultsDir = allDir[5]

    # Get generic Model
    genericModel = "gait2354_LockedJoints.osim"
    genericModelFile = genericDir + "/" + genericModel

    if not os.path.exists(subResultsDir):
        os.mkdir(subResultsDir)

    # generic input XML files
    scaleSetupFull = paramsDir + "/setupScale.xml"
    markerSetFull = paramsDir + "/markerSet.xml"
    # Make scale directory if non-existent
    scaleResultsDir = subResultsDir + "/scale"
    if os.path.exists(scaleResultsDir):
        shutil.rmtree(scaleResultsDir, ignore_errors=True)
    if not os.path.exists(scaleResultsDir):
        os.mkdir(scaleResultsDir)
    # Output XML Files
    outputScaleFile = subID + "_scaleFactors.xml"
    adjustedMarkerSet = subID + "_movedMarkers.xml"
    # Output Model Files
    outputModelFile = subID + ".osim"
    # Input Data Files
    dataFiles = parentDir + "/data/osDemo"
    staticMarkerFile = "subject01_static.trc"
    staticMarkerFull = dataFiles + "/" + staticMarkerFile
    shutil.copy(staticMarkerFull, scaleResultsDir + "/" + staticMarkerFile)

    # Output Data Files
    staticCoordinates = subID + "_staticCoordinates.mot"
    # Subject Measurements
    subjectMass = 72.60000000

    # Load Model
    aModel = osim.Model(genericModelFile)

    aModel.setName(subID)
    # Initialize System
    aModel.initSystem()
    aState = aModel.initSystem()

    # Add Marker Set
    newMarkers = osim.MarkerSet(markerSetFull)
    aModel.replaceMarkerSet(aState, newMarkers)
    # Re-initialize State
    aState = aModel.initSystem()
    # Get Time Array for .trc file
    markerData = osim.MarkerData(staticMarkerFull)
    # Get Initial and Final Time
    initial_time = markerData.getStartFrameTime()
    final_time = markerData.getLastFrameTime()
    # Create an array double and apply the time range
    TimeArray = osim.ArrayDouble()
    TimeArray.set(0, initial_time)
    TimeArray.set(1, final_time)
    # Scale Tool
    scaleTool = osim.ScaleTool(scaleSetupFull)
    scaleTool.setSubjectMass(subjectMass)

    # GenericModelMaker-
    # Tell scale tool to use the loaded model
    scaleTool.getGenericModelMaker().setModelFileName(
        genericDir + "/" + genericModel)
    # # Set the Marker Set file (incase a markerset isnt attached to the model)
    scaleTool.getGenericModelMaker().setMarkerSetFileName(markerSetFull)

    # ModelScaler-
    # Whether or not to use the model scaler during scale
    scaleTool.getModelScaler().setApply(1)
    # Set the marker file (.trc) to be used for scaling
    scaleTool.getModelScaler().setMarkerFileName("/" + staticMarkerFile)
    # set a time range
    scaleTool.getModelScaler().setTimeRange(TimeArray)
    # Indicating whether or not to preserve relative mass between segments
    scaleTool.getModelScaler().setPreserveMassDist(1)
    # Name of OpenSim model file (.osim) to write when done scaling.
    scaleTool.getModelScaler().setOutputModelFileName("")
    # Filename to write scale factors that were applied to the unscaled model (optional)
    scaleTool.getModelScaler().setOutputScaleFileName(outputScaleFile)

    # Run model scaler Tool
    scaleTool.getModelScaler().processModel(
        aState, aModel, scaleResultsDir, subjectMass)

    # initialize
    aState = aModel.initSystem()

    # # Marker Placer
    # # Whether or not to use the model scaler during scale
    scaleTool.getMarkerPlacer().setApply(1)
    # # Set the marker placer time range
    scaleTool.getMarkerPlacer().setTimeRange(TimeArray)
    # # Set the marker file (.trc) to be used for scaling
    scaleTool.getMarkerPlacer().setStaticPoseFileName("/" + staticMarkerFile)
    # # Return name to a variable for future use in functions
    scaledAdjustedModel = scaleTool.getMarkerPlacer(
    ).setOutputModelFileName("/" + outputModelFile)
    # # Set the output motion filename
    scaleTool.getMarkerPlacer().setOutputMotionFileName("/" + staticCoordinates)
    # # Set the output xml of the marker adjustments
    scaleTool.getMarkerPlacer().setOutputMarkerFileName("/" + adjustedMarkerSet)
    # # Maximum amount of movement allowed in marker data when averaging
    scaleTool.getMarkerPlacer().setMaxMarkerMovement(-1)
    # # Run Marker Placer
    scaleTool.getMarkerPlacer().processModel(aState, aModel, scaleResultsDir)
    scaleTool.printToXML(scaleResultsDir + "/" + subID + "_setupScale.xml")
    # Clear Terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    shutil.copy(scaleResultsDir + "/" + outputModelFile, subResultsDir)
    return ()
