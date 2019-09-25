from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

class Main():
    def getFile():
        global output
        output = []
        # Set headers  
        headers = requests.utils.default_headers()
        headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
        n = 0
        with open("users.csv", "r",encoding="utf-8") as f_input:
            n = len(f_input.read().split("\n"))
        with open("users.csv", "r",encoding="utf-8") as f_input:
            csv_input = csv.DictReader(f_input)
            print("total no: ", n)
            for i, row in enumerate(csv_input):
                name = row['username']
                print(i, "/", n)
                ...
                try:
                    url = 'http://lucid.blog/'+name
                    req = requests.get(url, headers)
                    soup = BeautifulSoup(req.content, 'html.parser')
                    ss = soup.find(class_="changeHref d-block").get_text()
                    data = ss.split()
                    count = int(data[0])
                    output.append(count)
                except:
                    output.append("No data")
                
                #print(output)
        return output

    def saveAscsv(output):
        #self.output = output
        print(output)

        csv_input = pd.read_csv('users.csv',encoding="utf-8")
        csv_input['Followers Count'] = output
        csv_input.to_csv('output.csv', index=False)


Likes = Main.getFile()

output = Main.getFile()
Main.saveAscsv(output)
