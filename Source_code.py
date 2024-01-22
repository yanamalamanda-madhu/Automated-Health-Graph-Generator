# Code for import libraries 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import *
from glob import glob
import mplcursors
import matplotlib.gridspec as gridspec
import os

# note: all the csv file names are with same name and the file name must ends with integer

k= int(input("Enter the number 1 or 2 :"))

# code if the csv files are in open space in the project folder in PC
"""
if(k==1):
    new_file=sorted(glob("page-1_table-*"))
if(k==2):
    new_file=sorted(glob("IMG_20230205_013735.jpg*"))

# Code for Reading csv files in order

# Code for merging all csv files into single file
merge_data=pd.concat(pd.read_csv(datafile).assign(sourcefilename=datafile)
for datafile in new_file)
print(merge_data)

# Code for Resetting the index of the merged csv file
merge_data=merge_data.reset_index()

# Code for delting the extra unwanted data in the merged csv file
del merge_data["index"]
del merge_data["Units"]
del merge_data["sourcefilename"]

# Code for deleting the column name Unitis if it is present in the merged csv file
for a in range(len(merge_data.columns)):
    if(merge_data.columns[a-1]=="Unitis"):
        del merge_data["Unitis"] 
"""

# code if the csv files are in folder in the project folder in PC

"""
if (k==1):
    folder_path = 'E:\Documents\Projects\Automatic-Health-Graph-Generator\health_reports-patient_1-csv_format'
if(k==2):
    folder_path = 'E:\Documents\Projects\Automatic-Health-Graph-Generator\health_reports-patient_2-csv_format'
"""

# code if the csv files are in folder in the project folder in github

if(k==1):
    folder_path ='Health_reports_person_1-csv_format'
if(k==2):
    folder_path ='Health_reports_person_2-csv_format'

merge_data = pd.DataFrame()

# Code for Iterate through the files in the folder
for filename in os.listdir(folder_path):
    # Code for to Check if the file has a ".csv" extension
    if filename.endswith('.csv'):
        # Code to Read the CSV file
        file_path = os.path.join(folder_path, filename)
        
        # Code to Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Code to Concatenate the data to the main DataFrame
        merge_data = pd.concat([merge_data, df], ignore_index=True)
        del merge_data["Units"]


# Code for assigning new column names
new_column_names=[]
for k in range(len(merge_data.columns)):
    if(k==0):
        new_column_names.append("Investigation")
    elif(k==1):
        new_column_names.append("Result")
    elif(k==2):
        new_column_names.append("Normal Ranges")
    else:
        new_column_names.append(merge_data.columns[k])
merge_data.columns=new_column_names
print(merge_data)
        
length=len(merge_data)

# Code for checking if the testname have float or nan value
test_index=[]
for i in range(length):
  if type(merge_data['Investigation'][i])==float:
    test_index.append(i)

# Code for storing the dataframe elements in the array form
results=[]
testname=[]
indexes=[]
Interval=[]
Results=merge_data['Result']
Testname=merge_data['Investigation']
interval=merge_data['Normal Ranges']

for k in range(len(Testname)):
    testname.append(Testname[k])
#print(testname)

for j in range(len(Results)):
    results.append(Results[j])
#print(results)

for m in range(len(interval)):
    Interval.append(interval[m])
#print(Interval)

for i in range(len(test_index)):
        results.pop(test_index[i]-i)
        testname.pop(test_index[i]-i)
        Interval.pop(test_index[i]-i)

mad=len(testname)

for l in range(len(Interval)):
    if type(Interval[l])==float:
        indexes.append(l)
print(indexes)

# Code for storing the test names in array form
main_testnames=[]
for k in indexes:
    main_testnames.append(merge_data['Investigation'][k])
#main_testnames
print(len(main_testnames))

# Code for deleting the main test names and its related values in the arrays
for i in range(len(indexes)):
        results.pop(indexes[i]-i)
        testname.pop(indexes[i]-i)
        Interval.pop(indexes[i]-i)
#print(results)
#print(testname)
#print(Interval)
#print(len(results))
#print(len(testname))
#print(len(Interval))

# Code for changing the test names if the test names are repeated
test_names=[]
for j in range(len(testname)):
    for k in range(len(testname)):
        if(j!=k):
            if(testname[j]==testname[k]):
                testname[k]=testname[k].replace(testname[k],testname[k]+str(k))
        else:
            test_names.append(testname[k])

