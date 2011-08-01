'''Google Reader Client 
'''
import urllib
import httplib2
import cookielib
import oauth2 as oauth
import re
httplib2.debuglevel = 2

class GoogleReaderClient(object):

    client_login_uri = 'https://www.google.com/accounts/ClientLogin'

    token_endpoint =  'https://accounts.google.com/o/oauth2/token'
    #feed_endpoint = 'https://www.google.com/reader/view/feed/'
    feed_endpoint = 'http://www.google.com/reader/atom/feed/'
    
    def __init__(self, **kwargs):
        self.http_client = httplib2.Http(**kwargs)
        self.auth_token = None

    def login(self, login, password):
        ''' Login into GoogleReader. You must call identify before calling this.
            You must call this before anything else that acces to GoogleReader data.'''

        data = {
            'accountType' : 'GOOGLE',
            'service' : 'reader',
            'Email' : login,
            'Passwd' : password,
            'source' : 'kinper',
            'continue' : 'http://www.google.com/',
            }
        headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
        body = urllib.urlencode(data)
        info,content = self.http_client.request(self.client_login_uri, method='POST', body=body, headers=headers)

        match = re.search(r"(Auth=)([\w|-]+)", content)
        self.auth_token = match.group(2)
        return self.auth_token != None

    def get_feed(self, feed_url):
        #url = self.feed_endpoint + urllib.quote(feed_url)
        url = self.feed_endpoint + feed_url
        headers = {"Authorization" : "GoogleLogin auth=" + self.auth_token}
        response = self.http_client.request(url, headers=headers)
        return response

if __name__ == "__main__":
    grc = GoogleReaderClient()
    grc.login('example@gmail.com', 'examplepass')
 
    feed = grc.get_feed('http://xkcd.com/rss.xml')
    print feed
                             
