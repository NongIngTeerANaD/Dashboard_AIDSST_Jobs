@echo off
chcp 65001 >nul
cd /d "%~dp0"
python -m pip install -r requirements.txt -q
echo Dashboard: http://127.0.0.1:8077
start "" http://127.0.0.1:8077
python -m app