# Code for removing the : in test names
test_name=[]
for i in test_names:
    i=i.replace(':',' ')
    i=i.strip()
    test_name.append(i)

# Code for replace " . " in the place of " , " in numeric data 
result=[]
for i in results:
    if(type(i)==str):
        i=i.replace(',','.')
    #print(i)
    result.append(float(i))

# Code for removing the units and other string data in the Normal Ranges
lower_limit=[]
upper_limit=[]
array=[]
array1=[]
for i in Interval:
    j= i.replace('_', ' ').replace(', ', ' ').replace('-', ' ').replace('mg/dl', ' ').replace('mg/dL', ' ').replace('UP TO','0 ').replace('U/L', ' ').replace('gm/dl', ' ').replace('gms/dl', ' ').replace('mill/cumm','').replace('/uL','').replace('%', ' ').replace('Lakhs/cumm','').replace('fL','').replace('pg','').replace('gms', ' ').replace('CHILDRENS', ' ').replace('ADULTS', ' ').replace('<', '0 ').replace('>', '100 ').replace('g/dL', ' ').replace('mg/dL', ' ').replace('mEq/L', ' ').replace('ng/mL', ' ').replace('ug/dL', ' ').replace('ulU/mL', ' ').replace('mill/mm3', ' ').replace('thou/mm3', ' ').replace('mm/hr', ' ').split()
    if(len(j)>2):
        for k in range(len(j)):
            array1.append(float(j[k]))
        array1=sorted(array1)
        low=str(array1[0])
        high=str(array1[-2])
        j=[low,high]
        print(j)
    else:
        print(j)
    array.append(j)

# Code for converting the data into float type
array1=[]
for i in range(len(array)):
    for j in range(len(array[i])):
        #print(array[i][j])
        #print(type(array[i][j]))
        array1.append(float(array[i][j]))

# Code for separating lower limit and upper limit values
for i in range(len(array1)):
    if i%2==0:
        lower_limit.append(array1[i])
    else:
        upper_limit.append(array1[i])

#  Code for plotting points (Note: 1=Below normal , 2=Normal , 3=Above Normal)
plotting_points=[]
for i in range(len(result)):
    if(result[i]<lower_limit[i]):
        plotting_points.append(1)
    elif(result[i]>upper_limit[i]):
        plotting_points.append(3)
    else:
        plotting_points.append(2)

# Code for creating new indexes
new_indexes=[]
for i in range(len(indexes)):
  if i==0:
    if(indexes[i]!=0):
      new_indexes.append(0)
      new_indexes.append(indexes[i])
    else:
      new_indexes.append(0)
  else:
    new_indexes.append(indexes[i])
if new_indexes[len(new_indexes)-1]!=len(Interval):
  new_indexes.append(mad)

print(new_indexes)

# for index differences:
id=[]
for k in range(len(new_indexes)):
  if k<len(new_indexes)-1:
    if indexes[0]!=0:
      id.append(new_indexes[k+1]-new_indexes[k])
    else:
      id.append(new_indexes[k+1]-new_indexes[k]-1)

print(id)

# Code for legends data
legends_data=[]
for k in range(len(new_indexes)):
  if k<len(new_indexes)-1:
    c=0
    problem_points=[]
    for l in range(new_indexes[k]-k,new_indexes[k+1]-(k+1)):
      if plotting_points[l]==2:
        c+=1
      else:
        problem_points.append(test_name[l])
    if c!=(id[k]):
      z="problem at",problem_points
      legends_data.append(z)
    else:
      legends_data.append("NO SIGNIFICANT ABNORMALITY")

print(legends_data)

# Code for creating the data frame only for testname and plotting points
data={'Test Name':test_name,'condition':plotting_points}
df=pd.DataFrame(data)

# Code for reading the source file
health_file=pd.read_csv("source_health_file.csv")
new_test_names=[]
problem_d=[]
new_med=[]
new_cul=[]
state=[]
reason=[]
for i in range(len(df['Test Name'])):
    for j in range(len(health_file['Test Name'])):
        if(df['Test Name'][i]==health_file['Test Name'][j]):
            if(df['condition'][i]==health_file['state'][j]):
                new_test_names.append(health_file['Test Name'][j])
                #problem_d.append(health_file['Problem'][j])
                new_med.append(health_file['Medition'][j])
                new_cul.append(health_file['culture'][j])
                state.append(health_file['state'][j])
                reason.append(health_file['Reason'][j])
