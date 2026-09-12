$utf8 = [System.Text.Encoding]::UTF8
$tis620 = [System.Text.Encoding]::GetEncoding(874)

# Read the corrupted file as UTF8 bytes
$bytes = [System.IO.File]::ReadAllBytes("e:\งาน\ลองทำ\สิ่งแวดล้อม\การบริหารจัดการพลังงานและการเปลี่ยนแปลงสภาพภูมิอากาศ.html")

# Let's read it as string with UTF8
$str = [System.Text.Encoding]::UTF8.GetString($bytes)

# If it was read as ANSI and written as UTF8, then the string characters are actually the ANSI bytes!
# Convert string back to ANSI bytes
$recoveredBytes = [System.Text.Encoding]::GetEncoding(1252).GetBytes($str)

# Decode ANSI bytes as TIS-620
$recoveredStr = $tis620.GetString($recoveredBytes)

$recoveredStr.Substring(0, 500)
