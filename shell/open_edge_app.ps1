//  get clipboard text
$clipboard=Get-Clipboard
Write-Output $clipboard
msedge --new-window --app="$clipboard"