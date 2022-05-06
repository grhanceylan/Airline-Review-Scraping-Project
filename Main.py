import Helpers
import datetime
import dateutil.parser as dtparser



# enter the skytrax links to extract airline names
skytrax_urls= ["https://skytraxratings.com/airlines?types=full_service&regions=europe", "https://skytraxratings.com/airlines?types=full_service&regions=north-america"]

# ub_date: upper bound for review date
# lb_date: lower bound for review date
# date should be in the following format: year-month-day
ub_date, lb_date= None, '2015-01-01'

# if give, cast date info else get the current date
ub_date = dtparser.parse(ub_date) if ub_date is not None else datetime.datetime.today()

#  if given, cast date info else  set zero
lb_date = dtparser.parse(lb_date) if lb_date is not None else datetime.datetime.min

for url in skytrax_urls:

    airline_names= Helpers.get_airline_names(url=url)
    print(str(len(airline_names))+ " airlines are found for the following link: " + url )
    # create directory for each skytrax link with search info

    directory= "SearchInfo__"+url.split('?')[1] + '_ub_date__'+ ub_date.strftime ('%Y_%m_%d') +'_lb_date__'+lb_date.strftime ('%Y_%m_%d')

    for airline_name in airline_names:
        reviews = Helpers.get_reviews(airline_name= airline_name,ub_date=ub_date,lb_date=lb_date,directory=directory)


