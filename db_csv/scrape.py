import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np

def scraping(i):
    url = "https://wikiwiki.jp/taiko-fumen/%E5%8F%8E%E9%8C%B2%E6%9B%B2/%E5%B9%B3%E5%9D%87%E5%AF%86%E5%BA%A6%E9%A0%86/%E3%81%8A%E3%81%AB/%E2%98%85%C3%97"
    r = requests.get(url + str(i))
    html_soup = BeautifulSoup(r.text,'html.parser')

    title=[]
    combo = []
    time = []
    density = []
    bpm_max = []
    bpm_min = []
    link=[]

    for head in html_soup.find_all(id="h3_content_1_1"):
        if "新筐体収録曲" in head.text:
            for table in html_soup.find(class_="h-scrollable"):
                for tr in table.find_all("tbody"):
                    for td in tr.find_all("tr"):
                        for item in td.find_all("td"):
                            if "ピコピコ ルイン" in item.text:
                                continue

                            if "*" in item.text[-3:]:
                                text = item.text[:-3]
                            else:
                                text = item.text # 脚注除去

                            if 'class="rel-wiki-page"' in str(item):
                                title.append(text) # 曲名取得
                                for href in item.find_all("a"):
                                    link.append("https://wikiwiki.jp" + str(href.get('href'))) # 攻略リンク取得

                            elif 'text-align:center;' in str(item) and 'colspan=' not in str(item) and 'background' not in str(item):
                                for strong in item:
                                    if "<strong>" in str(strong):
                                        density.append(float(text)) # 平均密度取得
                                    else:
                                        
                                        combo.append(int(text)+1) # コンボ数取得

                            elif 'text-align:right;' in str(item) and 'background' not in str(item):
                                time.append(float(text.replace("秒",""))) # 演奏時間取得

                            elif 'style="width:' in str(item):
                                bpm = text.replace("※", "").replace("?", "").split("-")

                                try:
                                    if len(bpm) == 2:
                                        bpm_max.append(float(bpm[1]))
                                        bpm_min.append(float(bpm[0]))
                                    else:
                                        bpm_max.append(float(bpm[0]))
                                        bpm_min.append(float(bpm[0])) # bpm取得
                                except:
                                        bpm_max.append(0.0)
                                        bpm_min.append(0.0) # bpm取得
    data = np.array([title, combo, time, density, bpm_max, bpm_min, link]).T.tolist()
    df = pd.DataFrame(data)#, columns=["title", "combo", "time", "density", "maxBPM", "minBPM", "link"])

    return df.to_csv(f"./lv{i}_data.csv", header=False, index=False)


for i in range(5,11):
    scraping(i)
    time.sleep(2)