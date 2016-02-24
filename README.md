**hcat-py**
==============
Returns metadata for objects in HCatalog as Python objects

Dependencies
--------------
- Python 2.6.x or above
- HCatalog accessible via WebHCat

Usage
--------------
NAME
    hcat

FILE
    hcat.py

FUNCTIONS
    describe(hcaturi, tablename, dbname='default', username='hdfs')
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

    showdatabases(hcaturi, username='hdfs')
        hcat.showdatabases

        Args:
                hcaturi (str): uri for webhcat host, eg hive.myorg.com:50111
                username (Optional[str]): user name, defaults to 'hdfs'
        Returns:
                list: list of available hcat databases

    showtables(hcaturi, dbname='default', username='hdfs')
        hcat.showtables

        Args:
                hcaturi (str): uri for webhcat host, eg hive.myorg.com:50111
                dbname (Optional[str]): database name, defaults to 'default'
                username (Optional[str]): user name defaults to hdfs
        Returns:
                list: list of available tables for the specified hcat database
				
