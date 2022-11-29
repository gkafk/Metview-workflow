#!/bin/sh
# In order to empty trash

echo `date`


# import global_variables
source $(dirname $0)/global_variables.cfg

# folders--------------------------------------------------------------------------------------


LOGS_FOLDER=$_LOGS_FOLDER

TRASH=$_TRASH
DaysOlderThan="+1"

# cd $TRASH


echo "Files to delete:"
gio list $TRASH

#  centos 8, ubuntu 20LTS
gio trash --empty #does not work in all distro

#  centos 7
# if [ -d "$TRASH" ]; then
#   # find "$TRASH" -maxdepth 1 -name "20*" -type d -mtime "$DaysOlderThan" -ls
#   find "$TRASH" -maxdepth 1 -name "20*" -type d -mtime "$DaysOlderThan" -exec rm -rf {} \;
# else
#   echo "Error: $TRASH not found"
#   exit 1
# fi

echo "Files after deleting:"
gio list $TRASH

#********************************************************************************************
# limiting log file size by using only last 10000 lines
#********************************************************************************************

# create log file if not exists
touch $LOGS_FOLDER/empty_trash.log || exit
# use only last 10000 lines, to keep small log file
echo "$(tail -1000 $LOGS_FOLDER/empty_trash.log)" > $LOGS_FOLDER/empty_trash.log
