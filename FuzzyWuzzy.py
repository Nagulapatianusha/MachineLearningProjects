 
import pandas as pd
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import re
import time

start_time = time.localtime()
Start_timestamp = time.strftime('%b-%d-%Y_%H%M', start_time)

master_data = pd.read_csv('C:\\Users\\Documents\\Fuzzy_Match\\Data\\vendor_data.csv', encoding = 'latin',usecols = ['<ID>','Product (EPH)','Size','Vendor Entered Size'])

master_data['Vendor_Entered_Size'] = master_data['Vendor Entered Size'].apply(lambda x: ''.join([i if 32 < ord(i) < 126 else " " for i in str(x)]))

master_data_size_list = list(master_data['Vendor_Entered_Size'])    

master_1 = master_data_size_list
len(master_1)
print(master_1)

master_2=[]
for i in master_1:
   
   master_2.append(re.sub('[^A-Za-z0-9.]+', '', str(i).lower().strip()))
   
len(master_2)
print(master_2)


master_3=[]
    
for i in master_2:
        
        if re.search('[0-9]+', i): 
            if ('inch' in i):
                a=str(i).replace('inch','in')
                master_3.append(a)
            elif ('ins' in i):
                a=str(i).replace('ins','in')
                master_3.append(a)
            elif ('ins.' in i):
                a=str(i).replace('ins.','in')
                master_3.append(a)
            elif ('in.' in i):
                a=str(i).replace('in.','in')
                master_3.append(a)
            elif ('ft.' in i):
                a=str(i).replace('ft.','ft')
                master_3.append(a)
            elif ('qt.' in i):
                a=str(i).replace('qt.','qt')
                master_3.append(a)
            elif ('lbs' in i):
                a=str(i).replace('lbs','lb')
                master_3.append(a)
            elif ('lb.' in i):
                a=str(i).replace('lb.','lb')
                master_3.append(a)
            elif ('ea.' in i):
                a=str(i).replace('ea.','ea')
                master_3.append(a)
            elif ('doz.' in i):
                a=str(i).replace('doz.','doz')
                master_3.append(a)
            elif ('pt.' in i):
                a=str(i).replace('pt.','pt')
                master_3.append(a)
            elif ('sq.' in i):
                a=str(i).replace('sq.','sq')
                master_3.append(a)
            elif ('tbsp.' in i):
                a=str(i).replace('tbsp.','tbsp')
                master_3.append(a)
            elif ('tsp.' in i):
                a=str(i).replace('tsp.','tsp')
                master_3.append(a)
            elif ('yd.' in i):
                a=str(i).replace('yd.','yd')
                master_3.append(a)
            else:
                master_3.append(i)
        else:
            master_3.append(i)
            
            
   
len(master_3)
#print(master_3)


master_final = pd.DataFrame(columns = ['EPH_Name','Size_Vendor_Entered','Vendor_Cleaned_size'])
master_final['Size_Vendor_Entered'] = master_data['Vendor Entered Size']
master_final['Vendor_Cleaned_size'] = master_3
master_final['EPH_Name'] = master_data['Product (EPH)']


#lookup.head(10)
#lookup.columns



lookup_data = pd.read_csv("C:\\Users\\Documents\\Fuzzy_Match\\Data\\size_eph.csv", encoding = 'latin',usecols = ['EPH','SIZE'])


lookup_data['Lookup_Size'] = lookup_data['SIZE'].apply(lambda x: ''.join([i if 32 < ord(i) < 126 else " " for i in str(x)]))


lookup_data_size_list = list(lookup_data['Lookup_Size'])    


  

lookup_1=lookup_data_size_list

lookup_2 = []
for i in lookup_1:
   
   lookup_2.append(re.sub('[^A-Za-z0-9.]+', '', str(i).lower().strip()))
   
   
lookup_3=[]
    
