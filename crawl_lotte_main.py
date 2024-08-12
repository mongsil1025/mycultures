from bs4 import BeautifulSoup
import requests


url = "https://culture.lotteshopping.com/getRecommendationClassList.ajax"
response = requests.post(url=url, data={"path": "recommendation", "orderSet": "F"})

soup = BeautifulSoup(response.text, "html.parser")
class_list = soup.select("div.swiper-slide.card_list_v")


class CultureClass:
    def __init__(
        self, title, img, status, location, dimension, teacher_type, time, price
    ):
        self.title = title
        self.img = img
        self.status = status
        self.location = location
        self.dimension = dimension
        self.teacher_type = teacher_type
        self.time = time
        self.price = price


cc_list = []

for _class in class_list:
    link = _class.select_one("a")["href"]
    img = _class.select_one("a > div.img_resize_w > img")["src"]
    status = _class.select_one("div.con > div > p:nth-child(1)").get_text().strip()
    location = _class.select_one("div.con > div > p:nth-child(2)").get_text().strip()
    title = _class.select_one("div.con > p.tit").get_text().strip().strip()
    dimension = (
        _class.select_one("div.con > div.info_con > div > p:nth-child(1)")
        .get_text()
        .strip()
    )
    teacher_type = (
        _class.select_one("div.con > div.info_con > div > p:nth-child(2)")
        .get_text()
        .strip()
    )
    time = (
        _class.select_one("div.con > div.info_con > p.time").get_text().strip().strip()
    )
    price = _class.select_one("div.bottom_info > p.price").get_text().strip().strip()
    cc_list.append(
        CultureClass(title, img, status, location, dimension, teacher_type, time, price)
    )

for cc in cc_list:
    print(cc.__dict__)
