import mysql.connector
import re

def checkInput(message, num):

    if num == 0:
        #zipcode
        z = input(message)
        if len(z) == 5 and re.match(r"78[67][0-9]{2}", z):
            return z
        else:
            print('Wrong zipcode entered. Exiting operation.')
            return 0
        
    elif num == 1:
        #zipid
        z = input(message)
        if len(z) in [8,9,10] and re.match(r"[0-9]{8,10}", z):
            return z
        else:
            print('Wrong zipid entered. Exiting operation.')
            return 0

    else:
        print("Something went wrong. Please try again")


def process(host, user, passwd):

    db = mysql.connector.connect(host=host, user=user, passwd=passwd)
    cs = db.cursor()

    cs.execute ('use ece_656')
    
    #House
    print("Please enter all details")
    
    zpid = int(checkInput("zpid: ",1))
    if zpid == 0:
        return
    
    city = input("city ")
    
    zipcode = int(checkInput("zipcode: ",0))
    if zipcode == 0:
        return
    
    garageSpaces = int (input("Number of ggarage spaces: "))
    hasAssociation = input("Has a Homeowner's Association (please Enter True or False): ")
    hasCooling = input("Has a Cooling system (please Enter True or False): ")
    hasGarage = input("Has a garage (please Enter True or False): ")
    hasHeating = input("Has Heating (please Enter True or False): ")
    hasSpa = input("Has a Spa (please Enter True or False): ")
    hasView = input("Has a scenic view (please Enter True or False): ")
    homeType = input("Type of property: ")
    parkingSpaces = garageSpaces
    yearBuilt = int(input("Year of construction: "))
    numOfAccessibilityFeatures = int(input("Number of AccessibilityFeatures: "))
    numOfAppliances = int(input("Number of Appliances: "))
    numOfParkingFeatures = int(input("Number of ParkingFeatures:"))
    numOfPatioAndPorchFeatures = int(input("Number of PatioAndPorchFeatures: "))
    numOfSecurityFeatures = int(input("Number of SecurityFeatures: "))
    numOfWaterfrontFeatures = int(input("Number of WaterfrontFeatures: "))
    numOfWindowFeatures = int(input("Number of WindowFeatures: "))
    numOfCommunityFeatures = int(input("Number of CommunityFeatures: "))
    lotSizeSqFt = int(input("Lot size in square feet: "))
    livingAreaSqFt = int(input("Living area in square feet: "))
    numOfBathrooms = int(input("Number of Bathrooms: "))
    numOfBedrooms = int(input("Number of Bedrooms: "))
    numOfStories = int(input("Number of Stories: "))

    in_house = """INSERT INTO House (zpid,city,zipcode,garageSpaces,hasAssociation,hasCooling,hasGarage,hasHeating,hasSpa,hasView,homeType,
parkingSpaces, yearBuilt,numOfAccessibilityFeatures,numOfAppliances,numOfParkingFeatures,numOfPatioAndPorchFeatures,numOfSecurityFeatures,
numOfWaterfrontFeatures, numOfWindowFeatures,numOfCommunityFeatures,lotSizeSqFt,livingAreaSqFt,numOfBathrooms,numOfBedrooms,numOfStories)
VALUES ({0},'{1}','{2}',{3},{4},'{5}','{6}','{7}','{8}','{9}','{10}','{11}',{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},
{25})""".format(zpid,city,zipcode,garageSpaces,hasAssociation,hasCooling,hasGarage,hasHeating,hasSpa,hasView,homeType,parkingSpaces,yearBuilt,numOfAccessibilityFeatures,numOfAppliances,numOfParkingFeatures,numOfPatioAndPorchFeatures,numOfSecurityFeatures,numOfWaterfrontFeatures,numOfWindowFeatures,numOfCommunityFeatures,lotSizeSqFt,livingAreaSqFt,numOfBathrooms,numOfBedrooms,numOfStories)
    
    cs.execute(in_house)

    for row in cs:
        print(row)
    db.commit()


    #SaleInfo
    latestPrice = int(input("Current price: "))
    propertyTaxRate = float(input("Property tax rate: "))
    numPriceChanges = int(input("Number of Price Changes: "))
    latestSaleDate = input("Last sale date: ")

    in_sale = """INSERT INTO saleinfo (zpid,latestPrice,propertyTaxRate,numPriceChanges,latestSaleDate)
VALUES ({0},{1},{2},{3},{4})""".format(zpid,latestPrice,propertyTaxRate,numPriceChanges,latestSaleDate)

    cs.execute(in_sale)

    for row in cs:
        print(row)
    db.commit()


    #School
    numOfPrimarySchools = int(input("Number of Primary Schools: "))
    numOfElementarySchools = int(input("Number of Elementary Schools: "))
    numOfMiddleSchools = float (input("Number of Middle Schools: "))
    numOfHighSchools = int(input("Number of High Schools :"))
    avgSchoolDistance = float(input("Average School Distance :"))
    avgSchoolRating = float(input("Average School Rating: "))
    avgSchoolSize = int(input("Average School Size: "))

    in_school = """INSERT INTO school (zpid,numOfPrimarySchools,numOfElementarySchools,numOfMiddleSchools,numOfHighSchools,avgSchoolDistance,avgSchoolRating,avgSchoolSize)
VALUES ({0},{1},{2},{3},{4},{5},{6},{7})""".format(zpid,numOfPrimarySchools,numOfElementarySchools,numOfMiddleSchools,numOfHighSchools,avgSchoolDistance,avgSchoolRating,avgSchoolSize)

    cs.execute(in_school)
    for row in cs:
        print(row)
    db.commit()

if __name__ == "__main__":
    process()


