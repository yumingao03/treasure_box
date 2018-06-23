#!/usr/bin/python
#coding:utf8

import sys
import json
import urllib
import urllib2
import time

reload(sys)
sys.setdefaultencoding("utf8")

def request(url):
	res = None
	try:
		res = urllib2.urlopen(url).read()
	except Exception,e:
		pass
	return res

def get_value(text, start_delim, end_delim):
	start = text.find(start_delim)
	if start == -1:
		return None
	end = text.find(end_delim, start + len(start_delim))
	if end == -1:
		ret = text[start+len(start_delim):]
	else:
		ret = text[start+len(start_delim) : end]
	return ret

def json_decode(text, coding='utf8'):
	ret = {}
	try:
		ret = json.loads(text, encoding=coding)
	except Exception,e:
		print e
		pass
	return ret

def json_encode(text, coding='utf-8'):
	ret = None
	try:
		ret = json.dumps(text, encoding="utf-8", ensure_ascii=true)
	except Exception,e:
		print e
		pass
	return ret
	

def url_unquote(term):
	ret = urllib.unquote(term)
	return ret

def url_quote(term):
	ret = urllib.quote(term)
	return ret

def json_encode(js):
	text = json.dumps(js,ensure_ascii=False)
	return text
