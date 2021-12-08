## FEDFUNDSRATE
"https://api.stlouisfed.org/fred/series/observations?series_id=DFF&api_key=d965097fd22f504b8127e2c97a1bf669&file_type=json"

## 10-YEAR YIELD:
"https://api.stlouisfed.org/fred/series/observations?series_id=DGS10&api_key=d965097fd22f504b8127e2c97a1bf669file_type=json"

## SP500:
"https://api.stlouisfed.org/fred/series/observations?series_id=SP500&api_key=d965097fd22f504b8127e2c97a1bf669&file_type=json"

## These are clearly very similar. The only thing that changes is the series Id.

####################################

# SET A URL BASE, THAT INCUDES EVERYTHING THAT DOESN'T CHANGE:
url_base = "https://api.stlouisfed.org/fred/series/observations?series_id={}&api_key=d965097fd22f504b8127e2c97a1bf669&file_type=json"

# NOW PICK ALL THE SERIES THAT WE ARE INTERESTED IN:
fredSeries = ['DFF', 'DGS10','SP500']

# // Begin a loop, dealing with series one by one:
for i in fredSeries:  
   # // Build the URL for this iteration of the loop, and check what we are getting:
   URL = url_base.format(i)
   print(URL)
