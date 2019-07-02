import argparse
import os
import sys
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run when ./build present')
    parser.add_argument('--change', required=True)
    parser.add_argument('--change-url', required=True)
    parser.add_argument('--change-owner', required=True)
    parser.add_argument('--change-owner-username', required=True)
    parser.add_argument('--project', required=True)
    parser.add_argument('--branch', required=True)
    parser.add_argument('--reviewer', required=True)
    parser.add_argument('--reviewer-username', required=True) 
    args = parser.parse_args()

    response = requests.get('https://localhost:8080/a/changes/args.change/reviewers', auth=('admin', 'S/jPAt0YYGsehjbpU2BATnJ7w0wVzOc0Z+ThsnJNV'), verify = False)
    result = response.text[5:]
    result = json.loads(result)
    response3 = requests.post('https://slack.com/api/chat.postMessage?token=xoxp-650721783651-664265172182-664155169095-35390dbd1edc3bdfa8b271908fd63eaa&channel=%23gerrit-reviewers'
      + '&text= There has been a code change. Please check Gerrit.'
      +'&pretty=1')

    '''response2 = requests.get('https://slack.com/api/users.list?token=xoxp-650721783651-664265172182-664155169095-35390dbd1edc3bdfa8b271908fd63eaa&pretty=1')
    #print(json.dumps(response2.json(), indent = 4, sort_keys=True))
    userid = response2.json()["members"]
    members = len(response2.json()["members"])
    for i in range(members):
        for j in range(len(result)):
            if(result[j]['name'] == response2.json()["members"][i]["real_name"]):
                userid = response2.json()["members"][i]["id"]
    response3 = requests.post('https://slack.com/api/chat.postMessage?token=xoxp-650721783651-664265172182-664155169095-35390dbd1edc3bdfa8b271908fd63eaa&channel=%23gerrit-reviewers'
      + '&text=<@' + userid + '> There has been a code change. Please check Gerrit.'
      +'&pretty=1')'''

    sys.exit(0)
import argparse
import os
import sys
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run when ./build present')
    parser.add_argument('--change', required=True)
    parser.add_argument('--change-url', required=True)
    parser.add_argument('--change-owner', required=True)
    parser.add_argument('--change-owner-username', required=True)
    parser.add_argument('--project', required=True)
    parser.add_argument('--branch', required=True)
    parser.add_argument('--reviewer', required=True)
    parser.add_argument('--reviewer-username', required=True) 
    args = parser.parse_args()

    response = requests.get('https://localhost:8080/a/changes/args.change/reviewers', auth=('admin', 'S/jPAt0YYGsehjbpU2BATnJ7w0wVzOc0Z+ThsnJNV'), verify = False)
    result = response.text[5:]
    result = json.loads(result)
    response3 = requests.post('https://slack.com/api/chat.postMessage?token=xoxp-650721783651-664265172182-664155169095-35390dbd1edc3bdfa8b271908fd63eaa&channel=%23gerrit-reviewers'
      + '&text= There has been a code change. Please check Gerrit.'
      +'&pretty=1')

    '''response2 = requests.get('https://slack.com/api/users.list?token=xoxp-650721783651-664265172182-664155169095-35390dbd1edc3bdfa8b271908fd63eaa&pretty=1')
    #print(json.dumps(response2.json(), indent = 4, sort_keys=True))
    userid = response2.json()["members"]
    members = len(response2.json()["members"])
    for i in range(members):
        for j in range(len(result)):
            if(result[j]['name'] == response2.json()["members"][i]["real_name"]):
                userid = response2.json()["members"][i]["id"]
    response3 = requests.post('https://slack.com/api/chat.postMessage?token=xoxp-650721783651-664265172182-664155169095-35390dbd1edc3bdfa8b271908fd63eaa&channel=%23gerrit-reviewers'
      + '&text=<@' + userid + '> There has been a code change. Please check Gerrit.'
      +'&pretty=1')'''

    sys.exit(0)