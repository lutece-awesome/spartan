#!/usr/bin/env python
# coding=utf-8

from typing import List

from src.checker import checker
from src.compiler import compiler
from src.input import input
from src.output import output
from src.runner import runner
from src.scheduler import scheduler
from util.decorators import singleton


@singleton
class SpartanRunner:
    scheduler: scheduler.Scheduler
    input: input.Input
    compiler: compiler.Compiler
    runner: runner.Runner
    checker = checker.Checker
    output: output.Output

    def __init__(self, is_debug=False) -> None:
        self.scheduler = scheduler.Scheduler()
        self.input = input.Input()
        self.compiler = compiler.Compiler()
        self.runner = runner.Runner()
        self.checker = checker.Checker()
        self.output = output.Output()
        # self.SpartanContext = spartan_context.SpartanContext()

    def run(self, req):
        # type: (List[str], str) -> str
        RunningData = self.input.input(req)  # 传入 req 返回 spartan_context

        # check
        RunningData = self.checker.check(RunningData)

        # compiler
        RunningData = self.compiler.compile(RunningData)

        # scheduler
        RunningData = self.scheduler.schedule(RunningData)

        # runner
        RunningData = self.runner.Run(RunningData)

        # output
        result = self.output.output(RunningData)

        return result
