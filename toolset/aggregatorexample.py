"""
	Example usage of a field aggregator. Uses a DimensionsAggregator to aggregate an
	input publications CSV file dimensions column, and then uses https://plot.ly
	to plot the results as a pie chart.

	Requires plot.ly credentials - https://plot.ly/python/getting-started/

"""

import config.aggregatorexample_config as config
from tools.dimensionsaggregator import DimensionsAggregator
import plotly.plotly as py
import plotly.graph_objs as go

# Aggregate values in dimension column
dimensions_aggregator = DimensionsAggregator()
aggregated_fields = dimensions_aggregator.aggregate_field(config.paths['input_file'])

# Make API request to Plot.ly to render aggregated values as pie chart

labels = aggregated_fields.keys()
values = aggregated_fields.values()

fig = {
    'data': [{'labels': labels,
              'values': values,
              'type': 'pie'}],
    'layout': {'title': 'Publication dimensions'}
     }

py.plot(fig)
