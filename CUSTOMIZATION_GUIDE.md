# Customization Guide - Make This Project Your Own!

This guide will help you customize the installer to make it uniquely yours and demonstrate your creativity to universities.

## 🎨 Easy Customizations (Beginner-Friendly)

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

**Location**: [installer.py:79-91](installer.py#L79-L91)

```python
# Change fonts to match your style
style.configure('Cozy.TCheckbutton',
               font=('Arial', 10))  # Try: 'Helvetica', 'Courier New', 'Comic Sans MS'

style.configure('Title.TLabel',
               font=('Impact', 18, 'bold'))  # Try different sizes and weights
```

## 🔧 Intermediate Customizations

### 5. Add Categories/Sections

Group applications by type (Dev Tools, Media, Gaming, etc.):

```python
CATEGORIES = {
    "Development Tools": ["Visual Studio Code", "Vim", "Java JDK"],
    "Utilities": ["7-Zip", "VLC Media Player", "Firefox"],
    "Gaming & Social": ["Steam", "Discord", "Spotify"]
}
```

Then modify the checkbox creation to add section headers.

### 6. Add Sound Effects

Install `pygame` and add sound on completion:

```python
import pygame
pygame.mixer.init()
# Play sound when installation completes
pygame.mixer.music.load('success.mp3')
pygame.mixer.music.play()
```

### 7. Add a Welcome Screen

Create a splash screen that appears before the main window:

```python
def show_welcome(self):
    welcome = tk.Toplevel(self.root)
    welcome.title("Welcome")
    label = tk.Label(welcome, text="Welcome to My Installer!\nMade by [Your Name]",
                     font=('Arial', 14))
    label.pack(pady=20)
    btn = tk.Button(welcome, text="Continue", command=welcome.destroy)
    btn.pack(pady=10)
```

### 8. Add Application Icons

Use `tkinter.PhotoImage` to add icons next to each checkbox:

```python
icon = tk.PhotoImage(file="icons/vscode.png")
label = tk.Label(cb_frame, image=icon)
label.image = icon  # Keep a reference
label.pack(side=tk.LEFT)
```

## 🚀 Advanced Customizations

### 9. Add Download Progress Bars

Replace text logging with visual progress bars:

```python
from tkinter import ttk

def download_with_progress(self, url, filepath):
    response = urllib.request.urlopen(url)
    total_size = int(response.headers.get('content-length', 0))

    progress = ttk.Progressbar(self.root, length=300, mode='determinate')
    progress.pack()

    downloaded = 0
    with open(filepath, 'wb') as f:
        while True:
            chunk = response.read(8192)
            if not chunk:
                break
            f.write(chunk)
            downloaded += len(chunk)
            progress['value'] = (downloaded / total_size) * 100
            self.root.update()
```

### 10. Add Configuration File Support

Let users save their preferences:

```python
import json

def save_preferences(self):
    prefs = {app: var.get() for app, var in self.app_vars.items()}
    with open('config.json', 'w') as f:
        json.dump(prefs, f)

def load_preferences(self):
    try:
        with open('config.json', 'r') as f:
            prefs = json.load(f)
            for app, selected in prefs.items():
                if app in self.app_vars:
                    self.app_vars[app].set(selected)
    except FileNotFoundError:
        pass
```

### 11. Add Update Checker

Check if apps are already installed:

```python
def is_installed(self, app_name):
    if self.os_type == "windows":
        # Check Windows registry or Program Files
        pass
    elif self.os_type == "linux":
        result = subprocess.run(['which', app_name.lower()],
                              capture_output=True)
        return result.returncode == 0
```

### 12. Create Installer Profiles

Let users save/load different installation profiles (e.g., "Gaming Setup", "Developer Setup"):

```python
PROFILES = {
    "Developer": ["Visual Studio Code", "Git", "Java JDK", "Docker"],
    "Gamer": ["Steam", "Discord"],
    "Content Creator": ["VLC Media Player", "Blender", "OBS Studio"]
}
```

## 🎓 University-Specific Customizations

### Make It Stand Out:

1. **Add Your Personal Touch**:
   - Custom color scheme that reflects your style
   - Personal logo or branding
   - Your name in the about section

2. **Show Technical Skills**:
   - Add unit tests (pytest)
   - Implement logging to a file
   - Add command-line arguments support
   - Create a configuration file format

3. **Demonstrate Problem-Solving**:
   - Add retry logic for failed downloads
   - Implement bandwidth throttling
   - Add checksum verification
   - Support for offline installation (pre-downloaded files)

4. **Show Design Thinking**:
   - A/B test different UI layouts
   - User feedback system
   - Accessibility features (keyboard shortcuts, screen reader support)
   - Multi-language support

## 📝 Documentation Tips

Universities love good documentation! Add:

1. **Personal README Section**:
```markdown
## About This Project

I created this installer to solve a problem I personally faced: setting up
new computers for programming takes hours. This tool reduces setup time from
3+ hours to under 30 minutes.

### What I Learned
- Cross-platform development challenges
- GUI design principles
- Asynchronous programming
- User experience optimization
```

2. **Development Blog/Journal**:
Create `DEVELOPMENT.md` documenting your process:
- Initial idea and motivation
- Challenges faced and solutions
- Iterations and improvements
- Future plans

3. **Code Comments**:
Add thoughtful comments explaining *why* not just *what*:
```python
# Using threading to prevent GUI freeze during long downloads
# Alternative considered: asyncio, but threading is simpler for this use case
thread = threading.Thread(target=self.install_applications, args=(selected_apps,))
```

## 🌟 Example: Complete Customization

Here's a quick transformation you could do:

**Theme**: "Cyberpunk Developer Setup"
- Color: Dark purple/cyan theme
- Title: "⚡ CyberDev Installer"
- Apps: Focus on dev tools (VSCode, Git, Docker, Node.js, Python)
- Features: Matrix-style text in log, neon button effects
- Unique: Add ASCII art logo, animated loading

This would show creativity, technical skill, and personal branding!

---

**Remember**: The best customization is one that:
1. Solves a real problem for you
2. Shows your unique style
3. Demonstrates technical understanding
4. Is well-documented

Good luck with your university application! 🎓
