# Alooma SE Challenge

Extracting engagement data from hubspot helps build part of a functional data pipeline to better understand user behavior.


The functions for this task are in the api.py file. And the required python packages can be found in the requirements.txt. Additionally, this project uses psql.

This project can be used by doing the following
  1. download this reposity and navigate to the directory
  2. install the requirements.txt file with "pip install -r requirements.txt" 
  3. set up psql
  4. in a terminal type 'python -i api.py'
  5. this will open up an interactive shell with the functions available to use


#### Engagements

Using Hubspot's example API credentials, I queried the engagements API and converted the data to JSON. Storing in mongodb allows us to have a schema free repository for this data and to pull and aggregate information as needed.

A basic overview of the data demonstrates these following engagement type counts.


Engagement Type Counts

| PUBLISHING_TASK | NOTE | EMAIL | CALL | TASK | 
| --- | --- | --- | --- | --- |
| 2 | 76 | 1 | 5 | 16 |


##### Methods

I started by reading the Hubspot API documentation on egagements to better understand the type of data I would be dealing with. Since I have some familiarity with Hubspot as a platform I was quickly able to understand the data and jump right in to querying the API.

Once I started querying the API, I had to deal with formatting it into JSON and storing it in a database. I chose psql since I have some experience working with it before to store text data scraped from the web.

I ran a quick query to find out engagement type counts and to plan for larger analysis of this data set. 

I plan on doing more with this data including breaking down by date, and creating rolling averages.
