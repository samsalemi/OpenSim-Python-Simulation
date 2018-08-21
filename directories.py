def main(directories):
    parentDir = "E:/Documents/University/Masters/Sandbox/Project"
    paramsDir = parentDir + "/genericSettings"
    genericDir = parentDir + "/model"
    resultsDir = parentDir + "/results"
    subID = "subject01"
    subResultsDir = resultsDir + "/" + subID
    ikResultsDir = subResultsDir + "/ik"
    idResultsDir = subResultsDir + "/id"
    soResultsDir = subResultsDir + "/so"
    rraResultsDir = subResultsDir + "/rra"
    cmcResultsDir = subResultsDir + "/cmc"
    jrResultsDir = subResultsDir + "/jr"
    return(parentDir, paramsDir, genericDir, resultsDir, subID, subResultsDir, ikResultsDir,idResultsDir, soResultsDir, rraResultsDir, cmcResultsDir, jrResultsDir)
