job_title = job.find("a").text
    experience = job.find("li").text.replace("card_travel", '')
    location = job.find("ul", class_="top-jd-dtl clearfix")
    location = location.find("span").text

    key_skills = job.find(
        "span", class_="srp-skills").text.replace(" ", '')
    job_link = job.find("header", class_="clearfix").find("a")
    job_link = job_link.get("href")

    print(f"JOB: {job_title.strip()}")
    print(f"Experience: {experience}")
    print(f"Location: {location}")
    print(f"Skills: {key_skills.strip()}")
    print(f"Job Link: {job_link} ")
    print("")
    print("")