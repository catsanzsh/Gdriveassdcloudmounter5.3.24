a
# Define the script contents
import os

# Define the main folder path
main_folder_path = '$HOME/Google Drive"'


script_contents = """
# Your original script content goes here
"""

# Modify the script to use Google Drive instead of iCloud
google_drive_script = script_contents.replace(
 
    'GOOGLE_DRIVE_DIR="$HOME/Google Drive"'
).replace(
    '"$ICLOUD_DIR/"',
    '"$GOOGLE_DRIVE_DIR/"'
).replace(
    'ICLOUD_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs"',
    'GOOGLE_DRIVE_DIR="$HOME/Google Drive"'
).replace(
    '"$ICLOUD_DIR/"',
    '"$GOOGLE_DRIVE_DIR/"'
)

# Adding a check for Google Drive directory at the start of the script
google_drive_check = '''
# Check if Google Drive directory exists
if [ ! -d "$GOOGLE_DRIVE_DIR" ]; then
    echo "Google Drive directory not found at $GOOGLE_DRIVE_DIR. Please ensure Google Drive is installed and configured."
    exit 1
fi
'''

google_drive_script = google_drive_script.replace(
    '# Simplified loop to move directories and create symbolic links',
    google_drive_check + '\n\n# Simplified loop to move directories and create symbolic links'
)

# Save the modified script
google_drive_script_path = os.path.join(main_folder_path, 'google_drive_sync.sh')
with open(google_drive_script_path, 'w') as script_file:
    script_file.write(google_drive_script)

google_drive_script_path


#### [C] @Flames Co. 20XX