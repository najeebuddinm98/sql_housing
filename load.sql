USE project656;

SET innodb_lock_wait_timeout = 300;
 
LOAD DATA LOCAL INFILE 'data/austinHousingData.csv' INTO TABLE House
     FIELDS TERMINATED BY ','
     ENCLOSED BY '"'
     LINES TERMINATED BY '\n'
     IGNORE 1 ROWS 
     (zpid, city, streetAddress, zipcode, @dummy, latitude, longitude,
     propertyTaxRate, garageSpaces, hasAssociation, hasCooling, hasGarage,
     hasHeating, hasSpa, hasView, homeType, parkingSpaces, yearBuilt,
     latestPrice, numPriceChanges, latestSaleDate, @dummy, @dummy,
     latestPriceSource, @dummy, numOfAccessibilityFeatures,
     numOfAppliances, numOfParkingFeatures, numOfPatioAndPorchFeatures,
     numOfSecurityFeatures, numOfWaterfrontFeatures, numOfWindowFeatures,
     numOfCommunityFeatures, lotSizeSqFt, livingAreaSqFt, numOfPrimarySchools,
     numOfElementarySchools, numOfMiddleSchools, numOfHighSchools,
     avgSchoolDistance, avgSchoolRating, avgSchoolSize,
     MedianStudentsPerTeacher, numOfBedrooms, numOfBathrooms, numOfStories);
     
INSERT INTO SaleInfo (zpid, latestPrice, numPriceChanges, latestSaleDate,
     latestPriceSource, propertyTaxRate)
SELECT zpid, latestPrice, numPriceChanges, latestSaleDate,
latestPriceSource, propertyTaxRate FROM House;

INSERT INTO School (zpid, numOfPrimarySchools, numOfElementarySchools,
     numOfMiddleSchools, numOfHighSchools, avgSchoolDistance,
     avgSchoolRating, avgSchoolSize, MedianStudentsPerTeacher)
SELECT zpid, numOfPrimarySchools, numOfElementarySchools, numOfMiddleSchools,
numOfHighSchools, avgSchoolDistance,
avgSchoolRating, avgSchoolSize, MedianStudentsPerTeacher FROM House;



ALTER TABLE House DROP latestPrice, DROP numPriceChanges, DROP latestSaleDate,
DROP latestPriceSource, DROP propertyTaxRate, DROP numOfPrimarySchools,
DROP numOfElementarySchools, DROP numOfMiddleSchools, DROP numOfHighSchools,
DROP avgSchoolDistance, DROP avgSchoolRating, DROP avgSchoolSize,
DROP MedianStudentsPerTeacher;

LOAD DATA LOCAL INFILE 'data/austinCrime.csv' INTO TABLE Crimes
     FIELDS TERMINATED BY ','
     ENCLOSED BY '"'
     LINES TERMINATED BY '\n'
     IGNORE 1 ROWS 
     (location, @dummy, clearanceDate, clearanceStatus, @dummy,
          descript, district, latitude, @dummy, @dummy, longitude,
          primaryType, timeOfOccurence, eventID, @dummy, @dummy,
          yearOfOccurence, zipcode);

INSERT INTO Location (zpid, zipcode, numOfCrimes)
SELECT h.zpid, h.zipcode,
(SELECT COUNT(eventID) FROM Crimes WHERE zipcode = h.zipcode)
FROM House as h;


ALTER TABLE House ADD INDEX (zipcode);
ALTER TABLE Crimes ADD INDEX (zipcode);
