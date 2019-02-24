#!/usr/bin/env python
# coding=utf-8
import sys
from ..resource import spartan_context


class Input():
    def __init__(self):
        return

    def input(self, req):
        # todo
        context = spartan_context.SpartanContext(req)
        return context


if __name__ == '__main__':
    print 'todo'
