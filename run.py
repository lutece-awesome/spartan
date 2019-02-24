#!/usr/bin/env python
# coding=utf-8

from src.checker import checker
from src.compiler import compiler
from src.input import input
from src.output import output
from src.runner import runner
from src.scheduler import scheduler
from src.resource import spartan_context


class SpartanRunner():
    def __init__(self):
        self.Checker = checker.Checker()
        self.Compiler = compiler.Compiler()
        self.Input = input.Input()
        self.Output = output.Output()
        self.Runner = runner.Runner()
        self.Scheduler = scheduler.Scheduler()
        # self.SpartanContext = spartan_context.SpartanContext()

    def run(self, req):
        # input
        context = self.Input.input(req) # 传入 req 返回 spartan_context
        context.show()

        # check
        context = self.Checker.check(context)

        # compiler
        context = self.Compiler.compile(context)

        # scheduler
        context = self.Scheduler.schedule(context)

        # runner
        context = self.Runner.Run(context)

        # output
        context = self.Output.output(context)

        return context

    def test(self):
        req = {
            'Data':'print a + b',
            'DataType': 2,
            'Limitation':{
                'time': 1000,
                'memory': 1024
            },
            'InputType': 'Empty'
        }
        print self.run(req)


if __name__ == '__main__':
    Runner = SpartanRunner()
    Runner.test()
