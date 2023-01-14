@echo off
"C:\Users\Content Bloom\PycharmProjects\vault-uploader\venv\Scripts\python.exe" "C:\Users\Content Bloom\PycharmProjects\vault-uploader\vault-uploader.py"
pause
call git add .
call git commit -m "publishing new Zol content"
call git push origin hugo