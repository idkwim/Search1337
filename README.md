# Search1337

# Installation guide
    root@root:~/Desktop# cd 1337
    root@root:~/Desktop/1337# python setup.py install
    running install
    Checking .pth file support in /usr/local/lib/python2.7/dist-packages/
    /usr/bin/python -E -c pass
    TEST PASSED: /usr/local/lib/python2.7/dist-packages/ appears to support .pth files
    running bdist_egg
    running egg_info
    creating cmdline_search1337.egg-info
    writing cmdline_search1337.egg-info/PKG-INFO
    writing top-level names to cmdline_search1337.egg-info/top_level.txt
    writing dependency_links to cmdline_search1337.egg-info/dependency_links.txt
    writing entry points to cmdline_search1337.egg-info/entry_points.txt
    writing manifest file 'cmdline_search1337.egg-info/SOURCES.txt'
    reading manifest file 'cmdline_search1337.egg-info/SOURCES.txt'
    writing manifest file 'cmdline_search1337.egg-info/SOURCES.txt'
    installing library code to build/bdist.linux-i686/egg
    running install_lib
    running build_py
    creating build
    creating build/lib.linux-i686-2.7
    creating build/lib.linux-i686-2.7/1337
    copying 1337/useragent.py -> build/lib.linux-i686-2.7/1337
    copying 1337/__init__.py -> build/lib.linux-i686-2.7/1337
    copying 1337/call.py -> build/lib.linux-i686-2.7/1337
    copying 1337/day1337.py -> build/lib.linux-i686-2.7/1337
    copying 1337/helper.py -> build/lib.linux-i686-2.7/1337
    creating build/bdist.linux-i686
    creating build/bdist.linux-i686/egg
    creating build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/useragent.py -> build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/__init__.py -> build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/call.py -> build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/day1337.py -> build/bdist.linux-i686/egg/1337
    copying build/lib.linux-i686-2.7/1337/helper.py -> build/bdist.linux-i686/egg/1337
    byte-compiling build/bdist.linux-i686/egg/1337/useragent.py to useragent.pyc
    byte-compiling build/bdist.linux-i686/egg/1337/__init__.py to __init__.pyc
    byte-compiling build/bdist.linux-i686/egg/1337/call.py to call.pyc
    byte-compiling build/bdist.linux-i686/egg/1337/day1337.py to day1337.pyc
    byte-compiling build/bdist.linux-i686/egg/1337/helper.py to helper.pyc
    creating build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/PKG-INFO -> build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/SOURCES.txt -> build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/dependency_links.txt -> build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/entry_points.txt -> build/bdist.linux-i686/egg/EGG-INFO
    copying cmdline_search1337.egg-info/top_level.txt -> build/bdist.linux-i686/egg/EGG-INFO
    zip_safe flag not set; analyzing archive contents...
    creating dist
    creating 'dist/cmdline_search1337-0.1-py2.7.egg' and adding 'build/bdist.linux-i686/egg' to it
    removing 'build/bdist.linux-i686/egg' (and everything under it)
    Processing cmdline_search1337-0.1-py2.7.egg
    removing '/usr/local/lib/python2.7/dist-packages/cmdline_search1337-0.1-py2.7.egg' (and everything under it)
    creating /usr/local/lib/python2.7/dist-packages/cmdline_search1337-0.1-py2.7.egg
    Extracting cmdline_search1337-0.1-py2.7.egg to /usr/local/lib/python2.7/dist-packages
    cmdline-search1337 0.1 is already the active version in easy-install.pth
    Installing search1337 script to /usr/local/bin
    
    Installed /usr/local/lib/python2.7/dist-packages/cmdline_search1337-0.1-py2.7.egg
    Processing dependencies for cmdline-search1337==0.1
    Finished processing dependencies for cmdline-search1337==0.1
    
# Help
    root@root:~/Desktop# search1337
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

# Usage Type
      root@root:~/Desktop# search1337 --e ProFTP
      ProFTPd 1.3.5 - Remote Command Execution Exploit
      http://1337day.com/exploit/23544
      
      ProFTPd 1.3.5 - File Copy Vulnerability
      http://1337day.com/exploit/23509
      
      This exploit is private, cant get name.
      http://1337day.com/exploit/21719
      
      ProFTPD 1.3.3c compromised source remote root Trojan
      http://1337day.com/exploit/15026
      
      ProFTPD IAC Remote Root Exploit
      http://1337day.com/exploit/14761
      
      ..
      ..
      ..
      ProFTPD 1.2.0(rc2) (memory leakage example) Exploit
      http://1337day.com/exploit/5811
      
      root@root:~/Desktop# 






