#!/usr/bin/env python
# coding=utf-8
from ..resource import spartan_context


class Input:
    def __init__(self):
        return

    def input(self, req):
        # type: (List[str], dict) -> spartan_context
        # todo
        context = spartan_context.SpartanContext(req)
        return context
