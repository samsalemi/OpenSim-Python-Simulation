# August 14th 2018
# Author: Samuel Salemi
# University of Guelph Masters Candidate
# This module writes out excel files for the plotter 

def write(filename):

    import opensim as osim
    import csv
    import numpy as np
    import directories

    allDir = list(directories.main(directories))
    idResultsDir = allDir[7]
    soResultsDir = allDir[8]
    cmcResultsDir = allDir[10]
    
    storage = osim.Storage(filename)
    labels = storage.getColumnLabels()
    labelSize = labels.getSize()
    header = []

    for i in range(labelSize):
        header.append(labels.getitem(i))

    nrows = storage.getSize()

    data = []
    dataArray = []

    if header[0] == 'time':
        st = 1
        dataArray.append(osim.ArrayDouble())
        storage.getTimeColumn(dataArray[0])
        column = []
        for j in range(nrows):
            column.append(dataArray[0].getitem(j))

        data.append(column)
    else:
        st = 0

    for i in range(st, labelSize):
        dataArray.append(osim.ArrayDouble())
        storage.getDataColumn(header[i], dataArray[i])
        column = []
        for j in range(nrows):
            column.append(dataArray[i].getitem(j))

        data.append(column)
    dataFixed = np.transpose(data)
    headerFixed = []
    headerFixed.append(header)

# Writing excel file for plotting
    if filename == idResultsDir + "/" + "subject01_walk1_id.sto":
        with open((idResultsDir + "/" + "idData.csv"), "wb") as fid:
            csvWriter = csv.writer(fid, dialect='excel')
            csvWriter.writerows(headerFixed)
            csvWriter.writerows(dataFixed)

    if filename == soResultsDir + "/" + "subject01_walk1_StaticOptimization_force.sto":
        with open((soResultsDir + "/" + "soData.csv"), "wb") as fid:
            csvWriter = csv.writer(fid, dialect='excel')
            csvWriter.writerows(headerFixed)
            csvWriter.writerows(dataFixed)

    if filename == soResultsDir + "/" + "_Gait2354 Joint RXN_ReactionLoads.sto":
        with open((soResultsDir + "/" + "soJrData.csv"), "wb") as fid:
            csvWriter = csv.writer(fid, dialect='excel')
            csvWriter.writerows(headerFixed)
            csvWriter.writerows(dataFixed)

    if filename == cmcResultsDir + "/" + "_Gait2354 Joint RXN_ReactionLoads.sto":
        with open((cmcResultsDir + "/" + "cmcJrData.csv"), "wb") as fid:
            csvWriter = csv.writer(fid, dialect='excel')
            csvWriter.writerows(headerFixed)
            csvWriter.writerows(dataFixed)
    return()
