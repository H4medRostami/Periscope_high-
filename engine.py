#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:04:31 2019

@author: chevik
"""
from stem import Signal
from stem.control import Controller
import requests
import re
import json
from requests import Request, Session
from torrequest import TorRequest
tr=TorRequest(password='12345')
tr.reset_identity() #Reset Tor

_cookiles_list=[]
class PeriscopeBot:
    _apiUrl = 'https://api.periscope.tv/api/v2'
    _session = ''
    _token = ''
    _broadcast_id = 0

    def __init__(self, broadcast_id):
        self._session = tr.session
        self._session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        self._session.headers['Accept-Encoding'] ='gzip, deflate, br'
        self._session.headers['Cache-Control'] ='max-age=0'
        self._session.headers['Host'] ='api.periscope.tv'
        self._session.headers['Upgrade-Insecure-Requests'] ='1'
        self._session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        self._session.headers['Accept-Language'] = 'en-US,en;q=0.9,fa;q=0.8'
        self._broadcast_id = broadcast_id
        self._session.headers['Connection'] ='keep-alive'
        #self._session.headers['X-Attempt'] ='1'
        #self._session.headers['X-Idempotence'] ='1550503928193--542d37e1-060d-4e3c-8de5-6efdcd2ee499'
        #self._session.headers['X-Periscope-User-Agent'] ='PeriscopeWeb/App (9fb6d0514028f8d046413e1ae7667e20f1442685) Chrome/72.0.3626.96 (Linux;x86_64)'


    def setcookie(self,hash):
        self._session.headers['Cookie'] ='user_id='+hash
        pass


    def start(self):


        for c in _cookiles_list:
            rCount=0
            self.setcookie(c)
            self._token = self._getToken()

            while(rCount<=50):


                print (str(self._startWatching().content))
                print(self._session.headers['Cookie'])

                rCount +=1
        pass

    def _startWatching(self):
        r= self._session.get(self._getApiMethod('startPublic') + '?life_cycle_token=' + self._token + '&auto_play=false')

        return r

    def _getcl(self):
        self._session.get(self._getApiMethod('accessVideoPublic') + '?broadcast_id=' + self._broadcast_id+'&replay_redirect=false')
        _cookiles_list.append(self._session.cookies.get('user_id'))

        pass

    def _getToken(self):
        tknr2=(self._session.get(self._getApiMethod('accessVideoPublic') + '?broadcast_id=' + self._broadcast_id).json())

        return (str(tknr2['life_cycle_token']))
        #return tknr2['life_cycle_token']
       #   return  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJicm9hZGNhc3RfaWQiOiIxWXFKRHl5ZGVEYXhWIiwiY3JlYXRlZCI6MTU1MDI0MTE0OCwiZXhwIjoxNTUwMzI3NTQ4LCJpZ25vcmUiOmZhbHNlLCJpc19oaWdobGlnaHRzIjpmYWxzZSwiaXNfbGl2ZSI6ZmFsc2UsInBhcnRpY2lwYW50X2luZGV4IjowLCJ0b2tlbl92ZXJzaW9uIjoxfQ.F80mVkvtecoNelmiyIljuYRLjnt9ZtovBsfvtwz6FaU'
         #print (str(self._session.get(self._getApiMethod('accessVideoPublic') + '?broadcast_id=' + self._broadcast_id).content))


    def _getApiMethod(self, method):
        return self._apiUrl + '/' + method

broadcastId = '1yoKMjaAvwDGQ' #input('Broadcast ID: ')
Cookies_Count =50  #int(input('Number of bots: '))

cookiesCount = 0

while (cookiesCount <=Cookies_Count):
     rc=PeriscopeBot(broadcastId)
     #rc._session=requests.Session()
     #rc._broadcast_id=broadcastId
     rc._getcl()
     cookiesCount = int(cookiesCount) + 1
     print((_cookiles_list))
     PeriscopeBot(broadcastId).start()
print ('Success')
