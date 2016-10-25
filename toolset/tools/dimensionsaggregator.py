from fieldaggregator import FieldAggregator

class DimensionsAggregator(FieldAggregator):
  """
    DimensionsAggregator subclasses FieldAggregator and provides
    methods for aggregating the 'dimensions' field in a Publication CSV file
  """

  def aggregate_field(self, file, field="dimensions"):
    """
      Calls the aggregate_field super method with 'dimensions places' as the field to
      aggregate on.
    """
    return super(DimensionsAggregator, self).aggregate_field(file,field)

  def normalise_value(self, value):
    """
      Overrides the super method, to normalise the value specific to the 'dimensions'
      column by removing any whitespace in the value
    """
    return value.replace(" ","")


		
