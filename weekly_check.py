import sys
import os
import subprocess
import datetime
import dateutil.parser
import json
import re
import urllib.parse
import time

import mechanize
from bs4 import BeautifulSoup
from urllib.request import urlopen

from http.cookiejar import LWPCookieJar
import requests

from dotenv import load_dotenv
load_dotenv()

## .env variables
terminus_email = os.getenv('TR_EMAIL')
skilljar_pass = os.getenv('SJ_PASWD')
skilljar_email = os.getenv('SJ_EMAIL')
excluded_uuids = os.getenv('UUIDS').splitlines()

###
# Terminus Authentication
###

## Check validity of an email address
def is_valid_email(email):
    # Regular expression pattern for a valid email address
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

## Terminus authority verify
check_user = subprocess.Popen("terminus whoami", shell=True, stdout=subprocess.PIPE)
check_user_return = check_user.stdout.read()

## Terminus Auth:Login if not logged in
if is_valid_email(check_user_return.decode()):
    login = subprocess.Popen("terminus auth:login --email="+terminus_email, shell=True, stdout=subprocess.PIPE)
    login_result= login.stdout.read()

###
# Set SkillJar session for scraping
###

## Create Session
s = requests.Session()
cookie_file = '/tmp/cookies'
jar = LWPCookieJar(cookie_file)

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
browser.set_cookiejar(jar)

browser.open("https://dashboard.skilljar.com/login")

browser.select_form(nr=0)
browser.form['email'] = skilljar_email
browser.form['password1'] = skilljar_pass
browser.submit()


## Create an array organizations where member
get_orgs = subprocess.Popen("terminus org:list --fields=ID,Name,Label --format=csv", shell=True, stdout=subprocess.PIPE)
get_orgs_return = get_orgs.stdout.read()

## Iterate through organization array
for org_line in get_orgs_return.splitlines():
    org = org_line.decode("utf-8").split(',')

    # check if organization is exluded
    if (org[0] not in excluded_uuids):
        if (org[1] != "Name"):
            
            # Assign ID, Name, Label
            orgID = org[0]
            orgName = org[1]
            orgLabel = org[2]

            # Markup formatting
            print('Weekly Review for *'+orgLabel.strip('\"')+'* \n')
            print('*LMS*')

            lms_count = 0
            # Users within Org
            get_users = subprocess.Popen("terminus org:people:list "+ orgID + " --field=Email --format=csv", shell=True, stdout=subprocess.PIPE)
            get_users_return = get_users.stdout.read()
            for org_user in get_users_return.splitlines():
                user = org_user.decode("utf-8")
                domain = user.split('@')[1] 

                ## Exclude members who are Pantheors
                if not ("pantheon") in domain:
                    # print(user)
                    browser.open("https://dashboard.skilljar.com/analytics/students/ajax-data?draw=1&start=0&length=25&skip_total_count=true&order[0][column]=5&order[0][dir]=desc&signed_up_at=all&latest_activity=all&search[value]="+urllib.parse.quote_plus(user)+"&_=1668790286383")
                    response = browser.response().read().decode('utf-8')
                    r = json.loads(response)

                    for mem in r['data']:
                        if (mem['registrations']['display'] > 0):
                            print(user)
                            lms = user+"\n"
                            latest_activity = re.sub('<[^<]+?>', '', mem['latest_activity']['display'])
                            print("* Registrations: "+str(mem['registrations']['display']))
                            print("* Course Completions: "+str(mem['course_completions']['display']))
                            print("* Latest Activity: "+latest_activity)
                            lms_count = lms_count + 1
                    time.sleep(3)

            if (lms_count < 1):
                print("No org members registered in LMS")

            # Site Loop within Org
            get_sites = subprocess.Popen("terminus org:site:list "+ orgID + " --fields=ID,Name,\"Is Frozen?\" --format=csv", shell=True, stdout=subprocess.PIPE)
            get_sites_return = get_sites.stdout.read()
            
            site_count  = len(get_sites_return.splitlines()) - 1
            
            if (site_count == 0):
                print("No Sites")
            else:
                print(str(site_count)+" Sites in org")

            for site_line in get_sites_return.splitlines():
                site = site_line.decode("utf-8").split(',')
                if (site[1] != "Name"):
                    
                    # Assign ID, Name, Frozen
                    siteID = site[0]
                    siteName = site[1]
                    frozen = site[2]

                    # If NOT Frozen
                    if (frozen == "false"):

                        # Env loop envs within site
                        get_envs = subprocess.Popen("terminus env:info "+ siteName+".live" + " --field=Initialized", shell=True, stdout=subprocess.PIPE)
                        get_envs_return = get_envs.stdout.read()

                        # Find Live env
                        if b'1\n' in get_envs_return:
                            print(f"Live Environment:  {site[1]}")

    print("=======================")

