#! /bin/bash

mkdir Bot/res
touch Bot/res/config.ini
echo "[OAuth]" >> Bot/res/config.ini
echo "    app_id =" >> Bot/res/config.ini
echo "    app_secret =" >> Bot/res/config.ini
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt