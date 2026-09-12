$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$files = Get-ChildItem -Path "." -Filter *.html -Recurse | Where-Object { $_.Name -ne 'index.html' }

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
    $modified = $false
    
    # 1. Clean up the corrupted Thai characters for "หน้าหลัก"
    if ($content -match 'à¸«à¸™à¹‰à¸²à¸«à¸¥à¸±à¸[\s\S]*?(?=</a>)') {
        $content = $content -replace 'à¸«à¸™à¹‰à¸²à¸«à¸¥à¸±à¸[\s\S]*?(?=</a>)', "&#3627;&#3609;&#3657;&#3634;&#3627;&#3621;&#3633;&#3585;`r`n                "
        $modified = $true
    }

    # 2. Check if already inner-hero and remove image if any
    if ($content -match '<header class="inner-hero"') {
        if ($content -match 'style="background-image: url\([^)]+\);"') {
            $content = $content -replace 'style="background-image: url\([^)]+\);"','style="background-color: #2c3e50;"'
            $modified = $true
        }
    }

    # 3. Handle extra </div> from previous runs
    if ($content -match '(?s)</header>\s*</div>\s*(<div class="container">|<main class="content-section")') {
        $content = $content -replace '(?s)</header>\s*</div>\s*(<div class="container">|<main class="content-section")', "</header>`r`n`r`n    `$1"
        $modified = $true
    }

    # 4. If there is still a hero-banner, replace it
    $hasDivHero = $content -match '(?s)<div class="hero-banner">\s*<div class="container">.*?</div>\s*</div>'
    $hasHeaderHero = $content -match '(?s)<header class="hero-banner">.*?</header>'

    if ($hasDivHero -or $hasHeaderHero) {
        $isRoot = ($file.Directory.Name -eq "ลองทำ")
        $prefix = if ($isRoot) { "" } else { "../" }
        $category = if ($isRoot) { "" } else { $file.Directory.Name }
        $pageName = $file.BaseName
        
        $breadcrumb = @"
            <div class="inner-breadcrumb">
                <a href="${prefix}index.html">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: text-bottom;"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    &#3627;&#3609;&#3657;&#3634;&#3627;&#3621;&#3633;&#3585;
                </a>
"@
        if (-not $isRoot) {
            $breadcrumb += @"
`r`n                <span>&gt;</span>
                <a href="#">$category</a>
"@
        }
        $breadcrumb += @"
`r`n                <span>&gt;</span>
                <span>$pageName</span>
            </div>
"@

        $newHeader = @"
    <header class="inner-hero" style="background-color: #2c3e50;">
        <div class="inner-hero-content">
            <h1>$pageName</h1>
$breadcrumb
        </div>
        <a href="#content-start" class="scroll-down-btn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </a>
    </header>
"@
        
        if ($hasDivHero) {
            $content = $content -replace '(?s)<div class="hero-banner">\s*<div class="container">.*?</div>\s*</div>', $newHeader
            $modified = $true
        }
        if ($hasHeaderHero) {
            $content = $content -replace '(?s)<header class="hero-banner">.*?</header>', $newHeader
            $modified = $true
        }
    }
    
    if ($content -match '<main class="content-section">') {
        $content = $content -replace '<main class="content-section">', '<main class="content-section" id="content-start">'
        $modified = $true
    }
    if ($content -match '<div class="content-section">') {
        $content = $content -replace '<div class="content-section">', '<div class="content-section" id="content-start">'
        $modified = $true
    }

    if ($modified) {
        [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
        Write-Host "Updated $($file.FullName)"
    }
}
