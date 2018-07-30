import datetime
import psycopg2
import requests



def extract_engagements():
	engagements = urllib2.urlopen
	return engagements.read()



def store_engagements(engagements):
	# store engagements in psql
	conn = psycopg2.connect(host='localhost',dbname="postgres", user="postgres", password="postgres")
	cur = conn.cursor()
	
	# create table
	cur.execute("CREATE TABLE engagement_types (id bigint, type varchar, timestamp bigint);")
	
	# populate table with engagements
	for i in len(engagements['results']):
		day = datetime.datetime.fromtimestamp(i['engagement']['timestamp'])
		cur.execute("INSERT INTO engagements (id, type, day) VALUES (%s, %s, %s)", i['engagement']['id'], i['engagement']['type'], day)



	# query engagements
	c = cur.execute('''
		SELECT count(engagement), day 
		FROM {
		SELECT * FROM engagement_types
		GROUP by day
		}
		'''
	)

	# clean up
	conn.commit()
	cur.close()
	conn.close()


