$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$files = Get-ChildItem -Path en -Recurse -File -Filter *.html
foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $content = $content -replace '<main-nav.*?path=', '<main-nav path='
    $content = $content -replace '<main-footer(.*?)lang="en">', '<main-footer lang="en">'
    [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
}

$files_depth1 = Get-ChildItem -Path en -File -Filter *.html
foreach ($file in $files_depth1) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $content = $content -replace '<main-nav path=', '<main-nav depth="1" path='
    $content = $content -replace '<main-footer lang="en">', '<main-footer depth="1" lang="en">'
    [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
}

$files_depth2 = Get-ChildItem -Path en -Directory | Get-ChildItem -File -Filter *.html
foreach ($file in $files_depth2) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $content = $content -replace '<main-nav path=', '<main-nav depth="2" path='
    $content = $content -replace '<main-footer lang="en">', '<main-footer depth="2" lang="en">'
    [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
}
