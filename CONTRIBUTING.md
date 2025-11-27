# Contributing to Cross-Platform Software Installer

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Your operating system and Python version
- Screenshots if applicable

### Suggesting Features

Feature suggestions are welcome! Please include:
- Clear use case for the feature
- How it would benefit users
- Any implementation ideas you have

### Submitting Changes

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
   - Follow the code style (PEP 8)
   - Add comments for complex logic
   - Update documentation if needed
4. **Test your changes**
   - Test on your platform
   - Ensure existing functionality still works
5. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of changes"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## Code Style Guidelines

- Follow [PEP 8](https://pep8.org/) for Python code
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions focused and concise
- Comment complex logic, but let code be self-documenting where possible

### Example:

```python
def download_application(self, app_name, url):
    """
    Download an application from the specified URL.

    Args:
        app_name (str): Name of the application
        url (str): Download URL

    Returns:
        Path: Path to downloaded file, or None if download failed
    """
    # Implementation here
```

## Adding New Applications

To add a new application to the installer:

1. Add entry to `APPLICATIONS` dictionary in [installer.py](installer.py):

```python
"Your Application": {
    "windows": "https://example.com/installer.exe",
    "linux": "package:app-name",
    "mac": "brew:app-name"
}
```

2. Test on at least one platform
3. Verify URLs are from official sources
4. Update the README.md table

## Testing

Before submitting a PR:

- [ ] Test on your operating system
- [ ] Verify the GUI displays correctly
- [ ] Test both successful and failed installations
- [ ] Check error messages are helpful
- [ ] Ensure no Python errors or warnings

## Documentation

When adding features:

- Update README.md with new functionality
- Add examples if applicable
- Update CUSTOMIZATION_GUIDE.md if relevant
- Include docstrings in code

## Questions?

Feel free to open an issue for any questions about contributing!

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers and help them learn
- Focus on what's best for the project
- Accept constructive criticism gracefully

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
