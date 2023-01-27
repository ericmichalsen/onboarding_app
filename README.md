# onboarding_app
Onboarding script to monitor customer activity on the platform and LMS

This script requires Python 3, and various Python modules. This should be easily
resolved with ```brew install python```.

Once Python is installed, you will need to run pip, the Python module installer.
```
* pip3 install python-dateutil
* pip3 install mechanize
* pip3 install beautifulsoup4
* pip3 install requests
* pip3 install python-dotenv
```

Edit the .env file and set your Skilljar username and password.

When you are ready to run the script, type ```python3 weekly_check.py```

The content will print out pre-formatted for Slack. You may need to set the auto-formatting in the Slack preferences. To do so, open Slack's preferences menu by clicking the menu at the top-left corner of the Slack window and selecting “Preferences.” Click “Advanced” in the left pane and enable “Format messages with markup” under Input Options.