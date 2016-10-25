from fieldaggregator import FieldAggregator

class PublicationPlaceAggregator(FieldAggregator):
	"""
		PublicationPlaceAggregator subclasses FieldAggregator and provides
		methods for aggregating the 'publication places' field in a Publication CSV file
	"""
	def aggregate_field(self, file, field="publication places"):
		"""
			Calls the aggregate_field super method with 'publication places' as the field to
			aggregate on.
		"""
		return super(DimensionsAggregator, self).aggregate_field(file,field)

	def normalise_value(self, value):
		"""
			Overrides the super method, to normalise the value specific to the 'publication places'
			column by stripping any leading or trailing whitespace.
		"""
		return value.lstrip().rstrip()