new_data_sheet={'Test Name':new_test_names,'state':state,'Reason':reason,'Medition':new_med,'Culture':new_cul}
newdf=pd.DataFrame(new_data_sheet)
print(newdf)

df.loc[:,'Test Name']

# Code for plotting the graph for test names and result values
plot1=plt.plot(df.loc[:,"Test Name"],result,marker="*")
#cursor = mplcursors.cursor(plot1, hover=True)
plt.xticks(rotation=90)

# Code for plotting the graph for test names and conditions
plt.figure(figsize=(28,6))
plt.plot(df.loc[:,"Test Name"],df['condition'],marker="*")
#cursor = mplcursors.cursor(hover=True)
plt.xticks(rotation=90)
ylab=["",'below normal','normal','above normal',""]
plt.gca().set_yticks(range(len(ylab)))
plt.gca().set_yticklabels(ylab)

fig = plt.figure()
gs0 = gridspec.GridSpec(1,1,figure=fig)
gs00 = gridspec.GridSpecFromSubplotSpec(5,4, subplot_spec=gs0[0])
ax1 = fig.add_subplot(gs00[:-1, :-1])

i=df['Test Name']
j=df['condition']
newdf.loc[:,'Reason']
newdf.loc[:,'Medition']
newdf.loc[:,'Culture']
tt=newdf['Reason'].values
tt1=newdf['Medition'].values
tt2=newdf['Culture'].values

for k in range(len(indexes)):
    for l in range(len(indexes)):
        if(k<len(indexes)-1):
            if(k==l):
                if(k==0):
                    plt.plot(df.loc[:,"Test Name"][indexes[k]:indexes[k+1]],df['condition'][indexes[k]:indexes[k+1]],marker="*")
                else:
                    plt.plot(df.loc[:,"Test Name"][indexes[k]-l:indexes[k+1]-l],df['condition'][indexes[k]-l:indexes[k+1]-l],marker="*")
        else:
            plt.plot(df.loc[:,"Test Name"][indexes[k]-k:len(df.loc[:,'Test Name'])],df['condition'][indexes[k]-k:len(df['condition'])],marker="*")
scatter = plt.scatter(i,j,marker="*")
plt.xticks(rotation=90)
ylab=["",'below\nnormal','normal','above\nnormal',"",""]
plt.gca().set_yticks(range(len(ylab)))
plt.gca().set_yticklabels(ylab)
#leg = ax1.legend(fancybox=True, shadow=True)
legend=plt.legend(main_testnames,loc='upper right')

ax3 = fig.add_subplot(gs00[:1,:1])
labels=["Reason","Medicine","culture"]
activated = [False,False,False]
check = CheckButtons(ax3, labels, activated)

ax2 = fig.add_subplot(gs00[:,-1])
plt.axis('off')
texth=ax2.text(0.02, 0.75,"Reason :",horizontalalignment='left',verticalalignment='top',wrap='True',fontsize=14,transform=ax2.transAxes)
text1h=ax2.text(0.02, 0.50,"Medition :",horizontalalignment='left',verticalalignment='top',wrap='True',fontsize=14,transform=ax2.transAxes)
text2h=ax2.text(0.02, 0.25,"Culture :",horizontalalignment='left',verticalalignment='top',wrap='True',fontsize=14,transform=ax2.transAxes)
text3h=ax2.text(0.02, 0.99,"Problem :",horizontalalignment='left',verticalalignment='top',wrap='True',fontsize=14,transform=ax2.transAxes)
#lines=[text.set_visible(True),text1.set_visible(True),text2.set_visible(True)]

#format_axes(fig)
text_display = ax1.annotate("", xy=(0,0), xytext=(5,5),textcoords="offset points",bbox=dict(boxstyle='round',fc='linen',ec='k',lw=1),wrap='True')
text_display.set_visible(True)
text_display1 = ax2.annotate("", xy=(0.02,0.55), xytext=(5,5),textcoords="offset points",bbox=dict(boxstyle='round',fc='linen',ec='k',lw=1),wrap='True')
text_display1.set_visible(True)
text_display2 = ax2.annotate("", xy=(0.02,0.30), xytext=(5,5),textcoords="offset points",bbox=dict(boxstyle='round',fc='linen',ec='k',lw=1),wrap='True')
text_display2.set_visible(True)
text_display3 = ax2.annotate("", xy=(0.02,0.05), xytext=(5,5),textcoords="offset points",bbox=dict(boxstyle='round',fc='linen',ec='k',lw=1),wrap='True')
text_display3.set_visible(True)

