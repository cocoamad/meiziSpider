#!usr/bin/env
# -*- coding: utf-8 -*- 

#filename 妹子图

import re
import urllib
import threading
import regx
import os

g_root_url = "http://www.meizitu.com"
g_page_url = "http://www.meizitu.com/a/"

g_root_path = os.getcwd()
g_download_root_name = "meizitu/"


class PicItem(object):
	def __init__(self, title, url, path):
		self.title = title
		self.url = url
		self.download(path)

	def download(self, path):
		urllib.urlretrieve(self.url, '%s/%s.png' % (path, self.title))
		print self.title + "downloaded!"


class PageItem(object):
	"""dd"""
	def __init__(self, html, tag_name):
		# 封面title
		self.title = ""
		# 封面url
		self.cover_url = ""
		# item url
		self.page_url = ""
		# 所有的图片items
		self.pic_items = []

		self.tag_name = tag_name

		self.parseItem(html)

	def parseItem(self, html,):
		if html:
			m = re.search(regx.req_page_item_title_1, html, re.S)
			if m:
				self.title = m.group(0).decode('gbk').encode('utf-8')
			else:
				m = re.search(regx.req_page_item_title_2, html, re.S)
				if m:
					self.title = m.group(0).decode('gbk').encode('utf-8')

					self.path = g_download_root_name + self.tag_name + "/" + self.title
					if os.path.exists(self.path) == False:
						os.mkdir(self.path)

				m = re.search(regx.req_page_item_cover_url, html, re.S)
				if m:
					self.cover_url = m.group(0)

				m = re.search(regx.req_page_item_url, html, re.S)
				if m:
					self.page_url = m.group(0)

				if self.page_url:
					self.parseItemUrl(self.page_url)

	def parseItemUrl(self, url):
		html = urllib.urlopen(url).read()
		m = re.search(regx.req_picture_item_container, html, re.S)
		if m:
			pics = re.findall(regx.req_picture_item_image, m.group(0), re.S)
			if pics is not None:
				for str in pics:
					m = re.search(regx.req_picture_item_image_title, str, re.S)
					n = re.search(regx.req_picture_item_image_url, str, re.S)
					if m and n:
						title = m.group(0).decode('gbk').encode('utf-8')
						url = n.group(0)
						item = PicItem(title,url, self.path)
						self.pic_items.append(item)


class Tag(object):
	"""for tag"""
	def __init__(self, html):
		#保存所有的子页面
		self.urls = []
		#保存所有的子页面包含的图片组PageItem
		self.items = []

		# tag名字
		self.name = ""

		self.parseTagNameAndUrls(html)

	def parseTagNameAndUrls(self, html):
		url_result = re.search(regx.req_tag_url, html, re.S)
		if url_result:
			name_result = re.search(regx.req_tag_name, html, re.S)
			if name_result:
				self.name = name_result.group(0).decode('gbk').encode('utf-8').replace('"', '')
				if os.path.exists(g_download_root_name + self.name) == False:
					os.mkdir(g_download_root_name + self.name)
				url = url_result.group(0).replace('"','')
				if url:
					self.urls = self.parseAllPageUrl(url)
					for url in self.urls:
						items = self.parsePicItem(url)
						self.items.append(items)
			else:
				print "found tag name error"
		else:
			print "found tag error"

	def parseAllPageUrl(self, url):
		urls = [url]
		tagPage = urllib.urlopen(url)
		tagPageHtml = tagPage.read()
		m = re.search(regx.req_tag_page_level_1, tagPageHtml, re.S)
		if m:
			m = re.findall(regx.req_tag_page_level_2, m.group(0), re.S)
			if m:
				for subPage in m:
					n = re.search(regx.req_tag_page_level_3, subPage, re.S)
					if n:
						urls.append(g_page_url + n.group(0))
		else:
			print "find tag sub page error"
		return urls

	def parsePicItem(self, url):
		items = []
		html = urllib.urlopen(url).read()
		m = re.findall(regx.req_page_items_container, html, re.S)
		if m:
			for str in m:
				item = PageItem(str, self.name)
				items.append(item)
		return items

		
def findAllTags(url):
	tags = []
	rootPage = urllib.urlopen(g_root_url)
	rootHtml = rootPage.read()
	req = r'(?<=div class="tags">).*?(?=</div>)'
	re.compile(req)
	m = re.search(req, rootHtml, re.S)
	if m:
		if os.path.exists(g_download_root_name) == False:
			os.mkdir(g_download_root_name)

		req = r'(?<=a>).*?(?=>)'
		re.compile(req)
		tagList = re.findall(req, m.group(0), re.S)
		if m:
			for str in tagList:
				tag = Tag(str)
				tags.append(tag)
		else:
			print "found sub tag error"
	else:
		print "found  error"
	return tags

if __name__ == '__main__':
	tags = findAllTags(g_root_url)
