import os
import random
from datetime import date, time, datetime
import datetime
import requests

def get_data(access_token):
    # headers = {
    #     "Authorization": "token " + access_token
    # }
    remote = "https://" + access_token + "@api.github.com/user/repos"
    print(remote)
    response = requests.get(remote)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error fetching data from API')
        return None

repos = get_data("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")
print(len(repos))

total_day = 30 #total days back
commit_frequency = 10 #commit time per day
pointer = 0
for repo in repos:
    repo_link = "https://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@github.com/" + repo['full_name'] + ".git"
    
    tl = total_day #time day
    ctr = 1

    now = datetime.datetime.now()

    f = open("commit.txt", "w")
    os.system("git config user.name \"smartsolutions4u\"")
    os.system("git config user.email smartsolutions.git@gmail.com")
    os.system("git init")

    pointer = 90

    def randtime(start_time = datetime.time(9, 0, 0), end_time = datetime.time(17, 0, 0)):
        time_range = datetime.datetime.combine(datetime.date.today(), end_time) - datetime.datetime.combine(datetime.date.today(), start_time)
        random_seconds = random.randint(0, time_range.seconds)
        return (
            datetime.datetime.combine(datetime.date.today(), start_time)
            + datetime.timedelta(seconds=random_seconds)
        ).time()

    while tl > 0:
        ct = random.randint(0, 4)
        while ct > 0 and random.randint(0,2):
            with open("commit.txt", "a+") as f:
                l_date = now + datetime.timedelta(days=-pointer)
                if l_date.weekday() == 5 and random.randint(0, 7) != 5:
                    break
                if l_date.weekday() == 6 and random.randint(0, 12) != 5:
                    break
                formatdate = l_date.strftime("%Y-%m-%d")
                formattime = randtime()
                f.write(f"commit ke {ctr}: {formatdate}\n")
            os.system("git add .")
            os.system(f"git commit --date=\"{formatdate} {formattime}\" -m \"commit ke {ctr}\"")
            print(f"commit ke {ctr}: {formatdate}")
            ct-=1
            ctr+=1
        pointer+=1
        tl-=1

    os.system(f"git remote add origin {repo_link}")
    os.system(f"git remote set-url origin {repo_link}")
    os.system("git branch -M main")
    os.system("git push -u origin main -f")


# import requests

# # Replace with your Github username and personal access token
# username = 'smat'
# token = 'personal_access_token'

# # API endpoint to fetch repositories
# url = f"https://api.github.com/users/{username}/repos"

# # Header with authorization token
# headers = {
#     'Authorization': f'Bearer {token}'
# }

# # GET request to fetch repositories
# response = requests.get(url, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse response JSON
#     repositories = response.json()
#     # Print names of all the repositories
#     for repo in repositories:
#         print(repo['name'])
# else:
#     print(f"Request failed with status code: {response.status_code}")
