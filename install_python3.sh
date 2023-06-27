#!/bin/bash

# Install Python 3
sudo apt update
sudo apt install -y python3

# Install required Python packages
sudo apt install -y python3-pip
pip3 install numpy matplotlib openpyxl pandas

# Install additional packages
pip3 install collections sys

pip3 install gdown

echo "Python 3 and required packages installed successfully."
