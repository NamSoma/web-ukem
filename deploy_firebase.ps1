# Update PATH for this session so we can find Node and Firebase
$env:Path = "C:\Program Files\nodejs;C:\Users\UNIONIT\AppData\Roaming\npm;" + $env:Path

Write-Host "=== Starting Firebase Deployment ===" -ForegroundColor Cyan
Write-Host "Deploying to project 'union-esg'..."

# Run deploy command
firebase.cmd deploy --project union-esg

if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[Error] It looks like you are not logged in." -ForegroundColor Red
    Write-Host "Please run this command to login first:" -ForegroundColor Yellow
    Write-Host ".\login_firebase.ps1" -ForegroundColor White
    Write-Host "`nAfter logging in, please run .\deploy_firebase.ps1 again." -ForegroundColor Yellow
} else {
    Write-Host "`n[Success] Deployment complete!" -ForegroundColor Green
}

Write-Host "Deployment script finished."
