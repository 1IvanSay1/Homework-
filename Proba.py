# import xml.etree.ElementTree as ET

# parser = ET.XMLParser(encoding = "utf-8")
# tree = ET.parse("D:\IT\Проекты\Домашки\khkh.xml", parser)
# print(tree)
# root = tree.getroot()
# print(root.tag)
# print(root.text)
# print(root.attrib)

# # news_list = root.findall("channel/item")
# # print(f' В этом файле {len(news_list)} новостей')

# # for i in news_list:
# #     title = i.find("title")
# #     print(title.text)

# title_list = root.findall("channel/item/title")
# for title in title_list:
#     print(title.text)

# tree.write("D:\IT\Проекты\Домашки\khkh.xml", encoding="utf-8")
# import json
# d = {"hello": "python", "goodbye": 'java'}
# result = json.dumps(d)
# print(result)



# import json
# from collections import Counter
# # def read_json(file_path, word_max_len=6, top_words_amt=10):
# with open(r"D:\IT\Проекты\Домашки\newsafr.json", encoding="utf - 8", newline='') as f:
#     json_a = json.load(f)
# new_list = json_a["rss"]["channel"]["items"]
# popular = []
# for news in new_list:
#     name = [i for i in news["description"].split(' ') if len(i) > 6]
#     popular.extend(name)
#     popular = list(popular)
# top_10 = Counter(popular).most_common()
# print(top_10)


# from collections import Counter
# import xml.etree.ElementTree as ET
# parser = ET.XMLParser(encoding = "utf-8")
# tree = ET.parse(r"D:\IT\Проекты\Домашки\newsafr.xml", parser)
# root = tree.getroot()
# # print(root.tag)
# # print(root.text)
# # print(root.attrib)
# news_list = root.findall('channel/item')
# # popular = []
# for news in news_list:
#     title = news.find('title')
#     print(title.text)
#     name = [i for i in news.find("description").split(' ') if len(i) > 6]
#     popular.extend(name)
# popular = list(popular)
# words_counter = Counter(popular)
# top_10 = [w[0] for w in words_counter.most_common(10)]
# # print(top_10)