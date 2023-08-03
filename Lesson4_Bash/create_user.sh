#!/bin/bash

#argument checking
if [ $# -ne 4 ]; then
    echo "Invalid number of arguments!"
    exit 1
fi

#Assignment of arguments
user_name=$1
home_folder=$2
ssh_access=$3
enable=$4

#creating user and user folder
echo "Creating user: $user_name"
sudo useradd -m -d $home_folder $user_name

#Creating password
sudo passwd $user_name

#Setting up ssh access
if [ $ssh_access == "yes" ]; then
    echo "Enabling user ssh access: $user_name"
    sudo usermod -aG ssh $user_name
fi

#Enable or disable an account

if [ $enable == "yes" ]; then
    echo "Enable account: $user_name"
    sudo usermod -e "" $user_name
else
    echo "Disable account: $user_name"
    sudo usermod -e 1 $user_name
fi

echo "User $user_name has been created!"
