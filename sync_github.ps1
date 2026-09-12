[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$tempZip = Join-Path $PSScriptRoot "repo.zip"
$tempDir = Join-Path $PSScriptRoot "temp_extract"

# Try downloading main branch
try {
    Write-Host "Downloading main branch..."
    Invoke-WebRequest -UseBasicParsing -Uri "https://github.com/NamSoma/web-ukem/archive/refs/heads/main.zip" -OutFile $tempZip -ErrorAction Stop
    $branch = "main"
} catch {
    Write-Host "Failed to download main branch. Trying master branch..."
    try {
        Invoke-WebRequest -UseBasicParsing -Uri "https://github.com/NamSoma/web-ukem/archive/refs/heads/master.zip" -OutFile $tempZip -ErrorAction Stop
        $branch = "master"
    } catch {
        Write-Error "Could not download main or master branch. Details: $_"
        exit 1
    }
}

# Create temp extraction folder
New-Item -ItemType Directory -Force -Path $tempDir | Out-Null

# Extract archive
Write-Host "Extracting archive..."
Expand-Archive -Path $tempZip -DestinationPath $tempDir -Force

# Locate the extracted folder
$extractedFolder = Get-ChildItem -Path $tempDir -Directory | Select-Object -First 1

if ($extractedFolder) {
    Write-Host "Moving files to target directory..."
    # Move files and folders
    Get-ChildItem -Path $extractedFolder.FullName | ForEach-Object {
        $dest = Join-Path $PSScriptRoot $_.Name
        if (Test-Path $dest) {
            Remove-Item -Path $dest -Recurse -Force
        }
        Move-Item -Path $_.FullName -Destination $dest -Force
    }
}

# Cleanup
Write-Host "Cleaning up temporary files..."
if (Test-Path $tempZip) { Remove-Item -Path $tempZip -Force }
if (Test-Path $tempDir) { Remove-Item -Path $tempDir -Recurse -Force }
Write-Host "Sync completed successfully!"
