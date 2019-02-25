#!/usr/bin/env python
# coding=utf-8
import unittest
import sys, json
sys.path.append('..')
import run

class TestDict(unittest.TestCase):
    def test_all(self):
        Runner = run.SpartanRunner()
        req = {
            'Data': 'print a + b',
            'DataType': 2,
            'Limitation': {
                'time': 1000,
                'memory': 1024
            },
            'InputType': 'Empty'
        }
        req = json.dumps(req)
        status = Runner.run(req)
        self.assertEqual(status['status'], 'ERROR')

if __name__ == '__main__':
    unittest.main()