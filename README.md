# ip-sender

This allows you to send your IP if it changes to a webhook.

## Install dependencies

```
pip install -r requirements.txt
```

## Set your credentials
Update `config.json` with your webhook.

## Add Cron 

```
crontab -e
```
Add the command:
```
*/5 * * * * /usr/bin/python3 /path/to/main.py
```