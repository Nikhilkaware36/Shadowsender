#!/bin/bash

# Shadowsender uninstallation script

echo "Uninstalling Shadowsender..."

read -p "Are you sure you want to delete the Shadowsender folder? (y/n): " confirm

if [ "$confirm" = "y" ]; then
    SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
    cd "$SCRIPT_DIR"
    cd ..
    rm -rf Shadowsender
    echo "✅ Shadowsender has been removed successfully."
else
    echo "❌ Uninstallation canceled."
fi
