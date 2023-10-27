#!/bin/bash
if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: Python is not installed. Please install Python then try again' >&2
  exit 1
else
   python3 ~/T1A3_TerminalApp/src/main.py
fi
