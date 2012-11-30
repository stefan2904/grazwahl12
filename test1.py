import csv 

sprengel = csv.reader(open("./raw/Graz/GRW2012_Sprengelerg.csv", "r"), delimiter=";")

sprengelNr = -1

# wkurz;sprengel;ptname;ptlang;listenplatz;gesamt;unguel;gueltig;stimmen;anzspr;aenderung_am;aenderung_durch

for row in sprengel: 
	if(row[1].isdigit()):
		if(sprengelNr != row[1]):
			print ""
		sprengelNr = row[1]
		partei = row[3]
		gesamt = row[5]
		gueltig = row[7]
		stimmen = row[8]
	
		prozent = float(stimmen)/float(gueltig)*100
		print sprengelNr, partei, ":", prozent, "bei", stimmen, "von", gesamt, "Stimmen"
	else:
		print row
