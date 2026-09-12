$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$files = Get-ChildItem -Path "." -Filter *.html -Recurse | Where-Object { $_.Name -ne 'index.html' }

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
    $modified = $false

    # Match the inner-breadcrumb home link part that contains non-ASCII characters that are not Thai
    # We'll just replace the whole home link content to be safe.
    $pattern = '(?s)(<div class="inner-breadcrumb">\s*<a href="[^"]*index\.html">\s*<svg[^>]+>.*?</svg>)\s*[^<]+?(?=\s*</a>)'
    if ($content -match $pattern) {
        # Replace it with the SVG and HTML entities for "หน้าหลัก"
        $replacement = '$1' + "`r`n                    &#3627;&#3609;&#3657;&#3634;&#3627;&#3621;&#3633;&#3585;"
        $content = $content -replace $pattern, $replacement
        $modified = $true
    }

    if ($modified) {
        [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
        Write-Host "Fixed $($file.FullName)"
    }
}
