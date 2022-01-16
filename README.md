# MySQL Database for Property Listings

For our project submitted as part of the coursework for ECE 656: Database Systems, we aim to implement a Zillow-style application for users to view potential properties of interest as well as add their own listings for sale.  

The files contained in our repository are described below:  
- `data` folder - contains the Kaggle data `austinCrimes.csv` and `austinHousingData.csv` files upon which our project is built on.
- `data_mining_r.Rmd` and `data_mining_r.html` - implementation of the data mining exercise of regression analysis. The *html* version is ideal for viewing the results while the *Rmd* (R Studi notebook file) can be used for reproducing them.
- `View.py` and `Insert.py` - supplementary python files used to perform viewing of listings and adding of listings respectively.
- `user_cli.py` - the main script that implements the client-side application of our project.
- `relational_schema.sql` - self-explanatory
- `load.sql` - the ideal but slow implementation for populating the relational schema.
- `load_complete.mysql` - the easier way of defining the schema and populating it efficiently.


## Replication of results:
1. Clone the repository on your machine
2. Connect to MySQL user using your credentials
3. Check the file paths in the LOAD commands of the `load_complete.sql` file and run it in the MySQL CLI using the following command  
 ```source load_complete.sql```
4. Open `user_cli.py` using any text editor and edit the HOST, USER & PASSWD variables at the top of the code with your MySQL credentials.
5. Run the following in the terminal to start the application  
```python user_cli.py```

## References:
1. https://www.kaggle.com/ericpierce/austinhousingprices
2. https://www.kaggle.com/jboysen/austin-crime
