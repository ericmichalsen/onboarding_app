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

Rename the env_rename to .env file and set your Terminus, Skilljar username, and Skilljar password. If you would like to exlude an organization, add it to the UUIDS list, creating a new line, and within the quotes.

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
 * Run script against individual organization
