# National-Fuel-Pass-Nativefied
electron wrapper for Sri Lanka's national fuel pass website made with nativefier + build scripts

# Build Guide

## Ubuntu/Debain

1. Install all dependencies
    ```bash
    sudo apt update && sudo apt install nodejs npm python3 python3-pip git -y
    ```

2. install nativefier globally using npm
    ```bash
    npm install -g nativefier
    ```

3. clone and cd into the script
    ```bash
    git clone https://github.com/hirusha-adi/National-Fuel-Pass-Nativefied.git
    cd ./National-Fuel-Pass-Nativefied
    ```

4. run the build script
    ```bash
    python3 build.py
    ```


## Arch Linux

1. Install all dependencies
    ```bash
    sudo pacman -Syy nodejs npm python python-pip git --noconfirm
    ```

2. install nativefier globally using npm
    ```bash
    npm install -g nativefier
    ```

3. clone and cd into the script
    ```bash
    git clone https://github.com/hirusha-adi/National-Fuel-Pass-Nativefied.git
    cd ./National-Fuel-Pass-Nativefied
    ```

4. run the build script
    ```bash
    python build.py
    ```

## Windows

1. Download and install [NodeJS](https://nodejs.org/en/download/) (Windows Installer, npm is included in it)
2. Download and install [Python3](https://www.python.org/downloads/) (Make sure to check: **Python to PATH** on the first screen of the installer)
3. Install nativefier globally using npm
    ```
    npm install -g nativefier
    ```
4. Download the [source code](https://github.com/hirusha-adi/National-Fuel-Pass-Nativefied/archive/refs/heads/main.zip) and extract it
5. Open command prompt in that folder

![img1](https://cdn.discordapp.com/attachments/945257357867380747/998128679639056454/unknown.png)

6. run this command
    ```
    py build.py
    ```