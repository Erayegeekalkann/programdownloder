# Cross-Platform Software Installer

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/yourusername/program_downloder)

A modern, cross-platform software installer built with Python that streamlines the installation of essential development tools and applications. Features an intuitive GUI built with Tkinter, asynchronous download handling, and intelligent platform detection.

## Project Overview

This project was developed to solve the common problem of setting up new development environments. Instead of manually downloading and installing each application from different websites, this tool provides a centralized, automated solution that works across all major operating systems.

### Key Technical Features

- **Cross-Platform Architecture**: Single codebase supports Windows, Linux, and macOS through platform abstraction
- **Asynchronous Operations**: Multi-threaded download and installation to prevent GUI freezing
- **Dynamic URL Resolution**: Handles both direct downloads and package manager integrations
- **Clean Architecture**: Separation of concerns between UI, download logic, and platform-specific handlers
- **No External Dependencies**: Uses only Python standard library (tkinter, urllib, subprocess, threading)

### Supported Applications

- **Development Tools**: Visual Studio Code, Vim, Java JDK
- **Utilities**: 7-Zip, VLC Media Player, Firefox
- **Communication & Entertainment**: Discord, Spotify, Steam

## Requirements

- Python 3.7 or higher
- Internet connection for downloading applications

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/program_downloder.git
cd program_downloder
```

2. No additional dependencies required! The installer uses Python's built-in libraries.

## Usage

### Windows
```bash
python installer.py
```

Or simply double-click `installer.py`

### Linux/macOS
```bash
python3 installer.py
```

Or make it executable:
```bash
chmod +x installer.py
./installer.py
```

## Architecture & Design

### System Architecture

```
┌─────────────────────────────────────────┐
│         User Interface (Tkinter)        │
│  - Checkbox selection                   │
│  - Installation logging                 │
│  - Progress tracking                    │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      Application Controller             │
│  - Platform detection                   │
│  - Installation orchestration           │
│  - Thread management                    │
└──────────────┬──────────────────────────┘
               │
     ┌─────────┴─────────┐
     │                   │
┌────▼────────┐   ┌──────▼──────────────┐
│   Download  │   │  Platform Handlers  │
│   Manager   │   │  - Windows (.exe)   │
│             │   │  - Linux (apt/deb)  │
└─────────────┘   │  - macOS (dmg/brew) │
                  └─────────────────────┘
```

### Design Decisions

1. **Tkinter for GUI**: Chosen for zero external dependencies and cross-platform compatibility
2. **Threading**: Prevents UI freezing during long downloads
3. **Modular URL System**: Easy to add new applications or update download links
4. **Platform Abstraction**: Single interface for multiple package managers (apt, brew, snap)

## How It Works

1. **Platform Detection** - Automatically identifies OS (Windows/Linux/macOS)
2. **Application Selection** - User chooses applications via checkbox interface
3. **Download Management** - Downloads files to ~/Downloads/InstallerDownloads
4. **Installation Handling** - Launches installers (Windows), opens DMG files (macOS), or provides CLI commands (Linux)
5. **Progress Logging** - Real-time feedback with status indicators

## Platform-Specific Notes

### Windows
- Applications will be downloaded and installers will launch automatically
- Follow each installer's wizard to complete installation

### macOS
- Direct downloads will open DMG files
- For Homebrew packages, you'll need to run the suggested commands manually
- Homebrew must be installed for package-based installations

### Linux
- Direct downloads are provided for Debian-based systems (.deb files)
- For apt packages, you'll need to run the suggested commands manually with sudo
- Snap packages require snapd to be installed

## Security Notice

This installer downloads software from official sources:
- All URLs point to official vendor websites or CDNs
- Always verify the source before running any installer
- Some installations may require administrator privileges

## Supported Applications

| Application | Windows | Linux | macOS |
|------------|---------|-------|-------|
| 7-Zip | ✅ | ✅ | ✅ |
| Visual Studio Code | ✅ | ✅ | ✅ |
| Vim | ✅ | ✅ | ✅ |
| VLC Media Player | ✅ | ✅ | ✅ |
| Java JDK | ✅ | ✅ | ✅ |
| Steam | ✅ | ✅ | ✅ |
| Spotify | ✅ | ✅ | ✅ |
| Firefox | ✅ | ✅ | ✅ |
| Discord | ✅ | ✅ | ✅ |

## Customization

You can easily add more applications by editing the `APPLICATIONS` dictionary in [installer.py](installer.py). Each application needs URLs or package names for each supported platform.

Example:
```python
"Your App": {
    "windows": "https://example.com/app-installer.exe",
    "linux": "package:app-name",  # For apt-get
    "mac": "brew:app-name"  # For Homebrew
}
```

## Troubleshooting

**Issue**: "Python not found"
- **Solution**: Install Python from [python.org](https://www.python.org/downloads/)

**Issue**: Downloads fail
- **Solution**: Check your internet connection and firewall settings

**Issue**: Installer won't launch on Windows
- **Solution**: Right-click and select "Open with" → "Python"

**Issue**: Permission denied on Linux/macOS
- **Solution**: Run `chmod +x installer.py` to make it executable

## License

MIT License - Feel free to use and modify as needed

## Contributing

Contributions are welcome! Feel free to:
- Add more applications
- Improve the UI
- Add features
- Fix bugs

## Disclaimer

This installer is a convenience tool that downloads software from official sources. Users are responsible for:
- Reviewing and accepting each application's license terms
- Ensuring downloaded software is appropriate for their use
- Maintaining security best practices

## Technical Highlights

### Code Quality
- **Type Safety**: Proper error handling and exception management
- **Clean Code**: Follows PEP 8 style guidelines
- **Modular Design**: Separate methods for each platform's installation logic
- **Documentation**: Comprehensive docstrings and comments

### User Experience
- **Cozy Design**: Warm color palette (#f5f5f0, #6b8e23, #8b7355)
- **Responsive UI**: Scrollable interface adapts to different screen sizes
- **Clear Feedback**: Color-coded log messages with emoji indicators
- **Batch Operations**: Select/Deselect all functionality

### Security Considerations
- **Official Sources Only**: All downloads from verified vendor URLs
- **No Credential Storage**: No sensitive data handling
- **User Confirmation**: Explicit consent before any installation
- **Transparent Logging**: All actions logged for user review

## Future Enhancements

Potential improvements to consider:
- [ ] Add download progress bars with percentage
- [ ] Implement checksum verification for security
- [ ] Add configuration file for custom application lists
- [ ] Support for portable/non-admin installations
- [ ] Create installer packages (.exe for Windows, .app for macOS)
- [ ] Add update checking for already-installed applications
- [ ] Multi-language support (i18n)
- [ ] Dark/Light theme toggle

## Development

### Project Structure
```
program_downloder/
├── installer.py          # Main application
├── README.md            # Documentation
├── LICENSE              # MIT License
├── requirements.txt     # Dependencies (none!)
└── .gitignore          # Git exclusions
```

### Testing Locally
```bash
# Clone the repository
git clone https://github.com/yourusername/program_downloder.git
cd program_downloder

# Run the installer
python installer.py
```

## Screenshots

![Screenshot](https://github.com/user-attachments/assets/6316dd04-3ce9-46fd-b9c1-0a8c2e741b76)

The installer features a professional, cozy interface with:
- Warm, accessible color palette
- Clean checkbox selection system
- Real-time installation logging with status indicators
- Intuitive button layout for bulk operations
