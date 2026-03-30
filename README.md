# JWST Image Gallery Organizer
This project is a basic astronomy catalog that uses relatively recent JWST data from the MAST Archive to display images and metadata of a variety of popular DSOs, such as the Eagle Nebula (M16) and the Pinwheel Galaxy (M101). 


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
The purpose of this project was to use the fundamental basics of downloading and opening FITS 
files, reading FITS headers, and inputting data into pandas DateFrames, to create a simple astronomy catalog.
In doing so, our team not only was able to become familiar with conceptual astronomical data analysis and a variety of DSOs,
but apply the knowledge and necessary skills gained from lecture to create a fun and engaging project. 




## Technologies Used
- Python 3.14
- JupyterLab 4.4.7
- Astropy
- Matplotlib
- Numpy
- OS
- Pandas
- Urllib
- Streamlit



## Features
Interesting features:
- Accessible through Streamlit
- Images are included in the merged dataframe! 


## Screenshots
Here is where to find URIs for FITS data: "https://github.com/user-attachments/assets/4c0fecc8-9a94-4d5d-a6ae-029d39e27dd6
"


## Setup for Downloading FITS Files
1. Install Python 3.14
2. Use pip install to download the packages listed in "Technologies Used"
3. Access JWST data for a specific by downloading FITS files from the MAST archive. To download, create your own URL by copying URIs from the chosen files' "details" section.
4. Follow the instructions in the Notebook for further guidance on using packages to read FITS headers and display data.
5. Download each image as a JPEG file to store in dataframes. 


## Usage
To access the catalog through JupyterLab, the user must run each object FITS file cell to download, open, and read the data for each FITS file, which allows for the display of images and metadata for each object. Once each cell is run and a merged dataframe is created, the user can download the final catalog as an HTML file. 



## Project Status
Project is: in progress


## Room for Improvement
- Using classes to open FITS files avoid redundant code. 



## Acknowledgements and Helpful Sources
- Idea inspired by Project 2 Suggestions from Astronomy Data Analysis 1221 at The Ohio State University
- https://www.geeksforgeeks.org/python/how-to-create-a-pivot-table-in-python-using-pandas/
- https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html
- https://opencomputinglab.github.io/SubjectMatterNotebooks/astronomy/fits-images.html
- https://tingyuansen.github.io/coding_essential_for_astronomers/lectures/lecture14-astropy-time-observationplanning-fits.html
- https://tingyuansen.github.io/coding_essential_for_astronomers/lectures/lecture12-advanced-pandas.html
- https://stackoverflow.com/questions/53468558/adding-image-to-pandas-dataframe



## Contact
engum-corral.1@osu.edu
orcutt.28@osu.edu
plummer.452@osu.edu
smedley.48@osu.edu
