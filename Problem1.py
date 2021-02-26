import tkinter as tk
from tkinter import ttk,messagebox
import requests
import bs4
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import Select

def taskToDo():
    if ProductEntry.get() == "" or PincodeEntry.get().isnumeric()==False or len(PincodeEntry.get())!= 6:
        messagebox.showerror("Invalid", "Invalid Product name or Pincode!!!")
    else:
        if maxEntry.get().isnumeric()==False or minEntry.get().isnumeric()==False:
            messagebox.showerror("Invalid","Price range needs to be in integer format!!!")
        else:
            sortText = SortEntry.get()
            numberOfProd = NumEntry.get()
            priceRange = PriceEntry.get()
            pinCode = PincodeEntry.get()
            maxVal = int(maxEntry.get())
            minVal = int(minEntry.get())
            # print(sortText,numberOfProd,priceRange,pinCode)
            time.sleep(10)

        ###DONE
            options = Options()
            ua = UserAgent()
            userAgent = ua.random
            print(userAgent)
            options.add_argument(f'user-agent={userAgent}')
            driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
            time.sleep(1)
            driver.get("https://www.amazon.in/s?k="+ProductEntry.get()+"&ref=nb_sb_noss_2")
            time.sleep(2)

            # Price Sorting NEW
            if PriceEntry.get() != "No limit":
                driver.find_element_by_xpath('//*[@id="low-price"]').send_keys(minVal)
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="high-price"]').send_keys(maxVal)
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="a-autoid-1"]/span/input').click()

            # Normal SORTING
            driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]').click()
            if sortText == "Price: Low to High":
                time.sleep(2)
                driver.find_element_by_xpath(' //*[@id="a-popover-3"]/div/div/ul/li[2]').click()
            elif sortText == "Price: High to Low":
                time.sleep(2)
                driver.find_element_by_xpath(' //*[@id="a-popover-3"]/div/div/ul/li[3]').click()
            elif sortText =="Newest Arrivals":
                time.sleep(2)
                driver.find_element_by_xpath(' //*[@id="a-popover-3"]/div/div/ul/li[5]').click()
            else:
                time.sleep(2)
                driver.find_element_by_xpath(' //*[@id="a-popover-3"]/div/div/ul/li[1]').click()

            #PRICE Sorting OLD
            # if priceRange=="Under Rs.1000":
            #     time.sleep(2)
            #     driver.find_element_by_xpath('//*[@id="p_36/1318503031"]/span/a/span').click()
            # elif priceRange=="Rs.1000 - Rs.5000":
            #     time.sleep(2)
            #     driver.find_element_by_xpath('//*[@id="p_36/1318504031"]/span/a/span').click()
            # elif priceRange=="Rs.5000 - Rs.10000":
            #     time.sleep(2)
            #     driver.find_element_by_xpath('//*[@id="p_36/1318505031"]/span/a/span').click()
            # elif priceRange=="Rs.10000 - Rs.20000":
            #     time.sleep(2)
            #     driver.find_element_by_xpath('//*[@id="p_36/1318506031"]/span/a/span').click()
            # elif priceRange=="Over Rs.20000":
            #     time.sleep(2)
            #     driver.find_element_by_xpath('//*[@id="p_36/1318507031"]/span/a/span').click()
            # else:
            #     print("Rich Boi")


            headers = {
                'User-Agent': 'My User Agent 1.0',
                'From': 'vinaygovekar24@gmail.com'
            }

            url = driver.current_url
            req = requests.get(url, headers=headers)
            soup = bs4.BeautifulSoup(req.text, features="html.parser")

            ###DONE
            Name = soup.select('.a-size-medium.a-color-base.a-text-normal')


            Price = soup.select('.a-price-whole')
            # for i in range(0,len(Price)):
            #     print(Price[i].text)

            ratings = soup.select('.a-popover-trigger.a-declarative')
            timeT = soup.select('.a-row.s-align-children-center')
            AmazonMobileData = []
            for i in range(0, 10):
                # print(Name[i].text)
                # print(ratings[i + 1].text)
                # print(timeT[i + 1].text.lstrip().rstrip().split("Get it by")[-1].split("FREE")[0].rstrip())
                    AmazonMobileData.append([Name[i].text, Price[i].text, "Amazon", ratings[i + 1].text,timeT[i + 1].text.lstrip().rstrip().split("Get it by")[-1].split("FREE")[0].rstrip()])
            #     if ProductEntry.get() == "Mobile" or ProductEntry.get() == "Mobiles" or ProductEntry.get() == "mobile" or ProductEntry.get() == "mobiles":
            #         AmazonMobileData.append([Name[i].text, Price[i + 3].text,"Amazon", ratings[i + 1].text,
            #                                  timeT[i + 1].text.lstrip().rstrip().split("Get it by")[-1].split("FREE")[
            #                                      0].rstrip()])
            #     else:
            #

            link = soup.select('.a-link-normal.a-text-normal')
            m = 0
            for i in range(0, 20, 2):
                linkref = "https://www.amazon.in" + link[i]["href"]
                AmazonMobileData[m].append(linkref)
                m += 1

            df = pd.DataFrame(AmazonMobileData, columns=['Name', 'Price','Source','Rating', 'Delivery', 'Ref Link'])

            # df = pd.read_csv('ScrappedData.csv')
            # AmazonMobileData = df.values.tolist()
            df.to_csv('Problem1and2Solution.csv', index=False)

            FlipkartData = []
            FlipkartUrl = []

            for i in range(0,len(AmazonMobileData)):
                time.sleep(5)
                driver.get("https://www.flipkart.com/")
                try:
                    driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
                except:
                    print(".")
                time.sleep(2)
                # print(AmazonMobileData[i][0].split("(")[0])
                driver.find_element_by_xpath(
                    '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys(
                    AmazonMobileData[i][0].split(")")[0])
                time.sleep(2)
                driver.find_element_by_xpath(
                    '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
                time.sleep(2)
                headers = {
                    'User-Agent': 'My User Agent 1.0',
                    'From': 'vinaygovekar24@gmail.com'
                }
                url = driver.current_url
                time.sleep(2)
                req = requests.get(url, headers=headers)
                soup2 = bs4.BeautifulSoup(req.text, features="html.parser")
                time.sleep(2)
                try:
                    FlipkartPrice = soup2.select('._30jeq3._1_WHN1')
                    FlipkartData.append(FlipkartPrice[0].text)
                    FlipkartUrl.append(driver.current_url)
                except:
                    FlipkartUrl.append("None")
                    FlipkartData.append("20000,00")
                    print("Webpage error")
            print(FlipkartData)
            finalData=AmazonMobileData
            driver.quit()
            try:
                for i in range(len(AmazonMobileData)):
                    if int("".join(FlipkartData[i][1:].split(","))) < int("".join(AmazonMobileData[i][1].split(","))):
                        finalData[i][1]="".join(FlipkartData[i][1:].split(","))
                        finalData[i][2]="Flipkart"
                        finalData[i][5]=FlipkartUrl[i]
                        print("FlipKart better")
                    else:
                        print("Amazon Better")
            except:
                print("Er")
            df2 = pd.DataFrame(finalData, columns=['Name', 'Price','Least Price Source','Rating', 'Delivery', 'Ref Link'])
            df2.to_csv("Problem3Solution.csv",index=False)
            root.quit()

root = tk.Tk()
scrwdth = root.winfo_screenwidth()
scrhgt = root.winfo_screenheight()
xLeft = int((scrwdth / 2) - (350 / 2))
yTop = int((scrhgt / 2) - (280/ 2))
strg="350x300+"+str(xLeft)+"+"+str(yTop)
root.geometry(strg)
root.title("Product Search")
root.resizable(0,0)
root.wm_iconbitmap('SearchIcon.ico')
# root.overrideredirect(1)
Labelfont=("Times New Roman", 12)
titleLabel = tk.Label(root,text="Product Search",font=("Segoe UI", 20)).place(x=80,y=10)
ProductNameLabel = tk.Label(root, text="Product Name :",font=Labelfont).place(x=10,y=55)
ProductEntry = tk.Entry(root,width=30)
ProductEntry.place(x=150,y=60)

NumOfProdLabel = tk.Label(root, text="Number of Products :",font=Labelfont).place(x=10,y=85)
NumTup=[]
intg = tk.IntVar()
NumTup = [i for i in range(10,51)]
NumEntry = ttk.Combobox(root,state="readonly", width=27,textvariable=intg)
NumEntry['values'] = tuple([10])
NumEntry.current(0)
NumEntry.place(x=150,y=90)


SortByLabel = tk.Label(root, text="Sort By :",font=Labelfont).place(x=10,y=115)
n = tk.StringVar()
SortEntry = ttk.Combobox(root,state="readonly", width=27,textvariable=n)
SortEntry['values'] = ('Price: Low to High','Price: High to Low','Featured','Newest Arrivals')
SortEntry.current(2)
SortEntry.place(x=150,y=120)

PriceLabel = tk.Label(root, text="Price Range :",font=Labelfont).place(x=10,y=145)
m = tk.StringVar()
PriceEntry = ttk.Combobox(root,state="readonly", width=27,textvariable=m)
PriceEntry['values'] = ('No limit','In particular Range')
PriceEntry.current(0)
PriceEntry.place(x=150,y=145)

PincodeLabel = tk.Label(root, text="Delivery Pincode :",font=Labelfont).place(x=10,y=205)
PincodeEntry = tk.Entry(root,width=30)
PincodeEntry.insert(0,'400072')
PincodeEntry.place(x=150,y=210)
SearchButton = tk.Button(root,text="Search",font=Labelfont,width=10,command=taskToDo).place(x=125,y=250)
minlabel=tk.Label(root,text="Min:",font=Labelfont).place(x=150,y=175)
minEntry = tk.Entry(root,width=8)
minEntry.place(x=185,y=180)
minlabel=tk.Label(root,text="Max:",font=Labelfont).place(x=242,y=175)
maxEntry = tk.Entry(root,width=8)
maxEntry.place(x=280,y=180)
minEntry.insert(0,0)
maxEntry.insert(0,0)
root.mainloop()

