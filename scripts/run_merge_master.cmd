@echo off
setlocal

python "%~dp0merge_master_dataset.py" %*
exit /b %ERRORLEVEL%
