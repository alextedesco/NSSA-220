#!/bin/bash

# Run with root account

rpm --import https://packages.microsoft.com/keys/microsoft.asc

touch /etc/yum.repos.d/vscode.repo

echo "[code]" >> /etc/yum.repos.d/vscode.repo
echo "name=Visual Studio Code" >> /etc/yum.repos.d/vscode.repo
echo "baseurl=https://packages.microsoft.com/yumrepos/vscode" >> /etc/yum.repos.d/vscode.repo
echo "enabled=1" >> /etc/yum.repos.d/vscode.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/vscode.repo
echo "gpgkey=https://packages.microsoft.com/keys/microsoft.asc" >> /etc/yum.repos.d/vscode.repo

dnf install code
