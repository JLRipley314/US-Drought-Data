#!/usr/bin/bash

if [ "$1" == "-h" ]; then
  echo "Usage: convert notebook to html"
  exit 0
fi

jupyter nbconvert --to html Regional-Drought.ipynb
