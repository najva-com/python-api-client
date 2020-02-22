import requests
import json as json_parser
from datetime import datetime, timedelta

class Najva:

    apikey = ""
    token = ""

    # api to send notification for all subscribers.
    def send_to_all(self,title, body, url, icon, onclick='open-link', image=None, 
        content=None,json=None,sent_time=None, segment_include=None,
        segment_exclude=None, one_signal_enabled=False, one_signal_accounts=None):
    
        url = "https://app.najva.com/api/v1/notifications/"

        if sent_time==None:
            sent_time = datetime.now() + timedelta(minutes=3)

        body = {
            'api_key': self.apikey,
            'title': title,
            'body': body,
            'onclick-action': onclick,
            'url': url,
            'content': content,
            'icon': icon,
            'image': image,
            'json' : '"%s"' %json,
            'sent_time': sent_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'segment_include': segment_include,
            'segment_exclude': segment_exclude,
            'one_signal_enabled': one_signal_enabled,
            'one_signal_accounts': one_signal_accounts,
        }

        headers = {
            'authorization': "Token %s" % self.token,
            'content-type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.request(method="POST", url=url, data=json_parser.dumps(body), headers=headers)

        return response.text


    ## api to send notification for specific users
    def send_to_users(self,title, body, url, icon,subscriber_tokens, onclick='open-link', image=None, 
        content=None,json=None,sent_time=None):
    
        url = 'https://app.najva.com/notification/api/v1/notifications/'

        if sent_time==None:
            sent_time = datetime.now() + timedelta(minutes=3)


        body = {
            'api-key': self.apikey,
            'title': title,
            'body': body,
            'onclick-action': onclick,
            'url': url,
            'content': content,
            'json': '"%s"' % json,
            'icon': icon,
            'image': image,
            'sent_time': sent_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'subscriber_tokens': subscriber_tokens
        }

        headers = {
            'authorization': "Token %s" % self.token,
            'content-type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.request(method="POST", url=url, data = json.dumps(body), headers= headers)

        return response.text


    # get segment ids.
    def get_segments(self):
        url = "https://app.najva.com/api/v1/websites/%s/segments/" % apikey
        headers = {
            'content-type': "application/json",
            'authorization': "Token %s" % token,
            'cache-control': "no-cache",
            }
        response = requests.request("GET", url, headers=headers)
        return response.text


    # get created accounts ids.
    def get_onesignal_accounts(self):
        url = "https://app.najva.com/api/v1/one-signals/"
        headers = {
            'content-type': "application/json",
            'authorization': "Token %s" % token,
            'cache-control': "no-cache",
        }
        response = requests.request("GET", url, headers=headers)
        return response.text


if __name__ == "__main__":
    najva = Najva()
    najva.apikey = "ad4692ae-8f37-4883-a0fa-aac58ae55a86"
    najva.token = "b32aefa32fd46b2b413990792be0bbc0391e45c3"
    response = najva.send_to_all(title="title", body="some test data", url="https://najva.com", 
                icon="https://www.ait-themes.club/wp-content/uploads/cache/images/2020/02/guestblog_featured/guestblog_featured-482918665.jpg",
                json={'key':'value'})
    print(response)