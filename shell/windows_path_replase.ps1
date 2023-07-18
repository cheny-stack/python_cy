$clipboard = Get-Clipboard
Write-Output $clipboard
$convertedPath = $clipboard -replace '\\', '/'
$convertedPath | Set-Clipboard
pause