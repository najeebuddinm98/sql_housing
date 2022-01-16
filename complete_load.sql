CREATE DATABASE ece_656;

USE ece_656;

CREATE TABLE House (
  zpid bigint PRIMARY KEY NOT NULL,
  city text,
  streetAddress text,
  zipcode int NOT NULL,
  descript text,
  latitude double DEFAULT NULL,
  longitude double DEFAULT NULL,
  propertyTaxRate double DEFAULT NULL,
  garageSpaces int DEFAULT NULL,
  hasAssociation BOOLEAN DEFAULT FALSE,
  hasCooling BOOLEAN DEFAULT FALSE,
  hasGarage BOOLEAN DEFAULT FALSE,
  hasHeating BOOLEAN DEFAULT FALSE,
  hasSpa BOOLEAN DEFAULT FALSE,
  hasView BOOLEAN DEFAULT FALSE,
  homeType text,
  parkingSpaces int DEFAULT NULL,
  yearBuilt datetime,
  latestPrice int DEFAULT NULL,
  numPriceChanges int DEFAULT NULL,
  latest_saledate datetime,
  latest_salemonth int DEFAULT NULL,
  latest_saleyear int DEFAULT NULL,
  latestPriceSource text,
  numOfPhotos int DEFAULT NULL,
  numOfAccessibilityFeatures int DEFAULT NULL,
  numOfAppliances int DEFAULT NULL,
  numOfParkingFeatures int DEFAULT NULL,
  numOfPatioAndPorchFeatures int DEFAULT NULL,
  numOfSecurityFeatures int DEFAULT NULL,
  numOfWaterfrontFeatures int DEFAULT NULL,
  numOfWindowFeatures int DEFAULT NULL,
  numOfCommunityFeatures int DEFAULT NULL,
  lotSizeSqFt double DEFAULT NULL,
  livingAreaSqFt int DEFAULT NULL,
  numOfPrimarySchools int DEFAULT NULL,
  numOfElementarySchools int DEFAULT NULL,
  numOfMiddleSchools int DEFAULT NULL,
  numOfHighSchools int DEFAULT NULL,
  avgSchoolDistance double DEFAULT NULL,
  avgSchoolRating double DEFAULT NULL,
  avgSchoolSize int DEFAULT NULL,
  MedianStudentsPerTeacher int DEFAULT NULL,
  numOfBathrooms int DEFAULT NULL,
  numOfBedrooms int DEFAULT NULL,
  numOfStories int DEFAULT NULL
);
  
  
LOAD DATA LOCAL INFILE 'data/austinHousingData.csv' INTO TABLE House
     FIELDS TERMINATED BY ','
     ENCLOSED BY '"'
     LINES TERMINATED BY '\n'
     IGNORE 1 ROWS
     (zpid, city, streetAddress, zipcode, descript, latitude, longitude, propertyTaxRate, garageSpaces, hasAssociation, hasCooling,
     hasGarage, hasHeating, hasSpa, hasView, homeType, parkingSpaces, yearBuilt, latestPrice, numPriceChanges, latest_saledate, 
     latest_salemonth, latest_saleyear, latestPriceSource, numOfPhotos, numOfAccessibilityFeatures, numOfAppliances, numOfParkingFeatures, 
     numOfPatioAndPorchFeatures, numOfSecurityFeatures, numOfWaterfrontFeatures, numOfWindowFeatures, numOfCommunityFeatures, lotSizeSqFt, 
     livingAreaSqFt, numOfPrimarySchools, numOfElementarySchools, numOfMiddleSchools, numOfHighSchools, avgSchoolDistance, avgSchoolRating, 
     avgSchoolSize, MedianStudentsPerTeacher, numOfBedrooms, numOfBathrooms, numOfStories)
     
CREATE TABLE SaleInfo (
	zpid bigint PRIMARY KEY NOT NULL,
     propertyTaxRate double DEFAULT NULL,
	latestPrice int DEFAULT NULL,
	numPriceChanges int,
	latestSaleDate datetime,
	latestPriceSource text,
    FOREIGN KEY (zpid) REFERENCES House(zpid)
);

INSERT INTO SaleInfo (zpid, latestPrice, numPriceChanges, latestSaleDate, latestPriceSource, propertyTaxRate)
SELECT zpid, latestPrice, numPriceChanges, latest_saledate, latestPriceSource, propertyTaxRate FROM House;

CREATE TABLE School (
	zpid bigint PRIMARY KEY NOT NULL,
     numOfPrimarySchools int DEFAULT NULL,
	numOfElementarySchools int DEFAULT NULL,
	numOfMiddleSchools int DEFAULT NULL,
	numOfHighSchools int DEFAULT NULL,
	avgSchoolDistance double DEFAULT NULL,
	avgSchoolRating double DEFAULT NULL,
	avgSchoolSize int DEFAULT NULL,
	MedianStudentsPerTeacher int DEFAULT NULL,
     FOREIGN KEY (zpid) REFERENCES House(zpid)
);
    
INSERT INTO School (zpid, numOfPrimarySchools, numOfElementarySchools, numOfMiddleSchools, numOfHighSchools, avgSchoolDistance,
avgSchoolRating, avgSchoolSize, MedianStudentsPerTeacher) 
SELECT zpid, numOfPrimarySchools, numOfElementarySchools, numOfMiddleSchools, numOfHighSchools, avgSchoolDistance,
avgSchoolRating, avgSchoolSize, MedianStudentsPerTeacher FROM House;


ALTER TABLE House DROP latestPrice, DROP numPriceChanges, DROP latest_saledate, DROP latest_salemonth, DROP latest_saleyear, DROP latestPriceSource,
DROP propertyTaxRate, DROP numOfPrimarySchools, DROP numOfElementarySchools, DROP numOfMiddleSchools, DROP numOfHighSchools, DROP avgSchoolDistance,
DROP avgSchoolRating, DROP avgSchoolSize, DROP MedianStudentsPerTeacher, DROP descript;

CREATE TABLE Crimes (
    eventID int,
    location varchar(255),
    zipcode int NOT NULL,
    district varchar(2),
    latitude decimal(6,3) DEFAULT NULL,
    longitude decimal(6,3) DEFAULT NULL,
    timeOfOccurence DATETIME,
    yearOfOccurence int DEFAULT NULL,
    primaryType varchar(50),
    descript varchar(50),
    clearanceDate DATETIME,
    clearanceStatus varchar(50),
    PRIMARY KEY (eventID)
);

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




