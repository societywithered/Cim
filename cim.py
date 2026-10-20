#!/usr/bin/env python3
import os
import platform
import shutil
import subprocess
import sys


def find_manager(candidates):
    for name, command in candidates:
        if shutil.which(name):
            return command
    return None


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help", "help"):
        print("Usage: cim install PACKAGE [PACKAGE ...]")
        return 0

    if args[0] != "install" or len(args) < 2:
        print("Usage: cim install PACKAGE [PACKAGE ...]", file=sys.stderr)
        return 2

    packages = args[1:]
    system = platform.system().lower()
    is_termux = "com.termux" in os.environ.get("PREFIX", "")

    if is_termux:
        command = ["pkg", "install", "-y", *packages]

    elif system == "darwin":
        command = find_manager([
            ("brew", ["brew", "install"]),
            ("port", ["port", "install"]),
        ])
        if not command:
            print("Install Homebrew or MacPorts first.", file=sys.stderr)
            return 1
        command += packages

    elif system == "windows":
        command = find_manager([
            ("winget", ["winget", "install", "--exact"]),
            ("choco", ["choco", "install", "-y"]),
            ("scoop", ["scoop", "install"]),
        ])
        if not command:
            print("Install winget, Chocolatey, or Scoop first.", file=sys.stderr)
            return 1
        command += packages

    elif system == "linux":
        command = find_manager([
            ("apt-get", ["apt-get", "install", "-y"]),
            ("apt", ["apt", "install", "-y"]),
            ("dnf", ["dnf", "install", "-y"]),
            ("yum", ["yum", "install", "-y"]),
            ("pacman", ["pacman", "-S", "--needed", "--noconfirm"]),
            ("zypper", ["zypper", "--non-interactive", "install"]),
            ("apk", ["apk", "add"]),
            ("xbps-install", ["xbps-install", "-Sy"]),
            ("emerge", ["emerge"]),
            ("pkg", ["pkg", "install", "-y"]),
        ])
        if not command:
            print("No supported Linux package manager found.", file=sys.stderr)
            return 1

        command += packages

        if not is_termux and os.geteuid() != 0:
            if not shutil.which("sudo"):
                print("Run as root or install sudo.", file=sys.stderr)
                return 1
            command.insert(0, "sudo")

    else:
        print(f"Unsupported operating system: {system}", file=sys.stderr)
        return 1

    try:
        return subprocess.call(command)
    except FileNotFoundError:
        print(f"Command not found: {command[0]}", file=sys.stderr)
        return 127


if __name__ == "__main__":
    sys.exit(main())