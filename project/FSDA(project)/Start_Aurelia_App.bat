@echo off
echo =======================================================
echo          STARTING AURELIA LUXURY HOTEL APP
echo =======================================================
echo Please leave this window open while using the app!
echo The application will automatically open in your browser...
echo.

:: Automatically open the default web browser to the Login Page on Port 8001
start http://localhost:8001/user_login.html

:: Start the Python HTTP Server on Port 8001 so it never conflicts with Port 8000
python -m http.server 8001

pause
