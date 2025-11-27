#!/usr/bin/env python3
"""
Cross-Platform Software Installer

A modern, cross-platform software installer that streamlines the installation
of essential development tools and applications across Windows, Linux, and macOS.

Features:
    - Intuitive GUI built with Tkinter
    - Asynchronous download handling with threading
    - Intelligent platform detection and URL resolution
    - Support for direct downloads and package managers (apt, brew, snap)
    - No external dependencies (Python standard library only)

Author: [Your Name]
License: MIT
Version: 1.0.0
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import platform
import subprocess
import urllib.request
import os
import sys
import threading
import webbrowser
from pathlib import Path

# ============================================================================
# APPLICATION DATABASE
# ============================================================================
# Dictionary mapping applications to platform-specific download URLs or
# package manager commands. Supports three installation methods:
#   - Direct URL: Downloads and launches installer
#   - package:name: Uses apt-get (Linux)
#   - brew:name: Uses Homebrew (macOS)
#   - snap:name: Uses Snap (Linux)
APPLICATIONS = {
    "7-Zip": {
        "windows": "https://www.7-zip.org/a/7z2408-x64.exe",
        "linux": "package:p7zip-full",  # Using package manager
        "mac": "brew:p7zip"
    },
    "Visual Studio Code": {
        "windows": "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user",
        "linux": "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64",
        "mac": "https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal"
    },
    "Vim": {
        "windows": "https://github.com/vim/vim-win32-installer/releases/download/v9.1.0000/gvim_9.1.0000_x64.exe",
        "linux": "package:vim",
        "mac": "brew:vim"
    },
    "VLC Media Player": {
        "windows": "https://get.videolan.org/vlc/3.0.21/win64/vlc-3.0.21-win64.exe",
        "linux": "package:vlc",
        "mac": "https://get.videolan.org/vlc/3.0.21/macosx/vlc-3.0.21-universal.dmg"
    },
    "Java JDK": {
        "windows": "https://download.oracle.com/java/21/latest/jdk-21_windows-x64_bin.exe",
        "linux": "package:openjdk-21-jdk",
        "mac": "brew:openjdk@21"
    },
    "Steam": {
        "windows": "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe",
        "linux": "package:steam",
        "mac": "https://cdn.akamai.steamstatic.com/client/installer/steam.dmg"
    },
    "Spotify": {
        "windows": "https://download.scdn.co/SpotifySetup.exe",
        "linux": "snap:spotify",
        "mac": "https://download.scdn.co/Spotify.dmg"
    },
    "Firefox": {
        "windows": "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US",
        "linux": "package:firefox",
        "mac": "https://download.mozilla.org/?product=firefox-latest-ssl&os=osx&lang=en-US"
    },
    "Discord": {
        "windows": "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64",
        "linux": "https://discord.com/api/download?platform=linux&format=deb",
        "mac": "https://discord.com/api/download?platform=osx"
    }
}


class InstallerGUI:
    """
    Main GUI application class for the cross-platform installer.

    This class handles the entire user interface, download management,
    and installation orchestration. Uses Tkinter for GUI and threading
    for asynchronous operations.

    Attributes:
        root (tk.Tk): Main Tkinter window
        os_type (str): Detected operating system ('windows', 'linux', or 'mac')
        app_vars (dict): Dictionary mapping app names to their checkbox variables
        status_text (ScrolledText): Text widget for installation logging
    """

    def __init__(self, root):
        """
        Initialize the installer GUI.

        Args:
            root (tk.Tk): The main Tkinter window instance
        """
        self.root = root
        self.root.title("Software Installer")
        self.root.geometry("600x700")
        self.root.resizable(False, False)

        # Detect OS - determines which URLs/packages to use
        self.os_type = self.detect_os()

        # Variables to store checkbox states (BooleanVar for each app)
        self.app_vars = {}

        # Apply styling and color scheme
        self.setup_styles()

        # Build the user interface
        self.create_ui()

    def detect_os(self):
        """
        Detect the current operating system.

        Uses Python's platform.system() to identify the OS, which is crucial
        for selecting the correct download URLs and installation methods.

        Returns:
            str: One of 'windows', 'linux', 'mac', or 'unknown'
        """
        system = platform.system().lower()
        if system == "windows":
            return "windows"
        elif system == "linux":
            return "linux"
        elif system == "darwin":  # macOS identifies as 'Darwin'
            return "mac"
        else:
            return "unknown"

    def setup_styles(self):
        """
        Configure the visual styling and color scheme.

        Defines a cozy, professional color palette and applies it to
        Tkinter and ttk widgets. The warm tones create an inviting
        user experience while maintaining professionalism.
        """
        # Cozy color palette
        self.bg_color = "#f5f5f0"  # Warm off-white
        self.accent_color = "#6b8e23"  # Olive green
        self.button_color = "#8b7355"  # Brown
        self.text_color = "#2f2f2f"  # Dark gray

        self.root.configure(bg=self.bg_color)

        # Configure ttk styles
        style = ttk.Style()
        style.theme_use('clam')

        style.configure('Cozy.TCheckbutton',
                       background=self.bg_color,
                       foreground=self.text_color,
                       font=('Segoe UI', 10))

        style.configure('Title.TLabel',
                       background=self.bg_color,
                       foreground=self.accent_color,
                       font=('Segoe UI', 16, 'bold'))

        style.configure('Subtitle.TLabel',
                       background=self.bg_color,
                       foreground=self.text_color,
                       font=('Segoe UI', 9))

    def create_ui(self):
        """Create the main user interface"""
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color, pady=20)
        header_frame.pack(fill=tk.X)

        title = ttk.Label(header_frame, text="📦 Software Installer", style='Title.TLabel')
        title.pack()

        subtitle = ttk.Label(
            header_frame,
            text=f"Platform: {self.os_type.capitalize()} | Select applications to install",
            style='Subtitle.TLabel'
        )
        subtitle.pack(pady=(5, 0))

        # Separator
        separator1 = ttk.Separator(self.root, orient='horizontal')
        separator1.pack(fill=tk.X, padx=20, pady=10)

        # Checkbox frame with scrollbar
        canvas_frame = tk.Frame(self.root, bg=self.bg_color)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        # Create canvas and scrollbar
        canvas = tk.Canvas(canvas_frame, bg=self.bg_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.bg_color)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Add checkboxes for each application
        for app_name in sorted(APPLICATIONS.keys()):
            var = tk.BooleanVar(value=False)
            self.app_vars[app_name] = var

            cb_frame = tk.Frame(scrollable_frame, bg=self.bg_color, pady=5)
            cb_frame.pack(fill=tk.X, padx=10)

            cb = ttk.Checkbutton(
                cb_frame,
                text=f"  {app_name}",
                variable=var,
                style='Cozy.TCheckbutton'
            )
            cb.pack(anchor=tk.W)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Selection buttons
        select_frame = tk.Frame(self.root, bg=self.bg_color, pady=10)
        select_frame.pack(fill=tk.X, padx=20)

        select_all_btn = tk.Button(
            select_frame,
            text="Select All",
            command=self.select_all,
            bg=self.button_color,
            fg="white",
            font=('Segoe UI', 9),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2"
        )
        select_all_btn.pack(side=tk.LEFT, padx=5)

        deselect_all_btn = tk.Button(
            select_frame,
            text="Deselect All",
            command=self.deselect_all,
            bg=self.button_color,
            fg="white",
            font=('Segoe UI', 9),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2"
        )
        deselect_all_btn.pack(side=tk.LEFT, padx=5)

        # Separator
        separator2 = ttk.Separator(self.root, orient='horizontal')
        separator2.pack(fill=tk.X, padx=20, pady=10)

        # Install button
        install_btn = tk.Button(
            self.root,
            text="Install Selected Applications",
            command=self.start_installation,
            bg=self.accent_color,
            fg="white",
            font=('Segoe UI', 12, 'bold'),
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        install_btn.pack(pady=10)

        # Status text area
        status_label = ttk.Label(
            self.root,
            text="Installation Log:",
            style='Subtitle.TLabel'
        )
        status_label.pack(anchor=tk.W, padx=20, pady=(10, 5))

        self.status_text = scrolledtext.ScrolledText(
            self.root,
            height=8,
            bg="white",
            fg=self.text_color,
            font=('Consolas', 9),
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.status_text.pack(fill=tk.BOTH, padx=20, pady=(0, 20))
        self.status_text.config(state=tk.DISABLED)

    def select_all(self):
        """Select all checkboxes"""
        for var in self.app_vars.values():
            var.set(True)

    def deselect_all(self):
        """Deselect all checkboxes"""
        for var in self.app_vars.values():
            var.set(False)

    def log_message(self, message):
        """Add a message to the status text area"""
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, f"{message}\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)
        self.root.update()

    def start_installation(self):
        """Start the installation process in a separate thread"""
        selected_apps = [app for app, var in self.app_vars.items() if var.get()]

        if not selected_apps:
            messagebox.showwarning("No Selection", "Please select at least one application to install.")
            return

        # Confirm installation
        confirm = messagebox.askyesno(
            "Confirm Installation",
            f"Install {len(selected_apps)} application(s)?\n\n" + "\n".join(f"• {app}" for app in selected_apps)
        )

        if not confirm:
            return

        # Clear previous logs
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.config(state=tk.DISABLED)

        # Run installation in a thread to avoid freezing GUI
        thread = threading.Thread(target=self.install_applications, args=(selected_apps,))
        thread.daemon = True
        thread.start()

    def install_applications(self, selected_apps):
        """Install the selected applications"""
        self.log_message("=" * 50)
        self.log_message(f"Starting installation for {len(selected_apps)} application(s)...")
        self.log_message("=" * 50)

        for app_name in selected_apps:
            self.log_message(f"\n📦 Processing: {app_name}")

            app_info = APPLICATIONS.get(app_name)
            if not app_info:
                self.log_message(f"❌ Error: No configuration found for {app_name}")
                continue

            url_or_package = app_info.get(self.os_type)
            if not url_or_package:
                self.log_message(f"❌ Error: {app_name} not supported on {self.os_type}")
                continue

            try:
                self.install_single_app(app_name, url_or_package)
            except Exception as e:
                self.log_message(f"❌ Error installing {app_name}: {str(e)}")

        self.log_message("\n" + "=" * 50)
        self.log_message("Installation process completed!")
        self.log_message("=" * 50)
        messagebox.showinfo("Installation Complete", "All selected applications have been processed. Check the log for details.")

    def install_single_app(self, app_name, url_or_package):
        """Install a single application"""
        # Handle package manager installations
        if url_or_package.startswith("package:"):
            package_name = url_or_package.split(":", 1)[1]
            self.install_via_package_manager(app_name, package_name)
        elif url_or_package.startswith("brew:"):
            package_name = url_or_package.split(":", 1)[1]
            self.install_via_homebrew(app_name, package_name)
        elif url_or_package.startswith("snap:"):
            package_name = url_or_package.split(":", 1)[1]
            self.install_via_snap(app_name, package_name)
        else:
            # Direct download
            self.download_and_install(app_name, url_or_package)

    def install_via_package_manager(self, app_name, package_name):
        """Install via Linux package manager (apt)"""
        self.log_message(f"Installing {app_name} via package manager...")
        self.log_message(f"ℹ️  Package: {package_name}")
        self.log_message(f"⚠️  This requires sudo privileges. Please run the following command manually:")
        self.log_message(f"    sudo apt-get install -y {package_name}")

    def install_via_homebrew(self, app_name, package_name):
        """Install via Homebrew (macOS)"""
        self.log_message(f"Installing {app_name} via Homebrew...")
        self.log_message(f"ℹ️  Package: {package_name}")

        try:
            # Check if brew is installed
            subprocess.run(["brew", "--version"], capture_output=True, check=True)
            self.log_message(f"⚠️  Please run: brew install {package_name}")
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.log_message("❌ Homebrew not found. Please install Homebrew first:")
            self.log_message("    /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")

    def install_via_snap(self, app_name, package_name):
        """Install via Snap (Linux)"""
        self.log_message(f"Installing {app_name} via Snap...")
        self.log_message(f"ℹ️  Package: {package_name}")
        self.log_message(f"⚠️  Please run: sudo snap install {package_name}")

    def download_and_install(self, app_name, url):
        """Download and install from URL"""
        self.log_message(f"Downloading {app_name}...")

        # Determine file extension
        if self.os_type == "windows":
            ext = ".exe"
        elif self.os_type == "mac":
            ext = ".dmg"
        else:
            ext = ".deb"

        # Create downloads directory
        download_dir = Path.home() / "Downloads" / "InstallerDownloads"
        download_dir.mkdir(parents=True, exist_ok=True)

        # Sanitize filename
        filename = app_name.replace(" ", "_") + ext
        filepath = download_dir / filename

        try:
            # Download the file
            self.log_message(f"⬇️  Downloading to: {filepath}")
            urllib.request.urlretrieve(url, filepath)
            self.log_message(f"✅ Downloaded successfully!")

            # Open the file location or start installation
            if self.os_type == "windows":
                self.log_message(f"ℹ️  Opening installer...")
                os.startfile(filepath)
                self.log_message(f"✅ Installer launched. Please follow the installation wizard.")
            elif self.os_type == "mac":
                self.log_message(f"ℹ️  Opening DMG file...")
                subprocess.run(["open", filepath])
                self.log_message(f"✅ DMG opened. Please drag the app to Applications folder.")
            else:
                self.log_message(f"ℹ️  To install, run:")
                self.log_message(f"    sudo dpkg -i {filepath}")
                self.log_message(f"    sudo apt-get install -f")

        except Exception as e:
            self.log_message(f"❌ Download failed: {str(e)}")
            self.log_message(f"ℹ️  You can manually download from: {url}")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = InstallerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
