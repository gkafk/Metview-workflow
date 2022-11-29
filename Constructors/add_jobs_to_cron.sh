#!/bin/sh

# import global_variables
source $(dirname $0)/global_variables.cfg

# TODO
# if folders copy _SCRIPTS

DATA_FOLDER=$_DATA_FOLDER
INPUT_FOLDER=$_INPUT_FOLDER
INPUT_DB_FOLDER=$_INPUT_DB_FOLDER
OUTPUT_FOLDER=$_OUTPUT_FOLDER
LOGS_FOLDER=$_LOGS_FOLDER
SCRIPTS_FOLDER=$_SCRIPTS_FOLDER
PYTHONICS_FOLDER=$_PYTHONICS_FOLDER
EXPORT_IMAGES_FOLDER=$_EXPORT_IMAGES_FOLDER

# Create directories if not exist
mkdir -p $DATA_FOLDER
mkdir -p $INPUT_FOLDER
mkdir -p $INPUT_DB_FOLDER
mkdir -p $OUTPUT_FOLDER
mkdir -p $LOGS_FOLDER
mkdir -p $SCRIPTS_FOLDER
mkdir -p $PYTHONICS_FOLDER
mkdir -p $EXPORT_IMAGES_FOLDER
cd ../
cp Constructors/* $SCRIPTS_FOLDER
cp Pythonics/* $PYTHONICS_FOLDER

# sudo crontab -l > cron_bkp
# sudo echo "*/5 * * * * $SCRIPTS_FOLDER/split_gribls.sh >/dev/null 2>&1" >> cron_bkp
# sudo echo "*/5 * * * * $SCRIPTS_FOLDER/watchdog.sh >/dev/null 2>&1" >> cron_bkp
# sudo echo "00 00 * * * $SCRIPTS_FOLDER/remove-files.sh  >/dev/null 2>&1" >> cron_bkp
# sudo echo "00 05 */2 * * $SCRIPTS_FOLDER/empty_trash.sh >/dev/null 2>&1" >> cron_bkp
# sudo crontab cron_bkp
# sudo rm cron_bkp

# Add jobs to crontab
cron_line="*/5 * * * * $SCRIPTS_FOLDER/split_gribls.sh >/dev/null 2>&1"
cronjob=`crontab -l | grep "$cron_line"`
if [[ -z $cronjob ]]
    then
    crontab -l > cron_bkp
    echo -e "\n$cron_line" >> cron_bkp
    crontab cron_bkp
    rm cron_bkp
fi

cron_line="*/5 * * * * $SCRIPTS_FOLDER/watchdog.sh >/dev/null 2>&1"
cronjob=`crontab -l | grep "$cron_line"`
if [[ -z $cronjob ]]
    then
    crontab -l > cron_bkp
    echo -e "\n$cron_line" >> cron_bkp
    crontab cron_bkp
    rm cron_bkp
fi

cron_line="00 00 * * * $SCRIPTS_FOLDER/remove-files.sh  >/dev/null 2>&1"
cronjob=`crontab -l | grep "$cron_line"`
if [[ -z $cronjob ]]
    then
    crontab -l > cron_bkp
    echo -e "\n$cron_line" >> cron_bkp
    crontab cron_bkp
    rm cron_bkp
fi

cron_line="00 05 */2 * * $SCRIPTS_FOLDER/empty_trash.sh >/dev/null 2>&1"
cronjob=`crontab -l | grep "$cron_line"`
if [[ -z $cronjob ]]
    then
    crontab -l > cron_bkp
    echo -e "\n$cron_line" >> cron_bkp
    crontab cron_bkp
    rm cron_bkp
fi


