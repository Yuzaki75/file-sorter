# File Sorter

A simple Python utility to sort files in a folder into subfolders by type or other rules. This repository contains a single script:

- Main script: [file_sorter.py](file_sorter.py)

## Features

- Sorts files by extension into categorized folders (e.g., Images, Documents, Audio, Video, Archives).
- Skips duplicates safely by renaming or leaving existing files untouched.
- Optional dry-run to preview actions before applying changes.
- Verbose output for transparency.

## Requirements

- Python 3.9+ (Windows, macOS, or Linux)

## Installation

No install needed—just clone or download the repository.

```powershell
# Clone (requires Git)
git clone "https://github.com/<your-username>/<your-repo>.git"
cd "<your-repo>"

# Or download the ZIP from GitHub and extract
```

## Usage (Windows)

Run from the folder containing the script.

```powershell
# Using the default Python on your system
python .\file_sorter.py --source "C:\Path\To\folder" --dry-run

# If Python is installed as 'py'
py .\file_sorter.py --source "C:\Path\To\folder" --dry-run
```

Common options (your script may differ—update as needed):

- `--source`: Path to the folder with files to sort.
- `--dest`: Output directory where sorted folders will be created (defaults to source).
- `--dry-run`: Show planned moves without changing files.
- `--verbose`: Print extra details.
- `--rules`: Optional JSON or simple mapping to customize categories.

Example:

```powershell
python .\file_sorter.py --source "C:\Users\charl\Downloads" --dest "C:\Users\charl\Downloads\Sorted" --verbose
```

## Configuration

If your script supports custom rules, place a `rules.json` next to the script:

```json
{
  "Images": ["jpg", "jpeg", "png", "gif", "bmp", "webp"],
  "Documents": ["pdf", "docx", "doc", "txt", "md", "xlsx", "pptx"],
  "Audio": ["mp3", "wav", "flac", "aac"],
  "Video": ["mp4", "mkv", "mov", "avi", "webm"],
  "Archives": ["zip", "rar", "7z", "tar", "gz"]
}
```

Then run:

```powershell
python .\file_sorter.py --source "C:\Path\To\folder" --rules .\rules.json
```

## Troubleshooting

- Ensure paths are quoted if they include spaces.
- If you see "command not found", verify Python is installed and added to PATH.
- Use `--dry-run` first to confirm what will happen.
- Run PowerShell as Administrator if moving files across protected locations.

## Contributing

- Fork the repo and create a feature branch.
- Make focused changes and open a pull request.
- Add examples and update this README if options change.

## License

Add your preferred license (e.g., MIT) and include a LICENSE file.
