#! /usr/bin/env python
from day1337 import *
from helper import *


def main():
	HelpMan()
	parser = optparse.OptionParser()
	parser.add_option('--e', action="store")
	parser.add_option('--cve', action="store")
	options, args = parser.parse_args()

	if not options.e:
		HelpMan().usage()

	if options.e:
		if options.cve:
			B3mB4m( str(options.e), str(options.cve)).check()
		else:
			B3mB4m( str(options.e)).check()
