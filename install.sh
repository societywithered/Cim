#!/bin/sh
set -eu

REPO="SocietyWithered/cim"
BRANCH="main"

command -v python3 >/dev/null 2>&1 || {
    echo "Python 3 is required."
    exit 1
}
command -v curl >/dev/null 2>&1 || {
    echo "curl is required."
    exit 1
}

if [ -w /usr/local/bin ]; then
    DEST="/usr/local/bin"
else
    DEST="$HOME/.local/bin"
    mkdir -p "$DEST"
fi

curl -fsSL "https://raw.githubusercontent.com/$REPO/$BRANCH/cim.py" \
    -o "$DEST/cim"
chmod +x "$DEST/cim"

echo "Installed cim to $DEST/cim"
echo "Try: cim --help"
echo "If cim isn't found, add $DEST to your PATH."