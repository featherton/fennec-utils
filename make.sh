#!/bin/bash

echo "Preparing for clean build"
rm -rf ./build ./dist ./fennec-utils.spec ./fennec-utils
echo "Building with pyinstaller..."
pyinstaller --onefile ./fennec-utils.py
echo "Copying built executable to project root directory..."
cp ./dist/fennec-utils ./fennec-utils
echo "Cleaning everything up..."
rm -rf ./build ./dist ./fennec-utils.spec
echo "Installing final executable..."
sudo mv ./fennec-utils /bin/fennec-utils
