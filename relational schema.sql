-- create and select database
CREATE DATABASE ece_656;
USE ece_656;

-- clearing
DROP TABLE IF EXISTS House;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS School;
DROP TABLE IF EXISTS SaleInfo;
DROP TABLE IF EXISTS Crimes;

-- creation
CREATE TABLE House (
    zpid bigint,
    city varchar(20) DEFAULT NULL,
    streetAddress varchar(255) DEFAULT NULL,
    zipcode int DEFAULT NULL,
    latitude decimal(6,3) DEFAULT NULL,
    longitude decimal(6,3) DEFAULT NULL,
    lotSizeSqFt int DEFAULT NULL,
    livingAreaSqFt int DEFAULT NULL,
    numOfBathrooms int DEFAULT NULL,
    numOfBedrooms int DEFAULT NULL,
    numOfStories int DEFAULT NULL,
    homeType varchar(30) NOT NULL,
    yearBuilt int DEFAULT NULL,
    garageSpaces int DEFAULT NULL,
    parkingSpaces int DEFAULT NULL,
    hasAssociation varchar(5) DEFAULT 'FALSE' CHECK (hasAssociation IN ('TRUE', 'FALSE')),
    hasCooling varchar(5) DEFAULT 'FALSE' CHECK (hasCooling IN ('TRUE', 'FALSE')),
    hasGarage varchar(5) DEFAULT 'FALSE' CHECK (hasGarage IN ('TRUE', 'FALSE')),
    hasHeating varchar(5) DEFAULT 'FALSE' CHECK (hasHeating IN ('TRUE', 'FALSE')),
    hasSpa varchar(5) DEFAULT 'FALSE' CHECK (hasSpa IN ('TRUE', 'FALSE')),
    hasView varchar(5) DEFAULT 'FALSE' CHECK (hasView IN ('TRUE', 'FALSE')),
    numOfAccessibilityFeatures int DEFAULT NULL,
    numOfAppliances int DEFAULT NULL,
    numOfParkingFeatures int DEFAULT NULL,
    numOfPatioAndPorchFeatures int DEFAULT NULL,
    numOfSecurityFeatures int DEFAULT NULL,
    numOfWaterfrontFeatures int DEFAULT NULL,
    numOfWindowFeatures int DEFAULT NULL,
    numOfCommunityFeatures int DEFAULT NULL,
    PRIMARY KEY (zpid),
    CONSTRAINT zpid_length CHECK (REGEXP_LIKE(zpid, '[0-9]{8.10}')),
    CONSTRAINT zipcode_format CHECK (REGEXP_LIKE(zipcode, '78[0-9]{3}')),
    CONSTRAINT year_limit CHECK ( yearBuilt <= '2021' )
);


CREATE TABLE SaleInfo (
    zpid bigint,
    latestPrice int DEFAULT NULL,
    propertyTaxRate decimal(3,2) DEFAULT NULL,
    numPriceChanges int DEFAULT NULL,
    latestSaleDate DATETIME,
    PRIMARY KEY (zpid),
    FOREIGN KEY (zpid) REFERENCES House(zpid),
    CONSTRAINT saledate_limit CHECK ( latestSaleDate <= CURRENT_DATE() )
);


CREATE TABLE School (
    zpid bigint,
    numOfPrimarySchools int DEFAULT NULL,
    numOfElementarySchools int DEFAULT NULL,
    numOfMiddleSchools int DEFAULT NULL,
    numOfHighSchools int DEFAULT NULL,
    avgSchoolDistance decimal(4,2) DEFAULT NULL,
    avgSchoolRating decimal(4,2) DEFAULT NULL,
    avgSchoolSize int DEFAULT NULL,
    PRIMARY KEY (zpid),
    FOREIGN KEY (zpid) references House(zpid)
);

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

CREATE TABLE Location (
    zipcode int,
    zpid bigint,
    numOfCrimes int not null,
	PRIMARY KEY (zipcode,zpid),
    FOREIGN KEY (zipcode,zpid) references House(zipcode,zpid)
);



			                     
