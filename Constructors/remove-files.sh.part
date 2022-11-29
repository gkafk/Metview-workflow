#!/bin/sh
# In order to remove files from the input_db folder and output folder

echo `date`


# #--------------------------------------------------------------------------------------------
# #  FILES AND FOLNDERS paths
# #--------------------------------------------------------------------------------------------


# import global_variables
source $(dirname $0)/global_variables.cfg

# folders--------------------------------------------------------------------------------------

DATA_FOLDER=$_DATA_FOLDER
INPUT_FOLDER=$_INPUT_FOLDER
INPUT_DB_FOLDER=$_INPUT_DB_FOLDER
OUTPUT_FOLDER=$_OUTPUT_FOLDER
LOGS_FOLDER=$_LOGS_FOLDER

# Write output to log file
exec >> $LOGS_FOLDER/remove-files.log 2>&1

DaysOlderThan="+5"

if [ -d "$INPUT_DB_FOLDER" ]; then
  find "$INPUT_DB_FOLDER" -name "*" -type d -mtime "$DaysOlderThan" -ls
  find "$INPUT_DB_FOLDER" -name "*" -type d -mtime "$DaysOlderThan" -exec rm -rf {} \;
else
  echo "Error: $INPUT_DB_FOLDER not found"
  exit 1
fi

DaysOlderThan="+5"

if [ -d "$OUTPUT_FOLDER" ]; then
  find "$OUTPUT_FOLDER" -name "*" -type d -mtime "$DaysOlderThan" -ls
  find "$OUTPUT_FOLDER" -name "*" -type d -mtime "$DaysOlderThan" -exec rm -rf {} \;
else
  echo "Error: $OUTPUT_FOLDER not found"
  exit 1
fi

#********************************************************************************************
# limiting log file size by using only last 1000 lines
#********************************************************************************************

# create log file if not exists
touch $LOGS_FOLDER/remove-files.log || exit
# use only last 1000 lines, to keep small log file
echo "$(tail -1000 $LOGS_FOLDER/remove-files.log)" > $LOGS_FOLDER/remove-files.log

