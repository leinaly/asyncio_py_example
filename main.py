#!/usr/bin/env python3

import install
import asyncio

from connector import Connector


def status_check(conn):
    print('start status check')
    finished = False
    while not finished:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.ensure_future(api_status_handler(conn)))
        finished = conn.is_ready_to_update()
    print('end status check')


async def api_status_handler(conn):

    # way to do the scheduling
    task1 = asyncio.get_event_loop().create_task(conn.call_api1())
    task2 = asyncio.get_event_loop().create_task(conn.call_api2())
    task3 = asyncio.get_event_loop().create_task(conn.call_api3())

 
    # wait for the network calls to complete. Time to step off the event loop using await! 
    await asyncio.wait([task1, task2, task3])

    print(task1.result())
    print(task2.result())
    print(task3.result())

    print(conn.is_ready_to_update()) 


def test_main():
    conn = Connector()
    status_check(conn)


test_main()


