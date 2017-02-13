import requests, urllib2, zipfile, os, StringIO, csv, sys
from lxml import html

csv.field_size_limit(sys.maxsize)

resp = urllib2.urlopen(urllib2.Request("ftp://ftp.fec.gov/FEC/electronic/")).readlines()

counter=0
with open('complete_fec_2011-2017.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    for i in range(0, len(resp)):
        filename = (resp[i].replace("\n", "").replace("\r", "")).split(" ")[len((resp[i].replace("\n", "").replace("\r", "")).split(" "))-1]
        
        if filename.startswith(("2011", "2012", "2013", "2014", "2015", "2016", "2017")):
            counter+=1
            if not os.path.exists(os.getcwd()+'/'+filename):
                response = urllib2.urlopen("ftp://ftp.fec.gov/FEC/electronic/"+filename).read()
                with open(filename, 'w') as f:
                    f.write(response)
            
            archive = zipfile.ZipFile(filename, 'r')
            arclist = archive.namelist()
            
            print str(counter) + ": " + str(filename) + " => DONE!"
            
            for lis in arclist:
                reader = csv.reader(StringIO.StringIO(archive.open(lis).read()), delimiter="\034")
                
                for row in reader:
                    try:
                        if row[0] == 'SA11AI' or row[0] == 'SA17A' or row[0] == 'F65':
                            #print row
                            csvwriter.writerow(row)
                    except:
                        pass
            try:
                os.remove(os.getcwd()+'/'+filename)
            except:
                pass
