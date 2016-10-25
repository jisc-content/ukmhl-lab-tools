from labcsvreader import LabCSVReader
from pagerow import PageRow
class PageCSVReader(LabCSVReader):
	"""
		Subclasses LabCSVReader and provides methods for reading the rows
		of a Page CSV File into PageRow instances.
	"""
    def __init__(self,csv_filename):
        super(PageCSVReader, self).__init__(csv_filename)

    def get_row(self,row):
		page_row = PageRow(row)
		return page_row