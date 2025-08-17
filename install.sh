#!/bin/bash
echo "[*] Installing Termux URL Checker..."
pkg install python -y
pip install -r requirements.txt
chmod +x url_checker.py
cp url_checker.py $PREFIX/bin/url-checker
echo "[✔] Installation complete! Run using: url-checker <url>"
