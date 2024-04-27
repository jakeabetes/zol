@echo off
"C:\Users\jaetu\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\jaetu\OneDrive\Documents\git\python-scripts\vault-uploader.py"
call git add .
call git commit -m "publishing new Zol content"
call git push origin hugo
pause