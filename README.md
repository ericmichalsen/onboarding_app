# onboarding_app
v 1.1

Onboarding script to monitor customer activity on the platform and LMS

This script requires Python 3, and various Python modules. This _should_ be easily
resolved with

```brew install python```

Once Python is installed, you will need to run pip, the Python package installer.
```
sudo pip3 install python-dateutil mechanize beautifulsoup4 requests python-dotenv
```
You may need to install XCode.

Rename the env_rename to .env file and set your Terminus, Skilljar username, and Skilljar password. If you would like to exlude an organization, add it to the list, creating a new line, and within the quotes.
```
TR_EMAIL=<TERMINUS AUTH EMAIL>
SJ_EMAIL=<EMAIL>
SJ_PASWD=<PASSWORD>
UUIDS="a11954ef-5297-4d4a-bc9c-3d0140e25044
d3ecc20c-395a-43c4-93ee-f5f43808b6c8
fce29c48-522f-4984-8c7c-f9473733c67b
7fe89bb8-d49c-48f3-8507-10b9c7b6c353
cea85340-8e98-4049-b9cf-63fc5f21a306
cae88286-61c5-4417-b46d-0287990ce1b8
63149cf3-0b02-46e7-ae0f-97c7c67a915a"
```
Your SkillJar login may be SSO. This is OK. Go to https://dashboard.skilljar.com/login and click *Forgot Password?* It'll send the link so you can set your username to your email and password to your system password.

When you are ready to run the script, type ```python3 weekly_check.py```

The content will print out pre-formatted for Slack. You may need to set the auto-formatting in the Slack preferences. To do so, open Slack's preferences menu by clicking the menu at the top-left corner of the Slack window and selecting “Preferences.” Click “Advanced” in the left pane and enable “Format messages with markup” under Input Options.

Todo: 
 * There is a Terminus warning that gets printed when there are no sites. I need to suppress this.
 * ~~Terminus auth check and login~~ v1.1
 * ~~Exclude org UUIDS in .env~~ v1.1
 * **Harvest API** to display time w/customer for the week
 * **JIRA API** get slack channel and backup onboarder
 * Automatic submission into **Slack API**
