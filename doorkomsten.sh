#!/bin/bash

if [[ ! -d venv ]]; then
  echo 'Python virtual environment not found. Setting up new one...'
  python -m venv venv
  source venv/bin/activate
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
fi

venv/bin/python src/main.py
