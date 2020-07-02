# Project Kamini

The hardest choices require the strongest wills.



## Usage

Go to terminal.

Enter :
```bash
env EDITOR=nano crontab -e
```

Learn how to use Crontabs here: https://www.ostechnix.com/a-beginners-guide-to-cron-jobs/. 

In the file, enter:
```bash
0 * * * * python [REPO_PATH]/kamini.py -n [PHONE_NUMBER]
```
Be careful, this will send a message at the beginning of every minute.
- Change [REPO_PATH] to your path.
- Change [PHONE_NUMBER] to desired phone number.
- Ctrl + O
- Enter
- Ctrl + X
