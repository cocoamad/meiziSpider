#!usr/bin/env
# -*- coding: utf-8 -*- 

#filename 正则表达式

import re

req_tag_url = r'(?<=a href=").*?(?=target)'
req_tag_name = r'(?<=title=).*(?=)'

req_tag_page_level_1 = r'(?<=div id="wp_page_numbers">).*?(?=</div>)'
req_tag_page_level_2 = r'(?<=<li>).*?(?=</li>)'
req_tag_page_level_3 = r'(?<=<a href=\').*?(?=\'>)'

req_page_items_container = r'(?<=li class="wp-item").*?(?=</li>)'
req_page_item_cover_url = r'(?<=img src=").*?(?=")'
req_page_item_url = r'(?<=href=").*?(?=">)'
req_page_item_title_1 = r'(?<=b>).*?(?=</b>)'
req_page_item_title_2 = r'(?<=alt=").*?(?=">)'

req_picture_item_container = r'(?<=div id="picture").*?(?=</div>)'
req_picture_item_image = r'(?<=img alt=).*?(?=>)'
req_picture_item_image_title = r'(?<=").*?(?=")'
req_picture_item_image_url = r'(?<=src=").*?(?=")'

re.compile(req_tag_url)
re.compile(req_tag_name)
re.compile(req_tag_page_level_1)
re.compile(req_tag_page_level_2)
re.compile(req_tag_page_level_3)

re.compile(req_page_items_container)
re.compile(req_page_item_cover_url)
re.compile(req_page_item_url)
# re.compile(req_page_item_title_1)
# re.compile(req_page_item_title_2)

# re.compile(req_picture_item_container)
# re.compile(req_picture_item_image)
# re.compile(req_picture_item_image_title)
# re.compile(req_picture_item_image_url)

