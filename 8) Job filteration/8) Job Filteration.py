from bs4 import BeautifulSoup
import requests

print("""
      _       _       _____ _ _ _                 _   _               ____        _   
     | | ___ | |__   |  ___(_) | |_ ___ _ __ __ _| |_(_) ___  _ __   | __ )  ___ | |_ 
  _  | |/ _ \| '_ \  | |_  | | | __/ _ \ '__/ _` | __| |/ _ \| '_ \  |  _ \ / _ \| __|
 | |_| | (_) | |_) | |  _| | | | ||  __/ | | (_| | |_| | (_) | | | | | |_) | (_) | |_ 
  \___/ \___/|_.__/  |_|   |_|_|\__\___|_|  \__,_|\__|_|\___/|_| |_| |____/ \___/ \__|
                           made by dollarboysushil
                           
                           
                           
site used to filter job = https://www.timesjobs.com/                                                           
""")
skill = input("Enter Skill you have. For multiple skills use comma :")
skill = skill.replace(",", "+")
location = input("Enter Location of Job:")
skill = location.replace("", "+")

response = requests.get(
    f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={skill}&txtLocation={location}")

response = response.text

soup = BeautifulSoup(response, "html.parser")


jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

for job in jobs:

    job_title = job.find("a").text
    experience = job.find("li").text.replace("card_travel", '')
    location = job.find("ul", class_="top-jd-dtl clearfix")
    location = location.find("span").text

    key_skills = job.find(
        "span", class_="srp-skills").text.replace(" ", '')
    job_link = job.find("header", class_="clearfix").find("a")
    job_link = job_link.get("href")

    with open("txt.txt", "a") as file:
        file.write(f"JOB: {job_title.strip()}\n")
        file.write(f"Experience: {experience}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Skills: {key_skills.strip()}\n")
        file.write(f"Job Link: {job_link} \n")
        file.write("\n\n")

    print(f"JOB: {job_title.strip()}")
    print(f"Experience: {experience}")
    print(f"Location: {location}")
    print(f"Skills: {key_skills.strip()}")
    print(f"Job Link: {job_link} ")
    print("")
    print("")

print("All the results are written in the txt file.")
