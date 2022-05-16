# Airline review scraping
This project scraps airline reviews from [airlinequality.com](https://www.airlinequality.com/). It is fully integrated with [skytraxratings.com/airlines](https://skytraxratings.com/airlines). The usage is very straightforward. First, go to [skytraxratings.com/airlines](https://skytraxratings.com/airlines) and select the types of airlines according to rating, service type and region. Then, copy the generated link from the browser and paste it into the *skytrax_url* list in [main.py](./Main.py) and then, run the file. (Optionally, it is possible to insert multiple links into the list.) The code automatically extracts airline names from [skytraxratings.com/airlines](https://skytraxratings.com/airlines) and then, fetches the reviews from [airlinequality.com](airlinequality.com).

The project also allows getting the specific reviews that are posted between given dates. To achieve that, you need to set variables named *ub_date* (upper bound) and *lb_date* (lower bound) in [main.py](./Main.py) file. If variables are not provided then, *ub_date* and *lb_date* will be set to the current date and zero (minimum date), respectively

The code works as follows:

* For each link in *skytrax_url* get the airline names from skytrax.
* For each airline name create an url airlinequality.
* For each url get reviews page by page and, write to airlinename.csv file.
* For each review the following information will be fetched:
    * review_date,
    * over_all_rating,
    * review_header,
    * trip_verified,
    * review_text,
    * aircraft,
    * type_of_traveller,
    * seat_type,
    * route,
    * date_flown,
    * seat_comfort,
    * cabin_staff_service,
    * food__beverages,
    * inflight_entertainment,
    * ground_service,
    * wifi__connectivity,
    * value_for_money,
    * recommended
    
Gathered reviews will be written under the directory that is created from skytrax search information. For example, if the following [skytrax link](https://skytraxratings.com/airlines?stars=5) is used with ub_date="2019-01-01", lb_date="2015-01-01" then, the directory name will be "SearchInfo__stars=5_ub_date__2019-01-01_lb_date__2015-01-01".


# Required packages
Following packages are required:

   1. [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
   2. [Pandas](https://pandas.pydata.org/)
   3. [Numpy](https://numpy.org/)
   4. [Date util](https://dateutil.readthedocs.io/en/stable/) 


