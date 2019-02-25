#!/usr/bin/env python
# coding=utf-8


class Setting:
    # BASE
    HOST = '127.0.0.1'
    PORT = 7777

    # The default data
    DEFAULT_DATA = ''

    # The default data type, can be
    DEFAULT_DATA_TYPE = 'file'

    # The default time limit, with milliseconds
    DEFAULT_TIME_LIMIT = 1000

    # The default memory limit, with megabytes
    DEFAULT_MEMORY_LIMIT = 64

    # The default cpu number limit
    DEFAULT_CPU_NUMBER_LIMIT = 1

    # The default output limit, with megabytes
    DEFAULT_OUTPUT_LIMIT = 64

    # The default compile time limit, with milliseconds
    DEFAULT_COMPILE_TIME_LIMIT = 2000

    # The default compile memory limit, with megabytes
    DEFAULT_COMPILE_MEMORY_LIMIT = 64

    # The default checker time limit, with milliseconds
    DEFAULT_CHECKER_TIME_LIMIT = 2000

    # The default checker memory limit, with megabytes
    DEFAULT_CHECKER_MEMORY_LIMIT = 64

    # The default checker type
    DEFAULT_CHECKER_TYPE = "wcmp"

    # The default checker data
    DEFAULT_CHECKER_DATA = ""

    # The default data parser
    DATA_PARSER = "json"
