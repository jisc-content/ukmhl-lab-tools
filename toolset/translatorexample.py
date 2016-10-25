"""
	Example usage of the PageTranslator. Translates the page text files for 
	each publication listed in the input csv file. English language pages are ignored,
	non-english language texts are translated and output to given output directory.

"""

import config.translatorexample_config as config
from tools.pagetranslator import PageTranslator

page_translator = PageTranslator(config.translator_api['key'])
page_translator.translate_publications(config.paths['working_directory'],
	config.paths['translation_directory'],
	config.paths['input_file'])