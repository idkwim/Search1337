from useragent import *
import mechanize
import optparse
import sys
import re


class B3mB4m(object):
	def __init__(self, name=None, cve=None):
		if name != None:
			if cve != None:
				self.url = 'http://1337day.com/search?search_request=%s&search_type=1&category=-1&platform=-1&price_from=0&price_to=10000&author_login=&cve=%s' % (str(name), str(cve))
			else:
				self.url = 'http://1337day.com/search?search_request=%s&search_type=1&category=-1&platform=-1&price_from=0&price_to=10000&author_login=&cve=' % (str(name))
	def check(self):
		br = mechanize.Browser()
		br.set_handle_robots(False) 
		br.addheaders = [('User-agent', useragent.agents)]
		try:  	      	
			data = br.open("http://1337day.com/webapps")
		except:
			print "Site seems like down."
			sys.exit()	

		for form in br.forms():
		    br.select_form(nr=0)
		    for control in br.form.controls:
		    	if control != None:
			    	if control.name == "agree":
			    		br.submit()		
				
		data = br.open(self.url)
		search = re.findall("'/exploit/description/\S+'", data.read())


		if not search: #Empty ..
			print "Exploit Not Found ..";
		else:	
			for i in search:
				cut = i.replace("'", "").replace("/description", "")
				cut = "http://1337day.com" + cut
				data = br.open(cut)
				searchtitle = re.search('<title>(.*)</title>', data.read(), re.IGNORECASE).group(1)
				if searchtitle:
					if "private exploit" in searchtitle:
						print "This exploit is private, cant get name."
					else:	
						print searchtitle
				print "%s\n" % str(cut)





