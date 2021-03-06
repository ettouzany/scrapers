from bs4 import BeautifulSoup as bs
import requests
import lxml
import json

url = "https://www.dreamjob.ma/emploi/page/"

output = []

max = 14
with open("output.json", "w") as f:
    precent = 0
    j = 0
    for i in range(1, max+1):
        res = requests.get(url+str(i))
        soup = bs(res.text, "lxml")
        jobs_count = len(soup.find_all("article", {"class": "jeg_post"}))
        
        for job in soup.find_all("article", {"class": "jeg_post"}):
            link = job.find("a")["href"]
            # get request from link
            res = requests.get(link)
            # parse the html
            soup = bs(res.text, "lxml")
            # get the job title
            title = soup.find("h1", {"class": "jeg_post_title"}).text
            # get the job description
            description = soup.find("div", {"class": "entry-content"}).text
            # get the job location
            # add the job to the output
            output.append({"title": title, "link": link , "description": description})
            j += 1
            precent = (j/jobs_count)*100 /max
            print("\r"+str(round(precent, 2))+"%", end="")
    json.dump(output, f, indent=4, ensure_ascii=False)
    f.close()



