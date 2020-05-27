#### Are.na Connected Twitter Bot

I'll show you how to automatically tweet photos from your Are.na channel every 10 minutes and deploy it to Heroku so it can run for infinity.

### Getting Started
In order to use this project, you'll need to set a few things up first.  Since we're using Twitter and Are.na's APIs we'll need to register authorized apps on both sites.  Head over to {https://developer.twitter.com/en/apps} and click 'Create An App' to get generate the needed `CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET` keys for us to run this bot.  After you have those, throw them in the `credentials.py` file to keep them safe from wandering eyes on github.  Create an account with Are.na and head to {https://dev.are.na/oauth/applications} to register an app with them.  Grab the 'access token' and put it in credentials.py as `ARENA_ACCESS_KEY`.  From there you should be able to run your app locally!
### Usage

Install dependencies
```pip install requirements.txt```

Setup a credentials.py file to hide your api keys.  Add this to the file then add your twitter and are.na keys
```
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
ARENA_ACCESS_KEY = ''
```
To run the tweet script locally run this in the console
```
python3 tweet.py
```
### Deploying to Heroku and running your worker

Go to Heroku and register for an account.  If youre unfamiliar with deploying with Heroku follow this guide to help you push your code to the site - {https://devcenter.heroku.com/articles/git}.  This codebase has two files that important for working with Heroku - requirements.txt and Procfile.  The requirements file keeps module information to tell Heroku which packages are needed to run your app - like the Are.na python api wrapper {https://github.com/frnsys/arena}.  The Procfile is where we host our two resources - one is a super simple Flask server and the other is a worker to trigger our Tweet.py file.  Once our Heroku is setup, go to the resources tab and set your `worker python3 tweet.py` to on.  And that's it! This simple app with tweet all of the images from your Are.na channel every 10 minutes.  Currently, if you add new images to your channel, you'll have to restart the worker on heroku to add the images to the list to get tweeted. 


### License

Copyright 2020 Brian Curran

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

