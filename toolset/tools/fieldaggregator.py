from publicationcsvreader import PublicationCSVReader
import operator

class FieldAggregator(object):
	"""
		Provides methods for aggregating the values of a given field within
		a Publication CSV File
	"""
	def aggregate_field(self, file, field):
		"""
			Builds a map of values and number of appearances for 
			a given column in the file
		"""
		field_map = {}
		publication_csv_reader = PublicationCSVReader(file)
		while(True):
			row = publication_csv_reader.next()
		
			if row == None:
				break
			field_values = row.entries[field]
			for field_value in field_values:
				field_value = self.normalise_value(field_value)
				if field_value in field_map:
					field_map[field_value] +=1
				else:
					field_map[field_value] = 1
		publication_csv_reader.close()
		return field_map

	def normalise_value(self, value):
		"""
			Method can be overridden by subclasses to normalise the field 
			values specific to the field of interest.
		"""
		return value

	def sort_aggregated_fields(self,aggregated_fields):
		"""
			Returns the aggregated_fields dictionary reverse sorted by key
		"""
		return sorted(aggregated_fields.items(), key=operator.itemgetter(1), reverse=True)


