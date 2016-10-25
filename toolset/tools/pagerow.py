import labcsv

class PageRow(object):
	"""
		Standard representation of a row in a lab day Page CSV file, for reading and writing to file.
	"""
	page_fields = ["id","record","sequence","page number","group","thumb","zoom","illustrations"]
	entries = {field:"" for field in page_fields}

	def __init__(self,fields=None):
		"""
			The fields parameter can be used to populate the PageRow from the fields read in 
			from a Publication CSV file. If no fields are provided an empty PageRow will be created.
		"""
		if fields != None:
			self.entries['id'] = fields['id']
			self.entries['record'] = fields['record']
			self.entries['page number'] = fields['page number']
			self.entries['group'] = fields['group']
			self.entries['thumb'] = fields['thumb']
			self.entries['zoom'] = fields['zoom']
			self.entries['illustrations'] = labcsv.split_field_list(fields['illustrations']