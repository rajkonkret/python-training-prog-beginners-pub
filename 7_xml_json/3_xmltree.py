import xml.etree.ElementTree as ET

document: ET = ET.parse("slideshow.xml")
print(document.findall("slide")[0].attrib["colour"])
slide_list = document.findall("slide")
for slide in slide_list:
    # print(slide.findall("title"))  # zwróci wszystkie węzły o tagu title
    # print(slide.find("title"))  # zwróci pierwszy
    # print(slide.find("not_found"))  # zwróci None, ponieważ takiego tagu nie mamy
    print(slide.find("title").text)

print(document.findall(".//title"))  # zwróci wszystkie węzły o tagu title na dowolnym poziomie zagnieżdżenia
