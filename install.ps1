$ErrorActionPreference = "Stop"

$dir = Join-Path $env:LOCALAPPDATA "cim"
New-Item -ItemType Directory -Force $dir | Out-Null

$url = "https://raw.githubusercontent.com/SocietyWithered/cim/main/cim.py"
Invoke-WebRequest $url -OutFile (Join-Path $dir "cim.py")

@'
@echo off
py "%~dp0cim.py" %*
'@ | Set-Content (Join-Path $dir "cim.cmd")

$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if (($userPath -split ";") -notcontains $dir) {
    [Environment]::SetEnvironmentVariable(
        "Path",
        (($userPath.TrimEnd(";") + ";" + $dir).TrimStart(";")),
        "User"
    )
}

Write-Host "Installed cim. Open a new terminal, then run: cim --help"