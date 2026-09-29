# Update PATH for this session so we can find Node and Firebase
$env:Path = "C:\Users\Admin\.gemini\antigravity-ide\scratch\web-ukem\node22\node-v22.14.0-win-x64;" + $env:Path

Write-Host "=== Firebase Login ===" -ForegroundColor Cyan
Write-Host "Opening browser for login..."

firebase.cmd login

Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
