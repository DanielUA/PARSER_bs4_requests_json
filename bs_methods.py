# import re
#
# from bs4 import BeautifulSoup
#
# with open("blank/index2.html", mode = "r") as file:
#     src = file.read()
#
# soup=BeautifulSoup(src, "lxml")
# #
# # user_name = soup.find("div", class_ = "user__name").find("span").text
# # print(user_name)
# # birthday = soup.find("div", class_ = "user__birth__date").find_all("span")
# # for i in birthday:
# #     print(i.text)
# # user_name = soup.find("div", {"class": "user__info"}).find("span").text
# # # print(user_name)
# # find_all_span_in_class = soup.find(class_="user__info").find_all("span")
# # print((find_all_span_in_class))
# # for i in find_all_span_in_class:
# #     print(i.text)
#
# # social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# # print(social_links[0].text)
# # social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# # print(social_links)
# # all_a = soup.find_all('a')
# # print(all_a)
# # for i in all_a:
# #     item_text = i.text
# #     item_url = i.get("href")
# #     print(item_url)
# #     print(item_text)
#
# # find_block = soup.find(class_="post__text").find_parent()
# # print(find_block)
# # next_el = soup.find(class_="post__title").next_element.next_element.text
# # find_el = soup.find(class_="post__title").find_next().text
# # print(next_el)
# # print(find_el)
#
# # next_sib = soup.find(class_="post__title").find_next_sibling()
# # print(next_sib)
#
# link = soup.find(class_="some__links").find_all("a")
# # print(link)
# #
# # for i in link:
# #     link_href = i.get("href")
# #     en_link_href = i["href"]
# #     link_attr = i.get("data-attr")
# #     print(link_href)
# #     print(en_link_href)
# #     print(link_attr)
#
# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text.text)
# find_all_text = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_all_text)


