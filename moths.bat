@echo off
cd "C:\Users\\Downloads"
curl.exe --output main.py --url https://raw.githubusercontent.com/kieran-smith77/Moth_data/main/main.py
curl.exe --output british_moths_list.csv --url https://kieran-smith.com/uni/british_list.csv
C:\python\python.exe main.py "C:\Users\\Documents\Greg\Moth Lists"
del main.py british_moths_list.csv
