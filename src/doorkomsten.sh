#!/bin/bash

if [[ ! -d venv ]]; then
  echo 'Setting up python venv...'
  python -m venv venv
  source venv/bin/activate
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
fi

venv/bin/python main.py
