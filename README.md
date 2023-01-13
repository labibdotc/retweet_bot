# Retweet bot
Code behind <a href = "https://twitter.com/labib_likes">@labib_likes</a>, a twitter bot that retweets my main's <a href = "https://twitter.com/aka_labib">@aka_labib</a> twitter account likes

# Setup
1. Fork the repository.
2. Pull it to your desktop.
3. Create a `.env` file which contain only the following
```
  export API_KEY='Your API Key'
  export API_SECRET='Your API Secret'
  export ACCESS_TOKEN='Your Access Token'
  export ACCESS_SECRET='Your Access Secret'
```
4. Create a `.gitignore` file which contain only `.env` on one line. so that your keys stay safe.
5. Decide who you want to retweet and edit it in instead of `'aka_labib'` in `retweet_bot.py`
6. Download `pyenv` to setup developer environment for python with adequate dependeancies.
```
pyenv install 3.11.1 
# can try other python versions if you are looking here too far in the future. 
# pyenv does lose support sometimes for some versions as they get old

#make sure you are inside at root of this repository in your local before running next line
pyenv shell 3.11.1
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python retweet_bot.py 
# Your bot account now should have retweeted the given username's likes

deactivate # to exit environment

```

# Re-running the bot
```
#if you want to repeat for retweeting new likes you run: 
source venv/bin/activate
python retweet_bot.py 
deactivate # to exit environment
```
# Extra step
You can have the bot deployed on aws or render if you want it to periodically run using cronjobs. I am running it on my machine using crontab. Fairly easy. 

## Happy Coding <3
