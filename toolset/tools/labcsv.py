"""
 Utility methods that can be used to serialise and deserialise internal field structures
 within Publication and Page CSV files.
"""

import re
def join_field_list(fields):
	"""
		Join a list of entries into one field.
	"""
	return str.join("|",fields)

def split_field_list(field):
	"""
		Split a list of entries from a field into a list.
	"""
	fields = field.rstrip(" ").rstrip("|").split("|")
	cleansed_fields = []
	for field in fields:
		if field != "" and field != " ":
			cleansed_fields.append(field)
	return cleansed_fields 

def split_typed_field_list(field):
	"""
		Split a list of typed entries from a field into a list
	"""
	typed_fields = []
	fields =  split_field_list(field)
	for field in fields:
		typed_fields.append(to_typed_field(field))
	return typed_fields

def from_typed_field(field):
	"""
		Create a csv representation of a typed field
	"""
	return "["+field['type']+"]"+field['value']

def from_typed_field(type, value):
	"""
		Create a csv representation of a typed field from a type and value
	"""
	return "["+type+"]"+value

def to_typed_field(field):
	"""
		Create a typed field from a csv representation of a typed field
	"""
	type =""
	value = ""
	field_match = re.match("\[(.*)\](.*)",field.strip())
	if field_match != None:
		if field_match.group(1) != None:
			type = field_match.group(1)
		if field_match.group(2) != None:
			value = field_match.group(2)
	else:
		value = field
	return {"type":type,"value":value}
