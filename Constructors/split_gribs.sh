#!/bin/bash

# Bash script used for splitting incoming grib files from ECMWF.
# It uses eccodes tools for splitting grib files to frames

# #--------------------------------------------------------------------------------------------
#  Ensure that only one instance of the script is running
# #--------------------------------------------------------------------------------------------

# pidof -o %PPID -x $0 >/dev/null && echo "$(date  +'%Y-%m-%d %H:%M:%S') - NOTE: Script $0 already running." && exit 1

if pgrep -x "grib_copy"
then
  echo "$(date  +'%Y-%m-%d %H:%M:%S')  - NOTE: Script already running..."
  exit 0
fi


# #--------------------------------------------------------------------------------------------
# #  FILES AND FOLNDERS paths
# #--------------------------------------------------------------------------------------------


# import global_variables
source $(dirname $0)/global_variables.cfg

# folders--------------------------------------------------------------------------------------

DATA_FOLDER=${_DATA_FOLDER/%$'\r'/}
INPUT_FOLDER=${_INPUT_FOLDER/%$'\r'/}
INPUT_DB_FOLDER=${_INPUT_DB_FOLDER/%$'\r'/}
OUTPUT_FOLDER=${_OUTPUT_FOLDER/%$'\r'/}
LOGS_FOLDER=${_LOGS_FOLDER/%$'\r'/}
CONDA_SH=${_CONDA_SH/%$'\r'/}
CONDA_ENV_NAME=${_CONDA_ENV_NAME/%$'\r'/}
echo $(dirname $0)
echo $DATA_FOLDER
echo $CONDA_SH
echo $CONDA_ENV_NAME
# exit 0
#********************************************************************************************
#  It is madatory to activate conda fisrt, for using eccodes tools in metview environment
#********************************************************************************************

eval "$(conda shell.bash hook)"
# source /home/metview/miniconda3/etc/profile.d/conda.sh
source $CONDA_SH
conda activate $CONDA_ENV_NAME
echo `conda info --envs`

#--------------------------------------------------------------------------------------------
# ECMWF_DAY_FOLDER=$(date +"%Y%m%d")

DATETIME=$(date +"%Y%m%d%H")

# Write output to log file
exec >> $LOGS_FOLDER/split_gribs.log 2>&1

#*******************************************************************************************************
# Get date and run from the grib file. They will be used in construncting coresponding folders in
# EXPORTING_FOLDER,
#*******************************************************************************************************

cd $INPUT_FOLDER
# Find the first file in  INPUT_FOLDER.
if [[ `ls` ]]; then
  first_file=`ls -1 | head -n1`
  echo "$(date  +'%Y-%m-%d %H:%M:%S')  - first file: $first_file"
  # get time and run time from file, using eccodes.
  GRIB_DATE=$(grib_get -w count=1 -p dataDate $first_file)
  GRIB_TIME=$(grib_get -w count=1 -p dataTime $first_file)
  # add some zeros in the folder name.
  GRIB_TIME=`printf "%04d" $GRIB_TIME`
  # Create EXPORTING_FOLDER where grib frame will be extracted.
  EXPORTING_FOLDER=$OUTPUT_FOLDER/$GRIB_DATE/$GRIB_TIME
  mkdir -p "$EXPORTING_FOLDER/"
fi


#*******************************************************************************************************
# Function for creating folders according to grid frames names and splitting gribs in subfolders
# to individual grib frames
#*******************************************************************************************************

function make_products_from_grib(){
  #******** get the names of selected grib file ********************************
  VARIABLE_NAMES=$(grib_get -p name $1)  # expects input $1 grib file name
  #echo "variable names:$VARIABLE_NAMES"
  GRIB_DATE=$(grib_get -w count=1 -p dataDate $filename)
  GRIB_TIME=$(grib_get -w count=1 -p dataTime $filename)
  GRIB_TIME=`printf "%04d" $GRIB_TIME` # add some zeros in the folder name.
  OUTPUT_1_FOLDER=$DATA_FOLDER/"output/"$GRIB_DATE/$GRIB_TIME

  #******** create directories from grib dataNames *****************************
  for dire in $VARIABLE_NAMES;
  do
      shopt -s extglob
      dir=${dire%%+([[:space:]])}
      NAME=$dir
      # get levels from grib file
      VARIABLE_LEVELS=$(grib_get -w name="$NAME" -p level $filename)
      #echo "variable levels:$VARIABLE_LEVELS"
      # Case of 2nd grib files package with same variable names.
      # If file name starts with something else like L2S*** then add L2_ or whatever in front of file name.
      if [[ $filename == L2S* ]];
      then
        dir="L2_$dir"
      fi


      mkdir -p "$OUTPUT_1_FOLDER/$dir";

      #******* create sub-directories for levels **********************************
      for level in $VARIABLE_LEVELS;
      do
          # echo $level
          mkdir -p "$OUTPUT_1_FOLDER/$dir/${level%%+([[:space:]])}";
      done

      grib_copy -w name="$NAME" $filename "$OUTPUT_1_FOLDER/$dir/[level]/[shortName]_[level]_[dataDate]_[dataTime]_[startStep].grib"

  done
  # moving file in input_db
  move_grib_to_db $filename
}


#*******************************************************************************************************
# Function for moving incoming grib files from input file to INPUT_DB_FOLDER for saving
#*******************************************************************************************************

function move_grib_to_db(){
  FILENAME=$1
  GRIB_DATE=$(grib_get -w count=1 -p dataDate $FILENAME)
  GRIB_TIME=$(grib_get -w count=1 -p dataTime $FILENAME)
  GRIB_TIME=`printf "%04d" $GRIB_TIME` # add some zeros in the folder name.
  echo "$(date  +'%Y-%m-%d %H:%M:%S')  - moving $FILENAME to input DB folder: $INPUT_DB_FOLDER/$GRIB_DATE/$GRIB_TIME"
  # Creating folders if not existing
  mkdir -p "$INPUT_DB_FOLDER/$GRIB_DATE/$GRIB_TIME"
  mv $FILENAME "$INPUT_DB_FOLDER/$GRIB_DATE/$GRIB_TIME" &
}


#=======================================================================================================
#///////////////////////////////////////////////////////////////////////////////////////////////////////
# Starting procedure
#//////////////////////////////////////////////////////////////////////////////////////////////////////
#=======================================================================================================


cd $INPUT_FOLDER

#*********   use IFS for split with new line
IFS=$'\n'


while  [ `ls -l | wc -l` -gt 1 ]
do
  echo "$(date  +'%Y-%m-%d %H:%M:%S')  - files in folder:" `ls -l | wc -l` #`ls -al`
  # get only first 12 files for procedure for saving resources in threads
  for filename in `ls -U | head -12`
  do
      echo "$(date  +'%Y-%m-%d %H:%M:%S')  - $filename"
      make_products_from_grib $filename &
  done
  wait
done



#********************************************************************************************
# limiting log file size by using only last 5000 lines
#********************************************************************************************

# create log file if not exists
touch $LOGS_FOLDER/split_gribs.log || exit
echo "$(tail -5000 $LOGS_FOLDER/split_gribs.log)" > $LOGS_FOLDER/split_gribs.log
