# python-utils
An assembly of personal Python utility functions/classes to serve my own devilish purposes

## Updating Python Version Locally

Follow below steps. Can also read this [Stack Overflow article](https://stackoverflow.com/questions/3696124/changing-python-path-on-mac)
1. Go to the [Python download page](https://www.python.org/downloads/) and follow the instructions there to download an installer (safe for updates).
2. Update the `~/.bash_profile` and/or `~/.zprofile` files to update the PATH extension to point to the latest version of Python downloaded (these are usually stored at `/Library/Frameworks/Python.framework/Versions/...`)
3. Repoint the `python` command alias symlink by going to `/usr/local/bin` and executing `cp python3 python` (will work assuming the installer updated the `python3` alias to the latest version)