#!/bin/bash


# #--------------------------------------------------------------------------------------------
# #  FILES AND FOLNDERS paths
# #--------------------------------------------------------------------------------------------

echo "starting merging script"

echo "folder: $PWD "
echo "$(dirname $0)"
echo "folder: $PWD "

# import global_variables
source $(dirname $0)/global_variables.cfg


# folders--------------------------------------------------------------------------------------

DATA_FOLDER=$_DATA_FOLDER
INPUT_FOLDER=$_INPUT_FOLDER
INPUT_DB_FOLDER=$_INPUT_DB_FOLDER
OUTPUT_FOLDER=$_OUTPUT_FOLDER
LOGS_FOLDER=$_LOGS_FOLDER


#********************************************************************************************
#  It is madatory to activate conda fisrt, for using eccodes tools in metview environment
#********************************************************************************************

eval "$(conda shell.bash hook)"
# source /home/metview/miniconda3/etc/profile.d/conda.sh
source "$_CONDA_SH"
conda activate $_CONDA_ENV_NAME

#--------------------------------------------------------------------------------------------


DATETIME=$(date +"%Y%m%d%H")


#*******************************************************************************************************
# catch arguments
#*******************************************************************************************************

RUN_FOLDER=$1
TIME_FOLDER=$2


start=`date +%s`
EXPORTING_FOLDER=$OUTPUT_FOLDER/$RUN_FOLDER/$TIME_FOLDER
echo "$(date  +'%Y-%m-%d %H:%M:%S') - Output folder: $EXPORTING_FOLDER"

# Για τέστ
# EXPORTING_FOLDER=$OUTPUT_FOLDER//20220121/0000"

#*******************************************************************************************************
#  Merging grib files function
#*******************************************************************************************************

function merge_grib_files(){
  for sub in `ls $1` #περιμένει είσοδο $1 όνομα φακέλου
  do
      #echo $sub
      cd $1/$sub
      grib_files=$(ls -v) #-v για να ταξινομήσει αριθμητικά
      # echo $grib_files
      grib_copy $grib_files [shortName]_[level].grib
      # remove splitted grib files after merging the new one inside directory
      rm -f $grib_files
      cd ../../
  done
}

#*******************************************************************************************************
# Function for removing grib files that their data values number is lower than 100.000 values
#*******************************************************************************************************

function remove_small_grib_files(){
  for sub in `ls $1` # expecting input $1 file name
  do
      #echo $sub
      cd $1/$sub
      grib_files=$(ls -v) #-v for sorting by number
      # echo $grib_files
      for file in $grib_files
      do
        # codes_split_file -v -1 $file
        # rm -f $file
        grib_values=`grib_get -p numberOfDataPoints $file`
        if [[ $grib_values -lt 100000 ]]
        then
          echo "$grib_values less than 100000 values in file $file - $grib_values"
          # remove splitted grib files after merging the new one inside directory
          rm -f $file
        fi
      done
      cd ../../
  done
}


#*******************************************************************************************************
# Function for splitting files in directory, in case they have been merged
#*******************************************************************************************************

function split_grib_files(){
  for sub in `ls $1` #περιμένει είσοδο $1 όνομα φακέλου
  do
      #echo $sub
      cd $1/$sub
      grib_files=$(ls -v) #-v για να ταξινομήσει αριθμητικά
      # echo $grib_files
      for file in $grib_files
      do
        # print the count of messages and files created
        # codes_split_file -v -1 $file
        # do not print the count of messages and files created
        codes_split_file -1 $file
        rm -f $file
      done
      cd ../../
  done
}


#=======================================================================================================
#///////////////////////////////////////////////////////////////////////////////////////////////////////
# Merging Process
#//////////////////////////////////////////////////////////////////////////////////////////////////////
#=======================================================================================================


#********************************************************************************************
#   merge extracted grib files with the same parameter inside directory
#********************************************************************************************

if [ -d "$EXPORTING_FOLDER" ]; then
  echo "Folder $EXPORTING_FOLDER found..."
  cd $EXPORTING_FOLDER
  #*********   use IFS for split with new line
  IFS=$'\n'
  for folder in `ls`
  do
      echo "$(date  +'%Y-%m-%d %H:%M:%S') - merge items in folder:  $folder"
      split_grib_files $folder
      remove_small_grib_files $folder
      merge_grib_files $folder &
  done
  wait
else
  ###  if $EXPORTING_FOLDER  does NOT exists ###
  echo "$(date  +'%Y-%m-%d %H:%M:%S') - Error: folder ${EXPORTING_FOLDER} not found. Can not continue."
  exit 0
fi


end=`date +%s`
runtime=$((end-start))
echo "$(date  +'%Y-%m-%d %H:%M:%S') - Merging gribs endend in '$runtime'."
