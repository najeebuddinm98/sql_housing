import mysql.connector
import re

def checkInput(message, num):
    zipid_pattern = re.compile()
    year_pattern = re.compile(r"[12][0-9]{3}")
    if num == 0:
        z = input(message)
        if len(z) == 5 and re.match(r"78[67][0-9]{2}", z):
            return z
        else:
            print('Wrong zipcode entered. Exiting operation.')
            return 0
        
    elif num == 1:
        z = input(message)
        if len(z) in [8,9,10] and re.match(r"[0-9]{8,10}", z):
            return z
        else:
            print('Wrong zipid entered. Exiting operation.')
            return 0

    else:
        print("Something went wrong. Please try again")
        
        

def process(host, user, passwd):
    
    db = mysql.connector.connect(host=host , user=user ,passwd=passwd)
    cs = db.cursor()

    cs.execute('USE ece_656')
    
    zipcode = checkInput('Please enter zipcode of area where you want to look around: ', 0)
    if zipcode == 0:
        return

    print('Furthermore, the following filters can be applied to narrow down your search:')
    print("""1. Type of home \n2. Number of bathrooms \n3. Number of bedrooms \n4. Number of Floors \n5. Current price
6. Average school rating \n7. Number of parking spaces \n8. Air conditioning is present
9. Heating system is included \n10.Has a Spa \n11.Has a scenic view \n12.Year of construction
13.Accessibility features \n14.Number of included appliances \n15.Features of the Patio and Porches
16.Number of Security Features \n17.Waterfront features \n18.Lot Size \n19.Living area Size""")

    filt = int(input('Select the option corresponding to the filters or type 0 to view all listings in entered zipcode: '))

    query = "SELECT zpid, streetAddress, latestPrice FROM House INNER JOIN SaleInfo USING (zpid) WHERE zipcode = {0}".format(zipcode)

    while (filt != 0):
        homelist = ['Single Family', 'Residential', 'Vacant Land', 'Multiple Occupancy', 'Condo', 'Townhouse',
                    'Apartment', 'Mobile/Manufactured', 'MultiFamily', 'Other']
        
        if filt == 1:
            print("Types of homes available: ", homelist)
            x = int(input("Enter option number for type of home: "))
            
            query = query + " AND homeType = '{0}'".format(homelist[x-1])
            
        if filt == 2:
            x = int(input("Enter minimum number of bathrooms: "))
            query = query + " AND numOfBathrooms >= {0}".format(x)
                
        if filt == 3:
            x = int(input("Enter minimum number of bedrooms: "))
            query = query + " AND numOfBedrooms >= {0}".format(x)
            
        if filt == 4:
            x = int(input("Enter minimum number of floors: "))
            query = query + " AND numOfStories >= {0}".format(x)

        if filt == 5:
            print("Enter price range below")
            x = int(input("Minimum: "))
            y = int(input("Maximum: "))
            query = query + " AND latestPrice BETWEEN {0} AND {1}".format(x,y)

        if filt == 6:
            x = float(input("Enter minimum average school rating (scale of 1 to 10): "))
            query = query + "AND zpid IN (SELECT zpid FROM School WHERE avgSchoolRating >= {0})".format(x)
            
        if filt == 7:
            x = int(input("Enter minimum number of parking spaces: "))
            query = query + " AND garageSpaces >= {0}".format(x)
            
        if filt == 8:
            a = input("Do you require air conditioning? (y/n) : ")
            x = 'TRUE' if (a == 'y') else 'FALSE'
            query = query + " AND hasCooling = '{0}'".format(x)
            
        if filt == 9:
            a = input("Do you require heating? (y/n) : ")
            x = 'TRUE' if (a == 'y') else 'FALSE'
            query = query + " AND hasHeating = '{0}'".format(x)
            
        if filt == 10:
            a = input("Spa installed in the property (y/n) : ")
            x = 'TRUE' if (a == 'y') else 'FALSE'
            query = query + " AND hasSpa = '{0}'".format(x)
            
        if filt == 11:
            a = input("The property has scenic views (y/n) : ")
            x = 'TRUE' if (a == 'y') else 'FALSE'
            query = query + " AND hasSpa = '{0}'".format(x)
            
        if filt == 12:
            x = int(input("Enter the earliest year by which the property should have been built: "))
            query = query + " AND yearBuilt >= '{0}'".format(x)
            
        if filt == 13:
            a = input("Do you require accessibility features? (y/n): ")
            if a == 'y':
                query = query + " AND numOfAccessibilityFeatures >= 1"
            
        if filt == 14:
            x = int(input("Enter minimum number of included appliances: "))
            query = query + " AND numOfAppliances >= {0}".format(x)
            
        if filt == 15:
            x = int(input("Enter minimum number of patio features: "))
            query = query + " AND numOfPatioAndPorchFeatures >= {0}".format(x)
            
        if filt == 16:
            x = int(input("Enter minimum number of security features: "))
            query = query + " AND numOfSecurityFeatures >= {0}".format(x)
            
        if filt == 17:
            x = int(input("Enter minimum number of Waterfront features: "))
            query = query + " AND numOfWaterfrontFeatures >= {0}".format(x)
            
        if filt == 18:
            print("Enter minimum and maximum lot size in square feet below")
            x = int(input("Minimum: "))
            y = int(input("Maximum: "))
            query = query + " AND lotSizeSqFt BETWEEN {0} AND {1}".format(x,y)

        if filt == 19:
            print("Enter minimum and maximum living area size in square feet below")
            x = int(input("Minimum: "))
            y = int(input("Maximum: "))
            query = query + " AND livingAreaSqFt BETWEEN {0} AND {1}".format(x,y)
            
        filt = int(input('Do you want to add another filter? If yes, type filter option number, else type 0 to view results: '))

    
    check_res = None
    boolean = True
    
    cs.execute(query)
    for row in cs:
        check_res = row
        if check_res:
            print(f"zpID : {row[0]}, address : {row[1]}, price : {row[2]}")
        else:
            print("No properties match your filters. Please retry from the start.")
            boolean = False
            break

    if boolean:
        houseid = int(checkInput("To view the full details of a particular house, please enter the zpid or enter 0 to exit:", 1))

        if houseid == 0:
            print()
        else:        
            single_q = """SELECT city, streetAddress, zipcode, homeType, numOfStories, numOfBedrooms, numOfBathrooms, lotSizeSqFt,
    livingAreaSqFt, garageSpaces, hasAssociation, hasHeating, hasCooling, hasSpa, hasView, yearBuilt, numOfAccessibilityFeatures,
    numOfAppliances, numOfPatioAndPorchFeatures, numOfSecurityFeatures, numOfWaterfrontFeatures, numOfCommunityFeatures
    FROM House WHERE zpid = {0}""".format(houseid)
            
            cs.execute(single_q)
            for row in cs:
                print("City: ", row[0])
                print("Address: ", row[1])
                print("Zipcode: ", row[2])
                print("Home type: ", row[3])
                print("Number of Stories: ", row[4])
                print("Number of bedrooms: ", row[5])
                print("Number of bathrooms: ", row[6])
                print("Lot size (SqFt): ", row[7])
                print("Living area size (SqFt): ", row[8])
                print("Parking spaces: ", row[9])
                print("Has a Homeowner's Association: ", row[10])
                print("Has heating systems: ", row[11])
                print("Has air conditioning: ", row[12])
                print("Has a Spa: ", row[13])
                print("Has a scenic view: ", row[14])
                print("Year built: ", row[15])
                print("Number of Accessibility features: ", row[16])
                print("Number of Appliances: ", row[17])
                print("Number of Patio features: ", row[18])
                print("Number of Security features: ", row[19])
                print("Number of Waterfront features: ", row[20])
                print("Number of Community features: ", row[21])

            cs.execute("SELECT * FROM SaleInfo WHERE zpid = {0}".format(houseid))
            for row in cs:
                print("Current price: ", row[1])
                print("Property tax rate: ", row[2])
                print("Last sale date: ", row[4])

            cs.execute("SELECT * FROM School WHERE zpid = {0}".format(houseid))
            for row in cs:
                print("Number of primary schools: ", row[1])
                print("Number of elementary schools: ", row[2])
                print("Number of middle schools: ", row[3])
                print("Number of high schools: ", row[4])
                print("Average school size: ", row[7])
                print("Average school distance: ", row[5])
                print("Average school rating: ", row[6])

            cs.execute("SELECT numOfCrimes FROM Location WHERE zpid = {0}".format(houseid))
            for row in cs:
                print("Number of crimes in the given zipcode: ", row[0])

            inf = input('Do you want details about previous crimes around the selected house? (y/n) :')
            if inf == 'y':
                cleared_percent = """WITH cte AS (SELECT COUNT(*) AS total FROM Crimes WHERE zipcode = {0})
    SELECT (((SELECT total FROM cte) - COUNT(*))/(SELECT total FROM cte))*100 FROM Crimes
    WHERE clearanceStatus != 'Not cleared' AND zipcode = {0}""".format(zipcode)
                cs.execute(cleared_percent)
                for row in cs:
                    print("Percentage of crimes cleared by the authorities: ",row[0])

                most_common = """SELECT primaryType, COUNT(*) AS magnitude
    FROM Crimes WHERE zipcode = {0} GROUP BY primaryType ORDER BY magnitude DESC""".format(zipcode)
                cs.execute(most_common)
                for row in cs:
                    print("Crime type: ",row[0])
                    print("Number of reports: ",row[1])


if __name__ == "__main__":
    process()

