#!/usr/bin/env python3

import pip

def install(package):
   pip.main(['install', package])

install('requests')
install('json') 
install('asyncio')
