@echo off
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\push_to_github.ps1" %*
