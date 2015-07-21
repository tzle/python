# TASK      : Geocode unique instances of each address in the file
# Input     : csv file containing the "FROM" and "TO" points as lat/long values,
# Output    : csv output file containing 2 appended columns

# MODULES & FUNCTIONS -----------------------------------------------------------
#from geopy.geocoders import GoogleV3
#geolocator = GoogleV3()
import csv

# newport_ri = (41.49008, -71.312796)
# cleavland_oh = (41.499498, -81.695391)
# print(great_circle(newport_ri,cleavland_oh).miles)

# CONSTANTS ---------------------------------------------------------------------
theInFile = "stamfordct_stations.csv"
theOutFile = theInFile[0:len(theInFile)-4] + "_out.csv"

# MAIN --------------------------------------------------------------------------
dictAdrs = {} # create a dictionary to store unique addresses

# load input file
with open(theInFile, 'rb') as csvFile:  # all lines read-in
    writeList = [] # create output list
    # take headers from input file
    theHeader = ['Incident-Exp#','Alm Date','Alm Time','Address','IncidentType','lat','lon']
    writeList.append(theHeader)
    print writeList

    theRecords = csv.reader(csvFile,delimiter=',')
    theRecords.next() # skip the header

    count = 0
    for rec in theRecords:

        if rec[3] != "":
            theString = rec[3].title()

            if theString.find("/F") > 1:
                theAddress = theString[0:theString.find("/")]+",Ft Thomas, KY, ,USA"

            elif theString.find("/H") > 1:
                theAddress = theString[0:theString.find("/")]+",Highland Heights, KY, ,USA"

            elif theString.find("/W") > 1:
                theAddress = theString[0:theString.find("/")]+",Wilder, KY, ,USA"

            else:
                theAddress = theString+",Cold Spring,KY,,USA"

        theAddress = theAddress.strip()
        print theAddress


        try:
            location = geolocator.geocode(theAddress)
            theLat = location.latitude
            theLon = location.longitude
        except:
            theLat = "0"
            theLon = "0"

        theOutputString = rec[0], rec[1], rec[2], rec[3], rec[4], theLat, theLon
        writeList.append(theOutputString)
        count = count + 1

print str(count)

# begin geocode count 0 to 2500
# iterate file's address field

# for each address
# if address is in dictionary - collect lat/ lon from dictionary & write to file
# if address is NOT in dictionary - get lat/lon, update dictionary, write to file
#
# open file put it into a list
# with open(theInFile, 'rb') as csvFile:  # all lines read-in
#      theRecords = csv.reader(csvFile,delimiter=',')
#      theRecords.next()
#
#     # iterate records in list, computing distance & loading results into list
#      for rec in theRecords:
#          theIncLatLon = (rec[3],rec[4])
#          theDistance = great_circle(theIncLatLon, theStationLatLon).miles
#          outString = rec[0],rec[1],rec[2], rec[3], rec[4], rec[5], rec[6], theDistance
#          writeList.append(outString)


# write computed values to output file
with open(theOutFile, 'w') as csvFile:
    theWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
    for item in writeList:
        theWriter.writerow(item)
