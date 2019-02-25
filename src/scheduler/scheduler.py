import sys

import asyncio
import random
from typing import IO

from src.conf.config import Setting
from src.input.input import Input
from util.decorators import singleton


@singleton
class Scheduler:
    _setting: Setting
    _input: Input
    _event_loop: asyncio.events
    _event_que: list
    _max_job_number: int

    def __init__(self, setting: Setting):
        self._setting = setting
        self._input = Input(setting=setting)
        self._event_que = []
        # TODO(hezhu): change it something else
        self._max_job_number = 2

    async def _run_job(self, input_str: str):
        try:
            tl = random.random() * 2
            print(f'mock running judding, {input_str}, time needing is {tl}')
            await asyncio.sleep(tl)
            print(f'mock running judding, {input_str} completed')
        except Exception as error:
            print(f'Job error with {error}')
        finally:
            self._max_job_number += 1
            self._schedule_job()

    def _schedule_job(self):
        print(self._max_job_number)
        if self._max_job_number == 0:
            print('No enough resources, suspend request.')
            return
        elif len(self._event_que) == 0:
            return
        self._max_job_number -= 1
        input_str = self._event_que[0]
        self._event_que.pop(0)
        self._event_loop.create_task(self._run_job(input_str))

    def _trigger_schedule(self):
        # TODO(hezhu): improve the policy
        pass

    def _warm_shutdown(self):
        # TODO(hezhu): wait all taks complete and close it, impl it
        self._event_loop.close()

    def _get_io_update_str(self, file_in: IO):
        if file_in is sys.stdin:
            return file_in.readline()
        else:
            return file_in.read()

    def _request_coming(self, file_in: IO):
        self._event_que.append(self._get_io_update_str(file_in))
        self._schedule_job()

    def run_forever(self, file_in: IO):
        self._event_loop = asyncio.new_event_loop()
        self._event_loop.add_reader(file_in, self._request_coming, file_in)
        self._event_loop.run_forever()
