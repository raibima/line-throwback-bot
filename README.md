# line-throwback-bot
LINE bot that brings back old memories.
## Guide
*Current setup only supports deployment to Heroku*

Put your photos inside `static/img` directory.

Before deploying, these config vars should be set:
- CHANNEL_TOKEN (from LINE)
- CHANNEL_SECRET (from LINE)
- HOSTNAME (your Heroku URL `$ heroku info -s | grep web_url | cut -d= -f2`)

To deploy:

    $ git push heroku master
