#!/bin/bash

#cd to the script folder and run as: sh matlab_postinstall.sh
#read -p "Path of libmwlmgrimpl.so (e.g. /home/user/test/libmwlmgrimpl.so): " libfilepath
#read -p "MATLAB folder (e.g. /home/user/MATLAB/R2024a): " matfilepath
#libfilepath=$(pwd)/libmwlmgrimpl.so
matfilepath=/usr/local/MATLAB/R2024a
matuserpath=$HOME/Documents/MATLAB
startup_file=$(pwd)/startup.m

#to check if a file exist
#[ -e "$(pwd)/libmwlmgrimpl.so" ] && echo "File found. Continuing..." || echo "File not found...'"
#copy the file in the installation folder
#sudo cp $libfilepath $matfilepath/bin/glnxa64/matlab_startup_plugins/lmgrimpl/

#download from Google Drive the file and put in the installation folder
#use the sudo -E to avoid PROXY ERRORS when doing wget
sudo -E wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1GMNAkEmuB17Y5MGqrE4OUjJfIEjeSBqK' -O $matfilepath/bin/glnxa64/matlab_startup_plugins/lmgrimpl/libmwlmgrimpl.so

#install the matlab-support package and git too
sudo -E apt -qq --yes install matlab-support git

#copy the startup file in the matlab user folder
cp $startup_file $matuserpath/

#add the nfs mount to the fstab
sudo -E sh NFSmount.sh

#update the the hosts file
sudo -E sh hostsRedirect.sh

#end of the script
echo "Operation completed!"
#echo $matuserpath
