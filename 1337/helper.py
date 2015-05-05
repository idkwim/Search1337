class HelpMan(object):
	def __init__(self):
		try:
			import mechanize
		except:
			print """

You must install mechanize package !

	Tips;	
		1) sudo pip install mechanize
		2) sudo apt-get install python-mechanize
		3) sudo easy_install mechanize

			"""
			import sys
			sys.exit();

	def usage(self):
			print """

 _____     _           _      _ 
|_   _|  _| |_ ___ _ _(_)__ _| |
  | || || |  _/ _ \ '_| / _` | |
  |_| \_,_|\__\___/_| |_\__,_|_|
                                
                     
	python 1337day.py --e [SEARCH TAG]
				
Also you can append CVE number.
	python 1337day.py --e [SEARCH TAG] --cve [CVE]

You must read it, if you dont have any idea about CVE.	
	http://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures


Greetz : KnocKout,curtis Vesselam !
				""";
	def concat(self):
		"""
			b3mb4m@gmail.com

				^_^
		""";	
