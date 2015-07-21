# TASK: Joint EMS & Fire Records into 1 dataset keeping the date field
# GOAL:   Identify apparatus movements per day,
# IN  :
# OUT :

# MODULES & FUNCTIONS -----------------------------------------------------------
import csv
from geopy.geocoders import GoogleV3
geolocator = GoogleV3()

def rtnListFromFile(someFile):
# convert file object to list object
# assumes single column
    print someFile # file name
    with open(someFile, 'rb') as csvFile:  # open & read-in all lines
        records = csv.reader(csvFile,delimiter=',')
        print records.next()
        someList = list(records)
        print str(len(someList))
    return(someList)

def makeSeqUniqueKeepOrder(seq):
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   print len(checked)
   return checked

# CONSTANTS -------------------------------------------------------
theInputFile = "F:/_pydev/stamford/stamford_pregc_address.csv"
theOutFile = theInputFile[0:len(theInputFile)-4] + "_out.csv"

# MAIN -------------------------------------------------------------

# prepare the output list of values
writeOutList = []
theHeader = ['Address','lat','lon']
writeOutList.append(theHeader)

# prepare the address list to geocode
theRecords = rtnListFromFile(theInputFile) # convert file to list object
theUnqAddresses = makeSeqUniqueKeepOrder(theRecords) # convert list to unique ordered sequence

count = 0
for theAddress in theUnqAddresses:

    try:
        location = geolocator.geocode(theAddress)
        theLat = location.latitude
        theLon = location.longitude
    except:
        theLat = "0"
        theLon = "0"

    theOutputString = theAddress, theLat, theLon
    writeOutList.append(theOutputString)
    count = count + 1

# write to output file
with open(theOutFile, 'wb') as csvFile:

     theWriter = csv.writer(csvFile, delimiter=',',lineterminator='\n')

     for item in writeOutList:
         theWriter.writerow(item)
