#!/usr/bin/env python3


import requests
import json

searchurl = "https://api.twitter.com/1.1/search/tweets.json?q=deutsch%20Volk%20&src=typd"
posturl = "https://api.twitter.com/1.1/statuses/update.json"
antiurl = "http://whatever.org"  #payload
user = ""
auth = "WE LOVE DATA."

def check_connection(target, user, auth):
    r = requests.get(target, auth=(user, auth))
    return r.status_code

def search(target, user, auth):
    searchjson = requests.get(target, auth=(user, auth))
    print(searchjson.decode())
    # get username and id of tweet we want to answer to
    return replyto, targetuser

def compose(antiurl, targetuser):
    return "@" + targetuser + " ich glaube eher das: " + antiurl

# text: text of status update, max. 140
# replyto: ID of another tweet (mentioning "volk" and "deutsch"), target tweet
def answer(text, replyto):
    answerquery = {"status":text, "in_reply_to_status_id":replyto}
    send = json.encode(answerquery)
    r = requests.post(posturl, data=send, auth=(user, auth))


# check connection
print(check_connection(searchurl, user, auth))

replyto, targetuser = search(searchurl, user, auth)
text = compose(antiurl, targetuser)
answer(text, replyto)





