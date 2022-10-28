#!/bin/bash

python3 planet_music.py | grep -Eo "knowit{.*?}" --color=none
