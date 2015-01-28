#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: readrss.py
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2015-01-24 10:16:37
############################

from lib import feedparser
     
#python_wiki_rss_url = "http://www.python.org/cgi-bin/moinmoin/" \
                              # "RecentChanges?action=rss_rc"
python_wiki_rss_url= "http://wwdd23.github.io/pages/atom.xml"
feed = feedparser.parse( python_wiki_rss_url )

#print feed[ "bozo" ]
#print feed[ "items" ]
print  feed[ "channel" ][ "title" ] 
print feed[ "channel" ][ "link" ]
print feed[]
