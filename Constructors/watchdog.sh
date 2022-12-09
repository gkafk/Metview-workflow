#!/bin/bash

# #--------------------------------------------------------------------------------------------
#  Ensure that only one instance of the script is running
# #--------------------------------------------------------------------------------------------

pidof -o %PPID -x $0 >/dev/null && echo "$(date  +'%Y-%m-%d %H:%M:%S') - NOTE: Script $0 already running." && exit 1

# #--------------------------------------------------------------------------------------------


# #--------------------------------------------------------------------------------------------
# #  FILES AND FOLNDERS paths
# #--------------------------------------------------------------------------------------------

# import global_variables
source $(dirname $0)/global_variables.cfg

# folders--------------------------------------------------------------------------------------

DATA_FOLDER=${_DATA_FOLDER/%$'\r'/}
INPUT_FOLDER=${_INPUT_FOLDER/%$'\r'/}
INPUT_DB_FOLDER=${_INPUT_DB_FOLDER/%$'\r'/}
LOGS_FOLDER=${_LOGS_FOLDER/%$'\r'/}
SCRIPTS_FOLDER=${_SCRIPTS_FOLDER/%$'\r'/}
CONDA_SH=${_CONDA_SH/%$'\r'/}
CONDA_ENV_NAME=${_CONDA_ENV_NAME/%$'\r'/}

# scripts paths---------------------------------------------------------------------------------
merge_script=$SCRIPTS_FOLDER/merge_gribs.sh
# send_to_server_script=$SCRIPTS_FOLDER/send_to_server.sh


# watcher logs file
# create log file if not exists
touch $LOGS_FOLDER/processes.log || exit
processes=$LOGS_FOLDER/processes.log

# Number of files sending ECMWF
EXPECT_FILES=$_EXPECT_FILES

DATE=$(date +"%Y%m%d")

TIME=$(date +"%H%M")
HOUR=$(date +"%H")

# #********************************************************************************************
# It is madatory to activate conda fisrt, for using eccodes tools in metview environment
# #********************************************************************************************

eval "$(conda shell.bash hook)"
# source ~/miniconda3/etc/profile.d/conda.sh
source $CONDA_SH
conda activate $CONDA_ENV_NAME


# Write output to log file
exec >> $LOGS_FOLDER/watchdog.log 2>&1

#********************************************************************************************
# Funtion that returns the line of day and run wanted as variables from processes.log.
#********************************************************************************************
function find_in_log(){
  if [ -f "$processes" ]
  then
    while read -r logDateFolder logRunFolder logTime logFilesNum logStart logMerge logFctPro logMetgram logRoute logEnd
    do
      if [ "$1" -eq "$logDateFolder" ] && [ "$2" -eq "$logRunFolder" ]
      then
        echo "$logDateFolder $logRunFolder $logTime $logFilesNum $logStart $logMerge $logFctPro $logMetgram $logRoute $logEnd"
        break
      # else
      #   echo "$1 not in line"
      fi
    done < $processes
  else
    echo "$(date  +"%Y-%m-%d %H:%M:%S") - file not found"
    touch $processes
  fi
}

# Checking INPUT_DB_FOLDER for files number
# if the number of files in the sub_folder is equal to the number of files sending ECMWF
# then check if the log files contains date and run (folder and sub-folder)

echo "$(date  +'%Y-%m-%d %H:%M:%S') - Checking for folders not in processes"

for folder in `ls $INPUT_DB_FOLDER`
do
  for sub_f in `ls $INPUT_DB_FOLDER$folder`
  do
    echo -n "$(date  +'%Y-%m-%d %H:%M:%S') - checking $folder $sub_f"
    if ! grep -Fq "$folder $sub_f" $processes;then
      echo -e "\n$(date  +'%Y-%m-%d %H:%M:%S') - $folder $sub_f not in log."
      WORKING_FOLDER="$INPUT_DB_FOLDER$folder"
      WORKING_FOLDER_NAME="$folder"
      break
    else
      WORKING_FOLDER=$INPUT_DB_FOLDER$DATE
      WORKING_FOLDER_NAME="$DATE"
      echo '. Ok is in log'
    fi
  done
done

if [ -d "$WORKING_FOLDER" ]; then
  # echo "$(date  +'%Y-%m-%d %H:%M:%S') - Folder $WORKING_FOLDER found..."
  cd $WORKING_FOLDER
else
  ###  if $OUTPUT_FOLDER  does NOT exists, sleep in rest ###
  # echo "$(date  +'%Y-%m-%d %H:%M:%S') - Folder ${WORKING_FOLDER} not found."
  exit 0
fi

