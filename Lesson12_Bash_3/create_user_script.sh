#!/bin/bash

Help()
{
   echo "---------Welcome to help section------------"
   echo "This script is used for user creation"
   echo "{user_name} - use this parameter to create new user name"
   echo "{home_folder} - use this parameter to create new home folder for user. Please, use construction /home/{user_name}"
   echo "{ssh_access} - write ""yes"" if you want to edd ssh access to new user"
   echo "{enable} - write ""yes"" if you want to enable new user"
   echo "--------------Extra options-----------------"
   echo "{h} - use ""-h"" to open help section"
   echo "{i} - use ""-i"" to display parameters"
   echo "{v} - use ""-v"" to display example"
}

Get_param()
{
   echo "---------Welcome to parameter section----------"
   echo "{user_name} - first parameter. Write user name."
   echo "{home_folder} - second parameter. Write /home/{user_name}"
   echo "{ssh_access} - third parameter. Write ""yes"" if user needs ssh access"
   echo "{enable} - fourth parameter. Write ""yes"" if you need enable user"
}

Get_example()
{
   echo "---------Welcome to example section----------"
   echo "To create new user look at this example: ./create_user_with_function {user_name} {home_folder} {ssh_access} {enable}"
}

#getopts function usage code snippet
while getopts ":hiv" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      i) # display Parameters
         Get_param
         exit;;
      v) # display Example
         Get_example
         exit;;
   esac
done

#argument checking
#if [ $# -ne 4 ]; then
#    echo "Invalid number of arguments!"
#    exit 1
#fi

#Assignment of arguments
user_name=$1
home_folder=$2
ssh_access=$3
enable=$4


#creating user and user folder
sudo useradd $user_name
echo "$user_name has been created"
if [ -z $home_folder ]
then
   sudo mkdir /home/$user_name
   echo "Home directory /home/$user_name has been created"
else 
   sudo mkdir $home_folder
   echo "Home directory $home_folder has been created"
fi

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

echo "------------------------------------"
echo "User $user_name has been created!"

#Create user group
echo "Enter user group name:"
read group_name

sudo groupadd "$group_name"
sudo usermod -aG "$group_name" "$user_name"

echo "Group - $group_name was created and user - $user_name was added to $group_name"
