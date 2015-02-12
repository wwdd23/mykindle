#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: create-mobi.py
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2015-02-04 20:21:48
############################




TEMPLATES = {}
TEMPLATES['content.html'] = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
    <title>{{ user }}'s kindle reader</title>
    <style type="text/css">
    body{
        font-size: 1.1em;
        margin:0 5px;
    }

    h1{
        font-size:4em;
        font-weight:bold;
    }

    h2 {
        font-size: 1.2em;
        font-weight: bold;
        margin:0;
    }
    a {
        color: inherit;
        text-decoration: inherit;
        cursor: default
    }
    a[href] {
        color: blue;
        text-decoration: underline;
        cursor: pointer
    }
    p{
        text-indent:1.5em;
        line-height:1.3em;
        margin-top:0;
        margin-bottom:0;
    }
    .italic {
        font-style: italic
    }
    .do_article_title{
        line-height:1.5em;
        page-break-before: always;
    }
    #cover{
        text-align:center;
    }
    #toc{
        page-break-before: always;
    }
    #content{
        margin-top:10px;
        page-break-after: always;
    }
    </style>
</head>
<body>
    <div id="cover">
        <h1 id="title">{{ user }}'s kindle reader</h1>
        <a href="#content">Go straight to first item</a><br />
        {{ mobitime.strftime("%m/%d %H:%M") }}
    </div>
    <div id="toc">
        <h2>Feeds:</h2> 
        <ol> 
            {% set feed_count = 0 %}
            {% set feed_idx=0 %}
            {% for feed in feeds %}
            {% set feed_idx=feed_idx+1 %}
            {% if len(feed['entries']) > 0 %}
            {% set feed_count = feed_count + 1 %}
            <li>
              <a href="#sectionlist_{{ feed_idx }}">{{ feed['title'] }}</a>
              <br />
              {{ len(feed['entries']) }} items
            </li>
            {% end %}
            
            {% end %}
        </ol> 
        
        {% set feed_idx=0 %}
        {% for feed in feeds %}
        {% set feed_idx=feed_idx+1 %}
        {% if len(feed['entries']) > 0 %}
        <mbp:pagebreak />
        <div id="sectionlist_{{ feed_idx }}" class="section">
            {% if feed_idx < feed_count %}
            <a href="#sectionlist_{{ feed_idx+1 }}">Next Feed</a> |
            {% end %}
            
            {% if feed_idx > 1 %}
            <a href="#sectionlist_{{ feed_idx-1 }}">Previous Feed</a> |
            {% end %}
        
            <a href="#toc">TOC</a> |
            {{ feed_idx }}/{{ feed_count }} |
            {{ len(feed['entries']) }} items
            <br />
            <h3>{{ feed['title'] }}</h3>
            <ol>
                {% for item in feed['entries'] %}
                <li>
                  <a href="#article_{{ feed_idx }}_{{ item['idx'] }}">{{ item['title'] }}</a><br/>
                  {% if item['published'] %}{{ item['published'] }}{% end %}
                </li>
                {% end %}
            </ol>
        </div>
        {% end %}
        {% end %}
    </div>
    <mbp:pagebreak />
    <div id="content">
        {% set feed_idx=0 %}
        {% for feed in feeds %}
        {% set feed_idx=feed_idx+1 %}
        {% if len(feed['entries']) > 0 %}
        <div id="section_{{ feed_idx }}" class="section">
        {% for item in feed['entries'] %}
        <div id="article_{{ feed_idx }}_{{ item['idx'] }}" class="article">
            <h2 class="do_article_title">
              {% if item['url'] %}
              <a href="{{ item['url'] }}">{{ item['title'] }}</a>
              {% else %}
              {{ item['title'] }}
              {% end %}
            </h2>
            {{ feed['title'] }}
            <br />
            {% if item['author'] %}{{ escape(item['author']) }}{% end %}   {% if item['published'] %}{{ item['published'] }}{% end %}
            
            <div>{{ item['content'] }}</div>
        </div>
        {% end %}
        </div>
        {% end %}
        {% end %}
    </div>
</body>
</html>
"""





