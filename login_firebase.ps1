# Update PATH for this session so we can find Node and Firebase
$env:Path = "C:\Program Files\nodejs;C:\Users\UNIONIT\AppData\Roaming\npm;" + $env:Path

Write-Host "=== Firebase Login ===" -ForegroundColor Cyan
Write-Host "Opening browser for login..."

firebase.cmd login

Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
