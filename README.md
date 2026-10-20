# cim

A small cross-platform command that detects an available package manager and runs it for you.

## Requirements

- Python 3
- A supported package manager installed and configured

`cim` supports Termux, macOS, Windows, and common Linux distributions. Package names and availability vary by operating system and package manager.

## Install

### Linux, macOS, or Termux

```sh
curl -fsSL https://raw.githubusercontent.com/SocietyWithered/cim/main/install.sh | sh

Windows PowerShell

          
            
            
          
          irm https://raw.githubusercontent.com/SocietyWithered/cim/main/install.ps1 | iex
On Windows, open a new terminal after installing.
Usage

          
            
            
          
          cim install PACKAGE

Install multiple packages:

          
            
            
          
          cim install PACKAGE1 PACKAGE2
      Examples:

          
            
            
          
          cim install git
cim install curl vim

Supported package managers

Termux: pkg
macOS: Homebrew or MacPorts
Windows: winget, Chocolatey, or Scoop
Linux: APT, DNF, YUM, pacman, Zypper, APK, XBPS, Portage, or pkg

The package manager must already be installed. Some Linux installations require sudo privileges.
Troubleshooting

If cim is not found after installation, open a new terminal and check that its install directory is on your PATH.
If a package cannot be found, check the package’s name in your system’s package manager.
On Windows, make sure Python’s py launcher and a supported package manager are available.