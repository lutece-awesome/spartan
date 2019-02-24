#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append('..')
import run

def test():
    Runner = run.SpartanRunner()
    req = {
        'Data':'print a + b',
        'DataType': 2,
        'Limitation':{
            'time': 1000,
            'memory': 1024
        },
        'InputType': 'Empty'
    }
    print(Runner.run(req))

if __name__ == '__main__':
    test()
