# Metview-workflow:
## It is a bunch of scripts for producing weather forecasting images using ECMWF grib files.
## Uses ECMWF Metview for automated weather forecasting images production or grib files viewing. Receives ECMWF grib files in the directory ECMWF. Reconstructs downloaded grib files of one step grib containing all variables in grib files of the same variable merged to one grib file with all steps inside the directory output and subdirectories according to variable name and lower subdirectories of the levels of the product.

- Requirements

    1. Mini conda installed.
    https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
    Miniconda installer for Linux:
        https://docs.conda.io/en/latest/miniconda.html#linux-installers
    cd to downloaded file Miniconda3-latest-Linux-x86_64.sh
    In your terminal window, run:
        bash Miniconda3-latest-Linux-x86_64.sh

    2. Metview installed:
        https://metview.readthedocs.io/en/latest/install.html


    3. The metview-python package installed.
        https://github.com/ecmwf/metview-python

        From PyPI with:
        $ pip install metview

        or from conda-forge with:
        $ conda install metview-python -c conda-forge



- Install

    cd to downloaded files directory    
    cd Constructors
    Configure global_variables.cfg file according to your pc configuration.    
    $./add_jobs_to_cron.sh to start the installation.



- Usage

    - Constructors directory:
        Contains bash scripts for manipulating grib files, using ECMWF eccodes binaries, installed with metview.
        - split_gribs.sh script splits grib files in a directory according to the model run date and subdirectory according to grib variables
        - merge_gribs.sh script merges splitted grib files in one large for every variable directory.
    - Pythonics directory:
        Contains python scripts for producing forecasting maps, using ECMWF metview and metview-python interface.
        - panel.py script opens a graphical environment for choosing and viewing grib products in metview plot environment.
        - plot_images.py script exports forecasting images to images directory.

    1. Configure global_variables.cfg file according to your pc configuration.
    2. Configure globalVariables.py for desired images production.
    3. Direct incoming grib files from ECMWF to incoming directory ECMWF.
    4. Crontab will execute the required scripts.
