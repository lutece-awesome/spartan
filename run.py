#!/usr/bin/env python
# coding=utf-8

from typing import List

from src.checker import checker
from src.compiler import compiler
from src.input import input
from src.output import output
from src.runner import runner
from src.scheduler import scheduler


class SpartanRunner:

    def __init__(self) -> None:
        self.checker = checker.Checker()
        self.compiler = compiler.Compiler()
        self.input = input.Input()
        self.output = output.Output()
        self.runner = runner.Runner()
        self.scheduler = scheduler.Scheduler()
        # self.SpartanContext = spartan_context.SpartanContext()

    def run(self, req):
        # type: (List[str], dict) -> dict
        context = self.input.input(req) # 传入 req 返回 spartan_context

        # check
        context = self.checker.check(context)

        # compiler
        context = self.compiler.compile(context)

        # scheduler
        context = self.scheduler.schedule(context)

        # runner
        context = self.runner.Run(context)

        # output
        result = self.output.output(context)

        return result

