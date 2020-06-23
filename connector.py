#!/usr/bin/env python3

import requests
import json
import time

import asyncio

from status_res import StatusRes

class Connector:

    SERVER_URL = 'https://32df8992-903f-49f5-9b4d-4c10e1bfeb19.mock.pstmn.io'
    PATH = '/status2'
    PATH2='/started'
    # /status => 'running'
    # /status2 => 'completed'
    # /start => 'started'

    def __init__(self):
        self.api1_status = None
        self.api2_status = None
        self.api3_status = None

    async def call_api1(self):
        print('making network call for request:  api1')
        # simulate network delay
        time.sleep(5)
        r = requests.get(self.SERVER_URL+self.PATH)
        j = r.json()
        self.api1_status = StatusRes(**j)
        print('got network response for request: api1') 
        return self.api1_status.status

    async def call_api2(self):
        print('making network call for request:  api2')
        # simulate network delay
        time.sleep(3)
        r = requests.get(self.SERVER_URL+self.PATH)
        j = r.json()
        self.api2_status = StatusRes(**j)
        print('got network response for request: api2') 
        return self.api2_status.status

    async def call_api3(self):
        print('making network call for request:  api3')
        # simulate network delay
        time.sleep(1)
        r = requests.get(self.SERVER_URL+self.PATH)
        j = r.json()
        self.api3_status = StatusRes(**j)
        print('got network response for request: api3') 
        return self.api3_status.status
        
    def is_ready_to_update(self):
         return self.api1_status.is_completed() and self.api2_status.is_completed() and self.api3_status.is_completed() 
        
    async def update_api1(self):
        print('making network call to update:  api1')
        time.sleep(1) 

    async def update_api2(self):
        print('making network call to update:  api2')
        time.sleep(3)

    async def update_api3(self):
        print('making network call to update:  api3')
        time.sleep(5)            


