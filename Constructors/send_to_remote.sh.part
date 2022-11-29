#!/bin/bash
# Executed by watchdog.sh
# Sends the images to remote pc via ftp protocol
# Variables used from global_variables.cfg

#--------------------------------------------------------------------------------------------
#  FILES AND FOLNDERS paths
#--------------------------------------------------------------------------------------------

# import global_variables
source $(dirname $0)/global_variables.cfg

# folders--------------------------------------------------------------------------------------

DATA_FOLDER=$_DATA_FOLDER
INPUT_FOLDER=$_INPUT_FOLDER
INPUT_DB_FOLDER=$_INPUT_DB_FOLDER
LOGS_FOLDER=$_LOGS_FOLDER
SCRIPTS_FOLDER=$_SCRIPTS_FOLDER
IMAGES_FOLDER=$_EXPORT_IMAGES_FOLDER
REMOTE_PATH=$_REMOTE_PATH

# Write output to log file
exec >> $LOGS_FOLDER/send_to_remote.log 2>&1

# remote credentials
HOST=$_REMOTE_IP
USER=$_USER
PASSWORD=$_PASSWORD

DATETIME=$(date +"%d-%m-%y %H:%M")

cd $IMAGES_FOLDER

#*********   use IFS for split with new line
IFS=$'\n'

# Function for ftp.
# Waits for 2 arguments folder and subfolder.
# Sends the image files of the subfolder to the folder of ther remote pc
# permissions for the remote path mast be given

function send_ftp(){
	FTP_FOLDER=$1
	FTP_SUB=$2
	LOC=$FTP_FOLDER"/"$FTP_SUB"/"
	ftp -inv $HOST << EOF
	quote USER $USER
	quote PASS $PASSWORD
	cd $REMOTE_PATH
	mkdir $FTP_FOLDER
	mkdir $LOC
	cd $LOC
	binary
	lcd $IMAGES_FOLDER$LOC
	mput *
	pwd
	bye
EOF
}


# echo `ls`
# If there are directories in the path of IMAGES_FOLDER
if [[ `ls` ]]; then
	for folder in `ls -1 $IMAGES_FOLDER` #get the list of files
	do
	   echo "$(date  +'%Y-%m-%d %H:%M:%S') -   $folder"
	   if [[ $folder ]]; then
			echo "$DATETIME................... φάκελος: " $folder
			# cd $IMAGES_FOLDER
			cd $IMAGES_FOLDER$folder
			echo `ls`
			for subfolder in `ls`
			do
				# if subfolder is image file png
				if [[ $subfolder = *.png ]]; then
					send_ftp $folder " "
				# if subfolder is directory
				else
					send_ftp $folder $subfolder
				fi
			done
	   fi
	done
fi

#********************************************************************************************
# limiting log file size by using only last 10000 lines
#********************************************************************************************

# create log file if not exists
touch $LOGS_FOLDER/send_to_remote.log || exit
# use only last 10000 lines, to keep small log file
echo "$(tail -10000 $LOGS_FOLDER/send_to_remote.log)" > $LOGS_FOLDER/send_to_remote.log