ax3 = fig.add_subplot(gs00[:1,:1])
labels=["Reason","Medicine","culture"]
activated = [False,False,False]
check = CheckButtons(ax3, labels, activated)
label_index_array=[]
def func(label): 
    index = labels.index(label)
    print(index)
    if index==0: 
        label_index_array.append(0)
    elif index==1:
        label_index_array.append(1)
    elif index==2:
        label_index_array.append(2)

    re=label_index_array.count(0)
    me=label_index_array.count(1)
    cu=label_index_array.count(2)
    print(re,me,cu)

    if(label==labels[0]):
        if(re%2!=0):
            def motion_hover(event):
                annotation_visbility = text_display.get_visible()
                if event.inaxes == ax1:
                    is_contained, annotation_index = scatter.contains(event)
                    if is_contained:
                        data_point_location = scatter.get_offsets()[annotation_index['ind'][0]]
                        text_display.xy = data_point_location
                        text_label1 = '{}'.format([tt[n] for n in annotation_index['ind']])
                        text_display1.set_text(text_label1)
                        text_display1.set_visible(True)
                        fig.canvas.draw_idle()
                    else:
                        if annotation_visbility:
                            text_display1.set_visible(False)            
                            fig.canvas.draw_idle()
                            
            fig.canvas.mpl_connect('motion_notify_event', motion_hover) 
        else:
            def hover(event):
                text_display1.set_visible(False)
            fig.canvas.mpl_connect("motion_notify_event", hover)
    if(label==labels[1]):
        if(me%2!=0):
            def motion_hover(event):
                annotation_visbility = text_display.get_visible()
                if event.inaxes == ax1:
                    is_contained, annotation_index = scatter.contains(event)
                    if is_contained:
                        data_point_location = scatter.get_offsets()[annotation_index['ind'][0]]
                        text_display.xy = data_point_location
                        text_label2 = '{}'.format([tt1[n] for n in annotation_index['ind']])
                        text_display2.set_text(text_label2)
                        text_display2.set_visible(True)
                        fig.canvas.draw_idle()
                    else:
                        if annotation_visbility:
                            text_display2.set_visible(False)            
                            fig.canvas.draw_idle()
                            
            fig.canvas.mpl_connect('motion_notify_event', motion_hover) 
        else:
            def hover(event):
                text_display2.set_visible(False)
            fig.canvas.mpl_connect("motion_notify_event", hover)
        
    if(label==labels[2]):
        if(cu%2!=0):
            def motion_hover(event):
                annotation_visbility = text_display.get_visible()
                if event.inaxes == ax1:
                    is_contained, annotation_index = scatter.contains(event)
                    if is_contained:
                        data_point_location = scatter.get_offsets()[annotation_index['ind'][0]]
                        text_display.xy = data_point_location
                        text_label3 = '{}'.format([tt2[n] for n in annotation_index['ind']])
                        text_display3.set_text(text_label3)
                        text_display3.set_visible(True)
                        fig.canvas.draw_idle()
                    else:
                        if annotation_visbility:
                            text_display3.set_visible(False)            
                            fig.canvas.draw_idle()
                            
            fig.canvas.mpl_connect('motion_notify_event', motion_hover) 
        else:
            def hover(event):
                text_display3.set_visible(False)
            fig.canvas.mpl_connect("motion_notify_event", hover)
               
check.on_clicked(func)

main_test_names=legend.get_lines()

for k in main_test_names:
    k.set_picker(True)
    k.set_pickradius(10)
  
graphs={}
for k in range(len(main_testnames)):
    main_testnames[k]=plt.text(0.02, 0.95,legends_data[k],horizontalalignment='left',verticalalignment='top',wrap='True',fontsize=12,transform=ax2.transAxes)
    main_testnames[k].set_visible(False)

for k in range(len(main_test_names)):
    graphs[main_test_names[k]]=main_testnames[k]

def on_pick(event):
    leg=event.artist
    isVisible=leg.get_visible()
    graphs[leg].set_visible(isVisible)
    legend.set_visible(isVisible)
    fig.canvas.draw()
    def hover(event):
        for k in range(len(main_testnames)):
            main_testnames[k].set_visible(False)
    fig.canvas.mpl_connect("motion_notify_event", hover)        
plt.connect('pick_event',on_pick)

plt.show()
