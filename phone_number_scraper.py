import os, requests, csv, time
from lxml import html
from openpyxl import load_workbook
from openpyxl.workbook import Workbook

wb = load_workbook(filename=os.getcwd()+'/Ch4llengerTV.xlsx', read_only=True)
ws = wb['Ch4llengerTV']

a1, b1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1 = [],[],[],[],[],[],[],[],[],[],[],[]

for row in ws.rows:
    a1.append(row[0].value)
    b1.append(row[1].value)
    d1.append(row[3].value)
    e1.append(row[4].value)
    f1.append(row[5].value)
    g1.append(row[6].value)
    h1.append(row[7].value)
    i1.append(row[8].value)
    j1.append(row[9].value)
    k1.append(row[10].value)
    l1.append(row[11].value)
    m1.append(row[12].value)

with open(os.getcwd()+'/trump_master_Ch4llengerTV.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    main_info = ["LastName", "FirstName", "Address1", "Address2", "City", "State", "Zip", "Date", "Amount", "Total", "Employer", "Occupation", "Phone_1", "Phone_2",
                 "Phone_3", "Phone_4", "Phone_5"]
    
    csvwriter.writerow(main_info)
    counter=0
    for i in range(1, len(a1)):
        counter+=1
        headers = {
            'DNT': '1',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,fr;q=0.6',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Proxy-Authorization': 'Basic MmQ2OGIzYTctMGRhZi00ZDc4LTk0MGYtZjgxMDJlY2MzNjk4OmVlYzc3YWI0YjBmZGNmMmIxYTBhZGQ5ODI2Y2NkNDQ3MDJmZGE1ZTk=',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://findlinks.addresses.com/',
            'Proxy-Connection': 'keep-alive',
        }
        cooky = requests.get("http://findlinks.addresses.com/", headers=headers).cookies.get_dict()
        tree = html.fromstring(requests.get('http://findlinks.addresses.com/redirect.php?qf='+b1[i]+'&qn='+a1[i]+'&qc='+f1[i]+'&qs='+g1[i]+'&ReportType=34&x=24&y=16', headers=headers, cookies=cooky).text)
        
        temp = []
        temp.append(a1[i])
        temp.append(b1[i])
        temp.append(d1[i])
        temp.append(e1[i])
        temp.append(f1[i])
        temp.append(g1[i])
        temp.append(h1[i])
        temp.append(i1[i])
        temp.append(j1[i])
        temp.append(k1[i])
        temp.append(l1[i])
        temp.append(m1[i])
        temp.extend(tree.xpath('//div[@class="phone"]/text()'))
        
        csvwriter.writerow(temp)
        print (counter)
        time.sleep(3)
