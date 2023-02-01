# onboarding_app
v 1.0

Onboarding script to monitor customer activity on the platform and LMS

This script requires Python 3, and various Python modules. This _should_ be easily
resolved with

```brew install python```

Once Python is installed, you will need to run pip, the Python package installer.
```
* sudo pip3 install python-dateutil mechanize beautifulsoup4 requests python-dotenv
```

Create an .env file and set your Skilljar username and password.
```
SJ_EMAIL=<EMAIL>
SJ_PASWD=<PASSWORD>
```

When you are ready to run the script, type ```python3 weekly_check.py```

The content will print out pre-formatted for Slack. You may need to set the auto-formatting in the Slack preferences. To do so, open Slack's preferences menu by clicking the menu at the top-left corner of the Slack window and selecting “Preferences.” Click “Advanced” in the left pane and enable “Format messages with markup” under Input Options.

Todo: 
 * There is a Terminus warning that gets printed when there are no sites. I need to suppress this.
 * Terminus auth check and login
 * Exclude org UUIDS in .env
 * Harvest API to display time w/customer for the week
 * Automatic submission into Slack
