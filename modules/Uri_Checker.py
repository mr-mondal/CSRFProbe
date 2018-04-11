#!/usr/bin/env python2
#-*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import urlparse
import re
from colors import *

def buildUrl(url, href):

	if re.search('logout',href) or re.search('action=out',href) or re.search('action=logoff', href) or re.search('action=delete',href) or re.search('UserLogout',href) or re.search('osCsid', href) or re.search('file_manager.php',href) or href=="http://localhost":#make exclusion list
		return ''
	
	parsed = urlparse.urlsplit(href)
	app=''

	if parsed[1] == urlparse.urlsplit(url)[1]:
		app=href

	else:
		if len(parsed[1]) == 0 and (len(parsed[2]) != 0 or len(parsed[3])!=0):
			domain = urlparse.urlsplit(url)[1]
			if re.match('/', parsed[2]):
				app = 'http://' + domain + parsed[2]
				if parsed[3]!='':
					app += '?'+parsed[3]
			else:
				try:
					app = 'http://' + domain + re.findall('(.*\/)[^\/]*', urlparse.urlsplit(url)[2])[0] + parsed[2]
				except IndexError:
					app = 'http://' + domain + parsed[2]
				if parsed[3]!='':
					app += '?'+parsed[3]

	return app

def buildAction(url, action):

	print O+' [*] Parsing URL parameters...'
	if action!='' and not re.match('#',action):
		return buildUrl(url,action)
	else:
		return url
