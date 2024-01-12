import json
import os
from csv import DictWriter
import time

try:
  with open('instaData.txt') as f:
    data = json.load(f)
  obj = {}
  obj['username'] = data['data']['user']['username']
  obj['bio'] = data['data']['user']['biography']
  obj['followersCount'] = data['data']['user']['edge_followed_by']['count']
  obj['followingCount'] = data['data']['user']['edge_follow']['count']
  obj['is_private'] = data['data']['user']['is_private']
  obj['is_verified'] = data['data']['user']['is_verified']
  obj['mediaCount'] = data['data']['user']['edge_owner_to_timeline_media']['count']

  i = 0
  for edge in data['data']['user']['edge_owner_to_timeline_media']['edges']:
    i += 1
    obj['like'+str(i)] = edge['node']['edge_liked_by']['count']
    obj['comment'+str(i)] = edge['node']['edge_media_to_comment']['count']
    if i >= 5:
      break
  print(obj)
  with open('instaOut.txt', 'a+') as f:
    f.write(json.dumps(obj))
  os.remove('instaData.txt')
  time.sleep(2)
except:
  os.remove('instaData.txt')
  time.sleep(2)
  print('error')