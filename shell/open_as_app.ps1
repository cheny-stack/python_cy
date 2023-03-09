$clipboard = Get-Clipboard
Write-Output $clipboard
Start-Process -FilePath "chrome" -ArgumentList "--profile-directory=Default", "--app=$clipboard"
pause