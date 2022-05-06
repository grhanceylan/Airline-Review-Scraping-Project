# Airline review scraping
This project scraps airline reviews from [airlinequality.com](airlinequality.com). It is fully integrated with [skytraxratings.com/airlines](https://skytraxratings.com/airlines).

The usage is very straightforward:

    1. Go to [skytraxratings.com/airlines](https://skytraxratings.com/airlines) and select the types of airlines according to rating, service type and region.
    2. Copy the genarated link from the browser and paste it into the skytrax_url list in [main.py](main.py) and run the file. (Optional: It is possible to insert multiple links into the list.) 

The project also allows to get the specific reviews which are posted between given dates. To achive that, you need to set variables named ub_date (upper bound) and lb_date (lower bound) in main.py file. If variables are not provided, ub_date and lb_date will be set to current date and zero (minimum date), respectively

The code works as follows:
    
    1. For each link in skytrax_url get the airline names from skytrax.
    2. For each airline name create an url airlinequality.com
    3. For each review page fetch the reviews and write to airlinename.csv file
    
Gathered reviews will be written under the directory that is created from skytrax search information. For example, if the following [skytrax link](https://skytraxratings.com/airlines?stars=5) is used with ub_date="2019-01-01", lb_date="2015-01-01" then, the directory name will be "SearchInfo__stars=5_ub_date__2019-01-01_lb_date__2015-01-01".


# Required packages
Following packages are required:

   1. [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
   2. [Pandas](https://pandas.pydata.org/)
   3. [Numpy](https://numpy.org/)
   4. [Date util](https://dateutil.readthedocs.io/en/stable/) 


