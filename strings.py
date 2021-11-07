xml_file = '''
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
   <channel>
      <title>{title}</title>
      <description>{description}</description>
      <link>{root_link}</link>
      <lastBuildDate>{todays_date}</lastBuildDate>
      {items}
   </channel>
</rss>
'''

xml_item = '''
      <item>
         <link>{root_link}{item_link}</link>
         <title>{title}</title>
         <description>{description}</description>
         <pubDate>{datetime}</pubDate>
      </item>
'''
