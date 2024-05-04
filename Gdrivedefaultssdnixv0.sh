#!/bin/bash

# Requires root privileges
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

echo "Listing all mounted hard drives on the system:"
# List all mounted volumes and their device identifiers
diskutil list

# Assuming CloudMounter is installed and configured to mount
# the Flames Co. Database as a virtual drive
# Set CloudMounter directory as default for VRAM and hard disk operations
CLOUDMOUNTER_PATH="/Users/catdevzsh/Library/CloudStorage/CloudMounter-FlamesCo.Database/:home"

if [ -d "$CLOUDMOUNTER_PATH" ]; then
    echo "Setting $CLOUDMOUNTER_PATH as the default path for VRAM and disk operations."
    # Example of setting an environment variable or similar to use this path
    # This is a placeholder and might need adjustment based on actual use case
    export DEFAULT_STORAGE_PATH="$CLOUDMOUNTER_PATH"
else
    echo "CloudMounter path not found. Ensure CloudMounter is configured correctly."
fi

# Any additional commands to utilize the storage can be added here
# For example, redirecting cache files or other data to use the mounted path

echo "Setup complete."
