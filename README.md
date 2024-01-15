# Automated Health Graph Generator
## Table of Contents :
 1. Introduction
 2. Requirements
 3. Health reports in image format
 4. Health reports in CSV file format
 5. Results
 6. Conclusion
## Introduction:
It is very difficult to understand the medical reports for normal people who didn’t study MBBS. And 
a specialist is needed to analyse the medical reports and tells about the patient health problem, condition and 
health status of the person, medicine, curation, remedy, solution for the problem, and if need of any changes 
in the food habits that the patient should follow. To derive meaningful insights from voluminous healthcare 
data, it is essential to convert it into machine understandable knowledge. Currently, machine understandable 
domain specific healthcare knowledge curation framework does not exist for complete body of human. By 
these automated systems helps extraction of medical reports data and the data is saved in the machine 
understandable format. The better way to convey the medical health reports is graphs or images. After the 
extraction of medical health data, graph is generated based on the extracted data. The automated graph helps 
in monitoring and recording all the vital information of a particular patient by maintaining all the records. Most 
prior work on information extraction has focused on extracting information from texts in digital documents.
With this automated graph generator, patient data can be extracted, moved, integrated, and accessed seamlessly 
so that the patient is never inconvenienced.
## Requirements:
### 1 . Pandas 
### Installing Pandas
We need to install it in our system using the pip command. Type the cmd command in the search box and locate the folder using the cd command where python-pip file has been installed. After locating it, type the command:</br>
```md
pip install pandas
```
### Importing Pandas
After the pandas have been installed into the system, you need to import the library. This module is generally imported as follows:
```md
import pandas as pd
```
### 2 . Matplotlib
### Installing Matplotlib
We need to install it in our system using the pip command. Type the cmd command in the search box and locate the folder using the cd command where python-pip file has been installed. After locating it, type the command:</br>
```md
pip install matplotlib
```
### Importing Matplotlib
After the Matplotlib have been installed into the system, you need to import the library. This module is generally imported as follows:
```md
import matplotlib.pyplot as plt
```
```md
from matplotlib.widgets import *
```
```md
import matplotlib.gridspec as gridspec
```
### 3 . Glob
### Importing glob
This module is generally imported as follows:
```md
from glob import glob
```
### 4 . Mplcursors
### Installing Mplcursors
We need to install it in our system using the pip command. Type the cmd command in the search box and locate the folder using the cd command where python-pip file has been installed. After locating it, type the command:</br>
```md
pip install mplcursors
```
### Importing Mplcursors
After the Mplcursors have been installed into the system, you need to import the library. This module is generally imported as follows:
```md
import mplcursors
```
## Health reports in image format
### sample health reports of person 1
![person 1 health report document 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1/Complete%20blood%20picture.jpeg)
![person 1 health report document 2](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1/Liver%20fuction%20report.jpeg)
### sample health reports of person 2
![person 2 health report document 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_2/Hemogram.jpeg)
![person 2 health report document 2](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_2/Lipid%20screen%20serum.jpeg)
![person 2 health report document 3](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_2/Liver%20kidney%20panel%20serum%20.jpeg)

## Health reports in CSV file format
### sample health reports of person 1
[person 1 health report document 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1-csv_format/page-1_table-2.csv)</br>
[person 1 health report document 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1-csv_format/page-1_table-3.csv)</br>
[person 1 health report document 2](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1-csv_format/page-1_table-1.csv)</br>
### sample health reports of person 2
[person 2 health report document 1](Health_reports_person_2-csv_format/IMG_20230205_013735.jpg1.csv)</br>
[person 2 health report document 2](Health_reports_person_2-csv_format/IMG_20230205_013735.jpg.csv)</br>
[person 2 health report document 3](Health_reports_person_2-csv_format/IMG_20230205_013735.jpg2.csv)</br>


 
