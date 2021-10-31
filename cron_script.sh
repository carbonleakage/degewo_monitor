#!/bin/sh
cd ~/Python_Projects/degewo_monitor/
#source usedobjenv/bin/activate
./monitor.py
#/home/ubuntu/Python_Projects/degewo_monitor/venv/bin/papermill scratchfile.ipynb scratchfile.ipynb
git add .
git commit -m "Cron Commit"
git push origin main
