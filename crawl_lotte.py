import requests
from bs4 import BeautifulSoup

url = "https://culture.lotteshopping.com/application/search/view.do?brchCd=0001&yy=2024&lectSmsterCd=3&lectCd=0410"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
fix_box_area = soup.select_one(
    "#wrap > div.cont_wrap > div > div.page_cont_area.no_padding > div.bg_inner.pd_bot > div.inner > div.right_box_fix_area.anchor_func_area > div > div > div"
    # "> div.pin-spacer > div > div > div.shadow_div > div:nth-child(1) > div.pop_wrap > div > div.for_padding > div > div.pop_head > div.tit_box > div > p.tit.lectNm"
)
pop_head = fix_box_area.select_one(
    "div > div:nth-child(1) > div.pop_wrap > div.pop_cont > div.for_padding > div.scroll_area > div.pop_head"
)
box_con = fix_box_area.select_one(
    "div > div:nth-child(1) > div.pop_wrap > div.pop_cont > div.for_padding > div.scroll_area > div.box_con > div.content_area > div.anchor_con > div.data_box > div.selected_info"
)

status = pop_head.select_one("div.top_area > div.label_div > p:nth-child(1)").get_text()
type = pop_head.select_one("div.top_area > div.label_div > p:nth-child(2)").get_text()

title = pop_head.select_one("div.tit_box > div > p:nth-child(1)").get_text()
subtitle = pop_head.select_one("div.tit_box > div > p:nth-child(2)").get_text()

print(f"{status} > {type}")
print(f"{title} > {subtitle}")
print("\n")

location = box_con.select_one("dl:nth-child(1) > dd").get_text().strip()
type = box_con.select_one("dl:nth-child(2) > dd").get_text().strip()
term = box_con.select_one("dl:nth-child(3) > dd").get_text().strip()
teacher = box_con.select_one("dl:nth-child(4) > dd").get_text().strip()
period = box_con.select_one("dl:nth-child(5) > dd").get_text().strip()
time = box_con.select_one("dl:nth-child(6) > dd").get_text().strip()
number_of_lectures = box_con.select_one("dl:nth-child(7) > dd").get_text().strip()
class_room = box_con.select_one("dl:nth-child(8) > dd").get_text().strip()
price = box_con.select_one("dl:nth-child(9) > dd").get_text().strip()
target_class = box_con.select_one("dl:nth-child(10) > dd").get_text().strip()
acceptance_period = box_con.select_one("dl:nth-child(11) > dd").get_text().strip()
contact = box_con.select_one("dl:nth-child(12) > dd").get_text().strip()
print(f"{location} | {type} | {term} | {teacher}")
print(f"{period} | {time} | {number_of_lectures} | {class_room} | {price}")
print(f"{target_class} | {acceptance_period} | {contact}")
