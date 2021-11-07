import os
import time
import datetime
import argparse
from strings import xml_file, xml_item

parser = argparse.ArgumentParser(description='Generate an rss file from a folder.')
parser.add_argument('path',
                    type=str,
                    help='Path to the folder to generate the RSS file from')
parser.add_argument('title',
                    type=str,
                    help='Title of the feed')
parser.add_argument('description',
                    type=str,
                    help='Description of the feed')
parser.add_argument('root_link',
                    type=str,
                    help='Root link of the website')

args = parser.parse_args()

file_times = {}
# read from a folder
for path, dirs, files in os.walk(args.path):
    for f in files:
        filepath = path + "/" + f
        filename = f.split(".")[0]
        file_times[filepath] = {}
        file_times[filepath]["file"] = filename
        for line in open(filepath, "r"):
            if line.startswith("date"):
                file_times[filepath]["time"] = datetime.date.fromisoformat(line.split(" ")[1])
                file_times[filepath]["date"] = "/".join(line.split(" ")[1].split("-"))
            if line.startswith("description"):
                file_times[filepath]["description"] = " ".join(line.split(" ")[1:]).rstrip()
            if line.startswith("title"):
                file_times[filepath]["title"] = " ".join(line.split(" ")[1:]).rstrip()
    break

print(file_times)
# for everything in the folder
xml_items = []
for file_time in file_times.values():
    date_time = file_time["time"].strftime("%a, %d %b %Y")
    xml_items.append(xml_item.format(root_link=args.root_link + "/", item_link=file_time["date"] + "/" + file_time["file"] + "/", title=file_time["title"], description=file_time["description"], datetime=date_time))

print(xml_items)

# write things to a file

todays_date = datetime.datetime.today().strftime("%a, %d %b %Y")
fileout = xml_file.format(title=args.title, description=args.description, root_link=args.root_link, todays_date=todays_date, items="".join(xml_items))

f = open(f"rss.xml","w") 
f.write(fileout)
f.close()