for i in lookup_2:
        #i.replace('ins',"inch")
        if re.search('[0-9]+', i): #and  re.search('in\d$',i):
            if ('inch' in i):
                a=str(i).replace('inch','in')
                lookup_3.append(a)
            elif ('ins' in i):
                a=str(i).replace('ins','in')
                lookup_3.append(a)
            elif ('ins.' in i):
                a=str(i).replace('ins.','in')
                lookup_3.append(a)
            elif ('in.' in i):
                a=str(i).replace('in.','in')
                lookup_3.append(a)
            elif ('ft.' in i):
                a=str(i).replace('ft.','ft')
                lookup_3.append(a)
            elif ('qt.' in i):
                a=str(i).replace('qt.','qt')
                lookup_3.append(a)
            elif ('lbs' in i):
                a=str(i).replace('lbs','lb')
                lookup_3.append(a)
            elif ('lb.' in i):
                a=str(i).replace('lb.','lb')
                lookup_3.append(a)
            elif ('ea.' in i):
                a=str(i).replace('ea.','ea')
                lookup_3.append(a)
            elif ('doz.' in i):
                a=str(i).replace('doz.','doz')
                lookup_3.append(a)
            elif ('pt.' in i):
                a=str(i).replace('pt.','pt')
                lookup_3.append(a)
            elif ('sq.' in i):
                a=str(i).replace('sq.','sq')
                lookup_3.append(a)
            elif ('tbsp.' in i):
                a=str(i).replace('tbsp.','tbsp')
                lookup_3.append(a)
            elif ('tsp.' in i):
                a=str(i).replace('tsp.','tsp')
                lookup_3.append(a)
            elif ('yd.' in i):
                a=str(i).replace('yd.','yd')
                lookup_3.append(a)
            else:
                lookup_3.append(i)
        else:
            lookup_3.append(i)
               

lookup_final = pd.DataFrame(columns = ['EPH','Size_lookup','Cleaned_lookup_size'])
lookup_final['Size_lookup'] = lookup_data_size_list
lookup_final['Cleaned_lookup_size'] = lookup_3
lookup_final['EPH'] = lookup_data['EPH']


for i,j,k in lookup_final.values:
   print (i,j,k)
#master_final.values[0]

print ("Enter integer")

option=int(input())
o=1
result = []
for i,j,k in master_final.values:
    #print (Vendor_Brand)
    print (o)
    o=o+1
    if (str(k).lower() == 'n/a' or str(k).lower() == 'none' or str(k).lower() == 'unbranded' or str(k).lower() == 'nan'):
        result.append([i,k,j,"This is a blank field","This is a blank field", 0])
    else:
        d=[]
        for l,m,n in lookup_final.values:
            if str(i) == str(l):
                d.append([i,k,j,n,m, fuzz.token_sort_ratio(str(k),str(n))])
            else:
                next
        ll=sorted(d,key=lambda x: x[5], reverse = True)
        for z in ll[:option]:
            result.append(z)
#sunoj[-2]
        


final_v2 = pd.DataFrame(columns = ['EPH','Cleanedup_Vendor_Size','Size_Vendor','Cleanedup_Lookup_Size','Lookup_Size', 'Score'])

col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]

for i in result:
    #print(i[3])
    col1.append(i[0])

for j in result:
    col2.append(j[1])
    
for k in result:
    col3.append(k[2])
    
for l in result:
    col4.append(l[3])

for m in result:
    col5.append(m[4])    

for n in result:
    col6.append(n[5]) 
    
    
    
final_v2['EPH'] = col1
final_v2['Cleanedup_Vendor_Size'] = col2
final_v2['Size_Vendor'] = col3
final_v2['Cleanedup_Lookup_Size'] = col4
final_v2['Lookup_Size'] = col5
final_v2['Score'] = col6


final_v2.to_excel('C:\\Users\\Documents\\Fuzzy_Match\\Result\\Size.xls')

end_time = time.localtime()
end_timestamp = time.strftime('%b-%d-%Y_%H%M', end_time)


print(Start_timestamp)print(end_timestamp)