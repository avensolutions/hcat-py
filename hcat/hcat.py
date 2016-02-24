"""
HCat Python Module 
Returns metadata for objects in HCatalog as Python objects
"""    
import json, urllib2

def _runcommand(command):
	url_resp = urllib2.urlopen(command)
	json_obj = json.load(url_resp)
	return json_obj

def _retcoltuples(inlist):
	# takes a list of dicts and returns a list of tuples of (name,type)
	cols = []
	if len(inlist) > 0:
		for col in inlist:
			cols.append((col['name'],col['type']))
	return cols

def showdatabases(hcaturi, username='hdfs'):
	"""
	hcat.showdatabases
	
	Args:
		hcaturi (str): uri for webhcat host, eg hive.myorg.com:50111
		username (Optional[str]): user name, defaults to 'hdfs'
	Returns:
		list: list of available hcat databases
	""" 
	command2run = 'http://' + hcaturi + '/templeton/v1/ddl/database?user.name=' + username
	resp = _runcommand(command2run)
	return resp['databases']
	
def showtables(hcaturi, dbname='default', username='hdfs'):
	"""
	hcat.showtables
	
	Args:
		hcaturi (str): uri for webhcat host, eg hive.myorg.com:50111
		dbname (Optional[str]): database name, defaults to 'default'
		username (Optional[str]): user name defaults to hdfs
	Returns:
		list: list of available tables for the specified hcat database
	"""
	command2run = 'http://' + hcaturi + '/templeton/v1/ddl/database/' + dbname+ '/table?user.name=' + username
	resp = _runcommand(command2run)
	return resp['tables']

def describe(hcaturi, tablename, dbname='default', username='hdfs'):
	"""
	hcat.describe
	
	Args:
		hcaturi (str): uri for webhcat host, eg hive.myorg.com:50111
		tablename (str): table name
		dbname (Optional[str]): database name, defaults to 'default'
		username (Optional[str]): user name defaults to hdfs
	Returns:
		dict: dict containing metadata for the table in the format:
			{
			'tableType':'<tableType>'
			,'inputFormat':'<inputFormat>'
			,'outputFormat':'<outputFormat>'
			,'columns': [('<colname>', '<coltype>')]
			,'partitionColumns': [('<colname>', '<coltype>')]
			,'bucketCols': [('<colname>', '<coltype>')]
			}
	"""
	retdict = {}
	command2run = 'http://' + hcaturi + '/templeton/v1/ddl/database/' + dbname + '/table/' + tablename + '?user.name=' + username + '&format=extended'
	resp = _runcommand(command2run)
	retdict['tableType'] = resp['tableType']
	retdict['inputFormat'] = resp['inputFormat']
	retdict['outputFormat'] = resp['outputFormat']
	retdict['columns'] = _retcoltuples(resp['columns'])
	retdict['partitionColumns'] = _retcoltuples(resp['partitionColumns'])
	retdict['bucketCols'] = _retcoltuples(resp['sd']['bucketCols'])
	return retdict