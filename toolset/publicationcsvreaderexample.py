"""
	Example usage of a PublicationCSVReader. Reads the input publication CSV file 
	and iterates through the rows, printing the publication id and summary title.

"""

from tools.publicationcsvreader import PublicationCSVReader
import config.publicationcsvreaderexample_config as config

publication_csv_reader = PublicationCSVReader(config.paths['input_file'])

while(True):
	row = publication_csv_reader.next()
	if row == None:
		break
	print "["+row.entries['id'] + "] " + row.entries['summary title']
publication_csv_reader.close()