#!/bin/bash

yesOrNo="y"

letter_writer() {
  echo -e "Dear "$1",\n\nWelcome to Initech Corporation! Were so happy to have you in the "$2 "Department as a" $3. "Please don't forget to complete your TPS Reports in a timely manner.\n\nSincerly,\n\nBill Lumbergh" > welcome.txt
}

file_system_writer() {
 mkdir /home/$1/Desktop
 mkdir /home/$1/Documents
 mkdir /home/$1/Downloads
 mkdir /home/$1/Pictures

 cp /home/student/Downloads/welcome.txt /home/$1/Documents
 cp /home/student/Downloads/ackbar.png /home/$1/Pictures
 
 chmod 444 /home/student/Downloads/welcome.txt /home/$1/Documents/welcome.txt
 chmod 644 /home/student/Downloads/welcome.txt /home/$1/Pictures/ackbar.png

 chown -R $1 /home/$1
 chgrp -R $1 /home/$1
}

# permission_editor() {
# }

while [ "$yesOrNo" = "y" ]
do
  read -p "Username: " username
  read -p "Full Name: " fullName
  read -p "Department: " deptName
  read -p "Job Title: " jobTitle
  useradd $username
  nameArray=($fullName)
  firstName=${nameArray[0]}
  letter_writer "$firstName" "$deptName" "$jobTitle"
  file_system_writer $username
  echo "Would you like to add another user (y/n): "
  read yesOrNo
done

