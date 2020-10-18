#!/bin/bash
cd `dirname $0`
VENV_PYTHON_INTERPRETER=../venv/bin/python3

$VENV_PYTHON_INTERPRETER ../src/monitor.py