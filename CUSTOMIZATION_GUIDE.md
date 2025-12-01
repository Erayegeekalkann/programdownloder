# Customization Guide - Make This Project Your Own!

This guide will help you customize the installer to make it uniquely yours!

## Customizations

### 1. Change the Color Scheme

**Location**: [installer.py:69-73](installer.py#L69-L73)

```python
def setup_styles(self):
    # Current cozy palette
    self.bg_color = "#f5f5f0"      # Background
    self.accent_color = "#6b8e23"  # Main accent (olive green)
    self.button_color = "#8b7355"  # Buttons (brown)
    self.text_color = "#2f2f2f"    # Text
```

**Ideas to try**:
- **Modern Dark Theme**: `bg_color="#2b2d31"`, `accent_color="#5865f2"`, `button_color="#4752c4"`
- **Ocean Theme**: `bg_color="#e6f3ff"`, `accent_color="#0077be"`, `button_color="#005a8c"`
- **Sunset Theme**: `bg_color="#fff5e6"`, `accent_color="#ff6b35"`, `button_color="#f7931e"`
- **Forest Theme**: `bg_color="#e8f5e9"`, `accent_color="#2e7d32"`, `button_color="#1b5e20"`
- **Lavender Theme**: `bg_color="#f3e5f5"`, `accent_color="#7b1fa2"`, `button_color="#6a1b9a"`

### 2. Change the Title and Branding

**Location**: [installer.py:108](installer.py#L108)

```python
title = ttk.Label(header_frame, text="📦 Software Installer", style='Title.TLabel')
```

**Ideas**:
- "DevKit Installer"
- "Quick Setup Tool"
- "Developer's Toolkit"
- "One-Click Environment Setup"
- "Essential Apps Installer"

### 3. Add Different Applications

**Location**: [installer.py:19-65](installer.py#L19-L65)

Add your favorite tools! Examples:

```python
"Git": {
    "windows": "https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe",
    "linux": "package:git",
    "mac": "brew:git"
},
"Node.js": {
    "windows": "https://nodejs.org/dist/v20.11.0/node-v20.11.0-x64.msi",
    "linux": "package:nodejs",
    "mac": "brew:node"
},
"Python": {
    "windows": "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe",
    "linux": "package:python3",
    "mac": "brew:python@3.12"
},
"Docker": {
    "windows": "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe",
    "linux": "package:docker.io",
    "mac": "https://desktop.docker.com/mac/main/amd64/Docker.dmg"
},
"Blender": {
    "windows": "https://download.blender.org/release/Blender4.0/blender-4.0.2-windows-x64.msi",
    "linux": "snap:blender",
    "mac": "https://download.blender.org/release/Blender4.0/blender-4.0.2-macos-x64.dmg"
}
```

### 4. Customize Font Style

### 5. Add Categories/Sections

Group applications by type (Dev Tools, Media, Gaming, etc.):

### 6. Add Sound Effects

Install `pygame` and add sound on completion:

### 7. Add a Welcome Screen

Create a splash screen that appears before the main window:

### 8. Add Application Icons

Use `tkinter.PhotoImage` to add icons next to each checkbox:

### 9. Add Download Progress Bars

Replace text logging with visual progress bars:

### 11. Add Update Checker

Check if apps are already installed:


### 12. Create Installer Profiles

Let users save/load different installation profiles (e.g., "Gaming Setup", "Developer Setup"):