if [[ `ls` ]]; then
  for sub_folder in `ls`
  do
    # echo "`ls $sub_folder | wc -l` files in sub folder $sub_folder"
    # Number of files in run time folder
    filesNum=`ls $sub_folder | wc -l`
    # if the number of files is the expected, the procedure begins
    if [ $filesNum -eq $EXPECT_FILES ];then
      echo "$(date  +'%Y-%m-%d %H:%M:%S') - folder $WORKING_FOLDER got $filesNum files"
      #  If date and run time folder exists in $processes, begins the production
      if ! grep -Fq "$WORKING_FOLDER_NAME $sub_folder" $processes;then
        echo "$(date  +'%Y-%m-%d %H:%M:%S') -  $WORKING_FOLDER_NAME $sub_folder Starting process"
        # Write in $processes the strating of process
        echo "$WORKING_FOLDER_NAME $sub_folder $TIME $filesNum started-proc" >> $processes

        #********************************************************************************************
        # Cleaning and merging grib files in output folder. All frames must be merged to one grib file
        # for better munipulation inside metview software
        #********************************************************************************************

        # Executing merge_script with day and run time arguments
        if [ "$_MERGE_FILES" == "YES" ];then
          bash $merge_script $WORKING_FOLDER_NAME $sub_folder
          # Write in $processes the ending of merging process
          sed -i '$ s/$/ merged-gribs/' $processes
          echo "-------------- end of merging --------------"
        else
          echo  "******* Merging was not configured to be executed ***********"
          sed -i '$ s/$/ merged-escaped/' $processes
        fi

        #********************************************************************************************
        # Producing png images
        #********************************************************************************************
        if [ "$_CREATE_FORECAST_IMAGES" == "YES" ];then
          cd "$_PYTHONICS_FOLDER"
          # Executing plot_images.py with 2 arguments: day folder and run folder for forecasting maps production
          python3 plot_images.py $WORKING_FOLDER_NAME $sub_folder
          # Write in  $processes the end of forecasting maps production
          sed -i '$ s/$/ plotted-fcst/' $processes
          echo "-------------- end of forecasting maps production  --------------"
        else
          echo  "******* forecasting maps production were not configured to be executed ***********"
          sed -i '$ s/$/ fcst-escaped/' $processes
        fi

        if [ "$_CREATE_METEOGRAMS" == "YES" ];then
          cd "$_PYTHONICS_FOLDER"
          # Executing metgram.py with 2 arguments: day folder and run folder for meteograms production
          python3 metgram.py $WORKING_FOLDER_NAME $sub_folder &
          # Write in  $processes the end of meteograms production
          sed -i '$ s/$/ metgram-ended/' $processes
          echo "-------------- end of meteograms production  --------------"
        else
          echo  "******* meteograms production were not configured to be executed ***********"
          sed -i '$ s/$/ metgram-escaped/' $processes
        fi

        if [ "$_CREATE_ROUTE_WEATHER_MAPS" == "YES" ];then
          cd "$_PYTHONICS_FOLDER"
          # Executing route_weather.py with 2 arguments: day folder and run folder for route weather production
          python3 route_weather.py $WORKING_FOLDER_NAME $sub_folder &
          # Write in  $processes the end of route weather production
          sed -i '$ s/$/ routew-ended/' $processes
          echo "-------------- end of route weather maps production --------------"
        else
          echo  "******* route weather maps were not configured to be executed ***********"
          sed -i '$ s/$/ routew-escaped/' $processes
        fi

        wait

        #********************************************************************************************
        # send to another server
        #********************************************************************************************
        if [ "$_SEND_IMAGES" == "YES" ];then
          bash $send_to_server_script >> $LOGS_FOLDER/send_to_server.log
        fi

        echo "$(date  +'%Y-%m-%d %H:%M:%S') - End of production process"
        sed -i '$ s/$/ ended-proc/' $processes
      else
        # Check if end of production chain is in $processes
        echo "$(date  +'%Y-%m-%d %H:%M:%S') - $WORKING_FOLDER_NAME $sub_folder is in log. Nothing to do"
        read -r day run num tim start merge fct metgram routw end rest<<< $(find_in_log $WORKING_FOLDER_NAME $sub_folder)
        if [ "$end" == "ended-proc" ]
        then
          echo "$(date  +'%Y-%m-%d %H:%M:%S') - $day $run $num Process has ended right"
        else
          # If log line does not contain  "ended-proc" in index 10, then the process begins again.
          echo "$(date  +'%Y-%m-%d %H:%M:%S') - $day $run $num Process has ended with probmlem"
          echo "$(date  +'%Y-%m-%d %H:%M:%S') - Starting producing forecast images, meteograms and route weather maps again"
          echo "End word: $end"
          cd "$_PYTHONICS_FOLDER"
          python3 plot_images.py $WORKING_FOLDER_NAME $sub_folder
          python3 metgram.py $WORKING_FOLDER_NAME $sub_folder
          python3 route_weather.py $WORKING_FOLDER_NAME $sub_folder

          # assign the line of log file to variable line
          line=`grep "$WORKING_FOLDER_NAME $sub_folder" $processes`
          # Deletes the line that contains variable date folder and run subfolder
          sed -i "/$WORKING_FOLDER_NAME $sub_folder/d" $processes
          # print untill merged-gribs
          echo "`cut -d " " -f 1-6 <<< "$line"` plotted-fcst metgram-ended routew-ended ended-proc run again at $TIME"  >> $processes

        fi
      fi
    else
      # input_db folder has not got the required number of files yet.
      echo "$(date  +'%Y-%m-%d %H:%M:%S') - Folder $WORKING_FOLDER_NAME/$sub_folder has less files than expected - $filesNum files."
    fi

  done
fi



#********************************************************************************************
# limiting log file size by using only last X lines
#********************************************************************************************

# create log file if not exists
touch $LOGS_FOLDER/watchdog.log || exit
echo "$(tail -10000 $LOGS_FOLDER/watchdog.log)" > $LOGS_FOLDER/watchdog.log

# create log file if not exists
touch $LOGS_FOLDER/processes.log || exit
echo "$(tail -1000 $LOGS_FOLDER/processes.log)" > $LOGS_FOLDER/processes.log
