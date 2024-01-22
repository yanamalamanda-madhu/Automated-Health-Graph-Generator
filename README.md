# Automated Health Graph Generator
## Table of Contents :
 1. Introduction
 2. Requirements
 3. Health reports in image format
 4. Health reports in CSV file format
 5. Results
 6. Conclusion
## Introduction:
It is very difficult to understand the medical reports for normal people who didn’t study MBBS. And a specialist is needed to analyse the medical reports and tells about the patient health problem, condition and health status of the person, medicine, curation, remedy, solution for the problem, and if need of any changes in the food habits that the patient should follow. To derive meaningful insights from voluminous healthcare data, it is essential to convert it into machine understandable knowledge. Currently, machine understandable 
domain specific healthcare knowledge curation framework does not exist for complete body of human. By these automated systems helps extraction of medical reports data and the data is saved in the machine understandable format. The better way to convey the medical health reports is graphs or images. After the extraction of medical health data, graph is generated based on the extracted data. The automated graph helps in monitoring and recording all the vital information of a particular patient by maintaining all the records. Most prior work on information extraction has focused on extracting information from texts in digital documents.With this automated graph generator, patient data can be extracted, moved, integrated, and accessed seamlessly so that the patient is never inconvenienced.
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
### Importing OS
Python OS module provides the facility to establish the interaction between the user and the operating system.This module is generally imported as follows:
```md
import os
```
## Health reports in image format
### sample health reports of person 1
![person 1 health report document 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1/Complete%20blood%20picture.jpeg)
![person 1 health report document 2](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1/Liver%20fuction%20report.jpeg)
### sample health reports of person 2
![person 2 health report document 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_2/Hemogram.jpeg)</br>

 > The above figure about the Hemogram test report. This test is necessary in diagnosing anemia,
hematological cancers, infections, acute hemorrhagic states, allergies, and immunodeficiencies. This tests are 
also used to monitoring side effects of certain drugs.</br>

![person 2 health report document 2](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_2/Lipid%20screen%20serum.jpeg)</br>

> The above figure about the Lipid Screen, Serum Test Report. It is a test to determine if your 
cholesterol level is normal or falls into a borderline, intermediate or high-risk category. It is used to monitor 
and screen for your risk of cardiovascular disease. This test is to help diagnose other medical conditions, such 
as liver disease </br>

![person 2 health report document 3](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_2/Liver%20kidney%20panel%20serum%20.jpeg)</br>

> The above figure about the Liver &Kidney Panel Test report. These tests check the overall 
health of your liver. It helps to diagnose liver diseases, such as hepatitis. Monitor treatment of liver disease. 
It checks how badly a liver has been damaged or scarred by diseases, such as cirrhosis. It monitors the side 
effects of medicines. Thyroid tests are used to checks how well your thyroid is working and to find the 
cause of problems such as hyperthyroidism or hypothyroidism.

## Health reports in CSV file format
### sample health reports of person 1
[person 1 health report document 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1-csv_format/page-1_table-2.csv)</br>
[person 1 health report document 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1-csv_format/page-1_table-3.csv)</br>
[person 1 health report document 2](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Health_reports_person_1-csv_format/page-1_table-1.csv)</br>
### sample health reports of person 2
[person 2 health report document 1](Health_reports_person_2-csv_format/IMG_20230205_013735.jpg1.csv)</br>
[person 2 health report document 2](Health_reports_person_2-csv_format/IMG_20230205_013735.jpg.csv)</br>
[person 2 health report document 3](Health_reports_person_2-csv_format/IMG_20230205_013735.jpg2.csv)</br>

## Results
### Results of person 1
![results of person 1 image 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Results/Results%20of%20person%201.png)</br>

> The above figure about the total health analysis. The graph is plotted based on the Test names on 
X- Axis and Condition on Y-Axis. The graph contains three stages below normal, normal, above normal. The 
graph contains checkboxes which are used to display the text which is necessary by the person. If cursor is 
moved to particular point(test name) then only it shows information regarding the Reason, Medicine, Food 
culture based on the check boxes input . Legends data represents the main test names in the health reports. 
</br>

![results of person 1 image 2](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Results/Results%20of%20person%201%20-1.png)</br>

>  The above figure about the situating a problem. The graph is plotted based on the Test names on 
X- Axis and Condition on Y-Axis. The graph contains three stages below normal, normal, above normal. The 
graph contains checkboxes which are used to display the text which is necessary by the person. If cursor is 
moved to particular point(test name) then only it shows information regarding the Reason, Medicine, Food 
culture based on the check boxes input . Legends data represents the main test names in the health reports. 
When we click on legends data then it displays where the problem is situated for the particular main Test Name.</br>

### Results of person 2
![results of person 2 image 1](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Results/Results%20of%20person%202.png)</br>

> The above figure about the total health analysis. The graph is plotted based on the Test names on 
X- Axis and Condition on Y-Axis. The graph contains three stages below normal, normal, above normal. The 
graph contains checkboxes which are used to display the text which is necessary by the person. If cursor is 
moved to particular point(test name) then only it shows information regarding the Reason, Medicine, Food 
culture based on the check boxes input . Legends data represents the main test names in the health reports. </br>

![results of person 2 image 2](https://github.com/yanamalamanda-madhu/Automated-Health-Graph-Generator/blob/main/Results/Results%20of%20person%202%20-%201.png)</br>

>  The above figure about the situating a problem. The graph is plotted based on the Test names on 
X- Axis and Condition on Y-Axis. The graph contains three stages below normal, normal, above normal. The 
graph contains checkboxes which are used to display the text which is necessary by the person. If cursor is 
moved to particular point(test name) then only it shows information regarding the Reason, Medicine, Food 
culture based on the check boxes input . Legends data represents the main test names in the health reports. 
When we click on legends data then it displays where the problem is situated for the particular main Test Name.</br>

## Conclusion
An automatic health graph generator can be a useful tool in healthcare settings for tracking and monitoring  patient health data over time. By automating the graph generation process, healthcare professionals can save time and resources while also ensuring accuracy and consistency in the presentation of data. However, it is important to ensure that the data being used for graph generation is reliable and meaningful, and that appropriate data privacy  and security measures are in place. Additionally, healthcare professionals should interpret the graphs in the context of the patient's overall health status and medical history, and not rely solely on the graphs for clinical decision making. While an automatic health graph generator can be a valuable tool for presenting and visualizing patient health data over time, healthcare professionals should use it as a supplement to their clinical judgment and 
expertise, rather than relying solely on the graphs for making medical decisions. The graphs can provide useful insights and trends in the patient's health data, but they should not be used as the only basis for diagnosis or treatment decisions. Healthcare professionals should interpret the graphs in the context of the patient's overall health status, medical history, and any other relevant factors, and make decisions based on a comprehensive assessment of all available information.




 
