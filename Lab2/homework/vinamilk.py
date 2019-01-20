from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")

# f = open("vinamilk.html", "wb")
# f.write(raw_data)
# f.close()

soup = BeautifulSoup(content, "html.parser")
table = soup.find("table", id="tableContent")

tr_list = table.find_all("tr")
table_list = []

for tr in tr_list:
    td_list = tr.find_all("td", "b_r_c")
    for td in td_list:
        td = td.string
        data = {
            "": td
        }
        table_list.append(OrderedDict(data))