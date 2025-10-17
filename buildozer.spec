[app]
# Title dan package info
title = Jens Dilemma 3
package.name = jensdilamma3
package.domain = com.example

# Versi
version = 1.0

# Python version
python = 3.9

# Requirements
requirements = python3,kivy,android

# Permissions
permissions = INTERNET

# Orientation
orientation = landscape
fullscreen = 0

# Architecture
arch = armeabi-v7a

# Icons dan presplash
icon.filename = game/gui/window_icon.png
presplash.filename = game/gui/presplash.png

[buildozer]
# Log level: 0 = debug, 1 = info, 2 = warning, 3 = error
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1

# Build directory
build_dir = .buildozer

# Bin directory
bin_dir = ./bin
