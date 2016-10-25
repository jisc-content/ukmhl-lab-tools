from labcsvreader import LabCSVReader
from publicationrow import PublicationRow
class PublicationCSVReader(LabCSVReader):
	"""
		Subclasses LabCSVReader and provides methods for reading the rows
		of a Publication CSV File into PublicationRow instances.
	"""
	def __init__(self,csv_filename):
		super(PublicationCSVReader, self).__init__(csv_filename,PublicationRow.publication_fields)

	def get_row(self,row):
		publication_row = PublicationRow(row)
		return publication_row
