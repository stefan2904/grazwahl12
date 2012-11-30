import csv 

sprengel = csv.reader(open("./raw/Graz/GRW2012_Sprengelerg.csv", "r"), delimiter=";")

sprengelNr = -1
sprengelCount = 0
gueltigSum = 0

piratenProzentSum = 0
piratenSum = 0

piratenCHECK = float(2.69726951718)
groesserCount = 0
kleinerCount = 0
maxProzent = 0
maxSprengel = 0

# wkurz;sprengel;ptname;ptlang;listenplatz;gesamt;unguel;gueltig;stimmen;anzspr;aenderung_am;aenderung_durch

for row in sprengel: 
	if row[1].isdigit():
		if sprengelNr != row[1]:
			#print ""
			sprengelCount+=1
			gueltigSum+=float(row[7])
		sprengelNr = row[1]
		partei = row[3]
		gesamt = row[5]
		gueltig = row[7]
		stimmen = row[8]
	
		prozent = float(stimmen)/float(gueltig)*100
		#print sprengelNr, partei, ":", prozent, "% bei", stimmen, "von", gesamt, "Stimmen"

		if partei == "Piratenpartei Graz":
			piratenProzentSum+=prozent
			piratenSum+=float(stimmen)

			if prozent > maxProzent:
				maxProzent = prozent
				maxSprengel = sprengelNr

			if prozent > piratenCHECK:
				print "Sprengel", sprengelNr, "war um", prozent-piratenCHECK, "groesser"
				groesserCount+=1
			else:
				print "Sprengel", sprengelNr, "war um", piratenCHECK-prozent, "kleiner"
				kleinerCount+=1

	else:
		print row

print ""
print "Piraten im Schnitt", piratenProzentSum/sprengelCount, "%"
print "Piraten in Summe", piratenSum/gueltigSum*100, "% bei", piratenSum, "Stimmen"
print "Es waren", groesserCount, "Sprengel groesser als die Summe"
print "Es waren", kleinerCount, "Sprengel kleiner als die Summe"
print "Rekord waren", maxProzent, "% in Sprengel", maxSprengel
print ""	
