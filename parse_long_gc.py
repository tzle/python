# TASK: Read in geocode file
# #     parse out to
# #     5 elements: Input Address, Lat, Long, Geocode Quality, Google Place ID
# #     Input   : html file converted from pdf
# #     Output  : csv file of incident data ready to geocode, if possible

# MODULES & FUNCTIONS -----------------------------------------------------------
import csv

# CONSTANTS ---------------------------------------------------------------------
inFile = "F:/_rdev/stamford/post_gc/stamford_1-2498.txt"   # convert to sys.arg[]
outFile = inFile[0:len(inFile)-4] + "_gc_out.csv"     # convert to standardized output: outFile = "out_" + inFile[1:len(inFile)-4] + "csv"

# MAIN --------------------------------------------------------------------------
writer = csv.writer(open(outFile,'wb'))

# WORKS WELL
with open(inFile) as f:  # all lines read-in
    #alist = f.read().strip('\n').split(" list(results = list(list(")
    #alist = f.read().strip('\n').split("types = "+'"'+"postal_code"+'")), ')
    #alist = f.read().strip('\n').split(", formatted_address = ")
    alist = f.read().strip('\n').split("list(results = list(list(address_components =")

print str(len(alist))

adrs = ""; latlon = ""; lat = ""; lon = "" #; loctyp = ""

for item in alist:

    if "formatted_address = " in item:
        adrs = item[item.index("formatted_address = ")+len("formatted_address = "):item.index("geometry = ") - 2].replace('"',"")

    if "geometry = list(location = list(" in item:
        latlon = list(item[item.index("geometry = list(location = list(")+len("geometry = list(location = list("):item.index(" location_type =")-1].split(","))

        if len(latlon) > 1:
            # print latlon

            lat = latlon[0].strip()
            lat = lat.strip("lat = ")
            # print lat

            lon = latlon[1].strip()
            lon = lon.strip("lng = ")
            lon = lon.rstrip(")")
            # print lon

    # if "geometry = list(location = list(" in item:
    #     spec = item[item.index("location_type = ")+len("location_type = "):item.index(", viewport = list(")]

    #writer.writerow([adrs.strip(), latlon ,spec.replace("),"," ")])
    #print adrs.strip() + "," + latlon

    # output = adrs.strip()+","+lat+","+lon
    # writer.writerow([output])

    writer.writerow([adrs.strip(), lat, lon])
    #adrs = ""; latlon = ""; loctyp = ""



# WORKS WELL
# lines = [line.rstrip('\r\n').strip() for line in open(inFile)] # read in file as lines
# for line in lines:
#     if "formatted_address = " in line:
#         try:
#             writeList = line[line.index("formatted_address = ")+len("formatted_address = "):line.index("geometry = ") - 2].replace('"',"")
#             writer.writerow([writeList])
#         except:  writeList = line[line.index("formatted_address = ")+len("formatted_address = "):len(line)].replace('"',"")
#     else: print "Not Found"

# WORKS WELL
# lines = [line.replace("    "," ").rstrip('\r\n').strip() for line in open(inFile)]  # all lines read-in
# for line in lines:
#     print line
#     lineList = list(line.split("list(results = list(list(address_components = list(list("))
#
#     for item in lineList:
#         newItem = item.replace('"',"").split(",")
#         newItemList = list(newItem)
#
#         for nwIt in newItemList:
#             nwIt = nwIt.replace(")","")
#             nwIt = nwIt.replace("list(","")
#             print nwIt.strip()
#     break
