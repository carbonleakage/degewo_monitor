#!/bin/sh
cd ~/Python_Projects/degewo_monitor/
#source usedobjenv/bin/activate
./monitor.py
#/home/ubuntu/Python_Projects/UsedObjects/usedobjenv/bin/papermill eBay_Overview.ipynb eBay_Overview.ipynb
git add .
git commit -m "Cron Commit"
git push origin main
