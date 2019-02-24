#!/usr/bin/env python
# coding=utf-8

from typing import List
from src.checker import checker
from src.compiler import compiler
from src.input import input
from src.output import output
from src.runner import runner
from src.scheduler import scheduler
from src.resource import spartan_context


class SpartanRunner():
    def __init__(self): # type: () -> None
        self.Checker = checker.Checker()
        self.Compiler = compiler.Compiler()
        self.Input = input.Input()
        self.Output = output.Output()
        self.Runner = runner.Runner()
        self.Scheduler = scheduler.Scheduler()
        # self.SpartanContext = spartan_context.SpartanContext()

    def run(self, req):
        # type: (List[str], dict) -> dict
        context = self.Input.input(req) # 传入 req 返回 spartan_context

        # check
        context = self.Checker.check(context)

        # compiler
        context = self.Compiler.compile(context)

        # scheduler
        context = self.Scheduler.schedule(context)

        # runner
        context = self.Runner.Run(context)

        # output
        result = self.Output.output(context)

        return result

