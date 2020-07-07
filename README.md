# COVINCLI

The Corona pandemic is on everyone's mind. There are many shiny GUI's available to visualize the
COVID19-India Data. Thanks to all of them.

On other note " I know nothing about epidemiology."

The data source for my tool is https://api.covid19india.org/. A big shout out to all the developers
for there amazing dedication and bring us the formated data and GUI.


# COVINCLI

A CLI written in Python3 to get the Covid19-India data.


### Prerequisite

  - You need nothing more than a basic installation of Python 3.6 or newer and time to work on it.
  - Virtualenv

Follow below step to install and setup the Python Virtual Env

```
sudo pip3 install virtualenv
python3 -m venv covid19
source covid19/bin/activate
pip3 install -r requirements.txt
```

### Goal

An attempt to create a 1st COVID-19 India CLI.


### Currently tool support 7 subcommands

     - country
     - district
     - state
     - state-cases
     - district-cases
     - states-name
     - districts-name

Note:

     - The CLI is still WIP and the arguments may change over the period of time.
     - This is a fun project for me.
     - I am not Python expert

## Run CLI

### Country(country)

Command country accepts 1 flag

 - active / confirmed / recovered / deceased

```
❯ covid19/bin/python3 covid.py country -a confirmed
Total confirmed cases in India are : 336370

❯ covid19/bin/python3 covid.py country -a active
Total active cases in India are : 154144

❯ covid19/bin/python3 covid.py country -a recovered
Total recovered cases in India are : 172578

❯ covid19/bin/python3 covid.py country -a deceased
Total deceased cases in India are : 9597
```

### State(state)

Command state accepts 2 flags

 - statename
 - active / confirmed / deceased / recovered

Note:- To get Indian States and Union Territories names please refer below Wiki

[[https://en.wikipedia.org/wiki/States_and_union_territories_of_India][Indian State and Union Territories]]

or you can run a CLI itself to get Indian States and Union Territories names

```
covid19/bin/python3 covid.py states-name

India's States and Union Territories Names are:
<--******************************************-->
['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Delhi', 'Dadra and Nagar Haveli and Daman and Diu', 'Goa', 'Gujarat', 'Himachal Pradesh', 'Haryana', 'Jharkhand', 'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Maharashtra', 'Meghalaya', 'Manipur', 'Madhya Pradesh', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Puducherry', 'Rajasthan', 'Sikkim', 'Telangana', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
```

```
❯ covid19/bin/python3 covid.py state 'Madhya Pradesh' -a confirmed
Total confirmed cases in Madhya Pradesh are: 10935

❯ covid19/bin/python3 covid.py state 'Madhya Pradesh' -a active
Total active cases in Madhya Pradesh are: 2567

❯ covid19/bin/python3 covid.py state 'Madhya Pradesh' -a recovered
Total recovered cases in Madhya Pradesh are: 7903

❯ covid19/bin/python3 covid.py state 'Madhya Pradesh' -a deceased
Total deceased cases in Madhya Pradesh are: 465
```


### District(district)

Command district accepts 3 flags

 - statename
 - ditrictname
 - active / confirmed / deceased / recovered

Note:- To get Indian States and Union Territories names and respective districts please refer below Wiki

[[https://en.wikipedia.org/wiki/List_of_districts_in_India][Indian States and Union Territories and respective districts]]

or you can CLI itself to get the districts in a state

```
covid19/bin/python3 covid.py districts-name 'Madhya Pradesh'

State Madhya Pradesh districts names are:
<-******************************************->
['Agar Malwa', 'Alirajpur', 'Anuppur', 'Ashoknagar', 'Balaghat', 'Barwani', 'Betul', 'Bhind', 'Bhopal', 'Burhanpur', 'Chhatarpur', 'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar', 'Dindori', 'Guna', 'Gwalior', 'Harda', 'Hoshangabad', 'Indore', 'Jabalpur', 'Jhabua', 'Katni', 'Khandwa', 'Khargone', 'Mandla', 'Mandsaur', 'Morena', 'Narsinghpur', 'Neemuch', 'Niwari', 'Other Region', 'Panna', 'Raisen', 'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Satna', 'Sehore', 'Seoni', 'Shahdol', 'Shajapur', 'Sheopur', 'Shivpuri', 'Sidhi', 'Singrauli', 'Tikamgarh', 'Ujjain', 'Umaria', 'Vidisha']
```

```
❯ covid19/bin/python3 covid.py district 'Madhya Pradesh' 'Indore' -a active
active cases in district Indore are: 989

❯ covid19/bin/python3 covid.py district 'Madhya Pradesh' 'Indore' -a confirmed
confirmed cases in district Indore are: 4069

❯ covid19/bin/python3 covid.py district 'Madhya Pradesh' 'Indore' -a active
active cases in district Indore are: 989

❯ covid19/bin/python3 covid.py district 'Madhya Pradesh' 'Indore' -a recovered
recovered cases in district Indore are: 2906

❯ covid19/bin/python3 covid.py district 'Madhya Pradesh' 'Indore' -a deceased
deceased cases in district Indore are: 174
```


### District Cases(districts-cases)

Command district-cases accepts 2 flags

 - statename
 - active / confirmed / deceased / recovered


```
covid19/bin/python3 covid.py district-cases 'Madhya Pradesh' -a active

active cases in district Agar Malwa are: 2
active cases in district Alirajpur are: 0
active cases in district Anuppur are: 5
active cases in district Ashoknagar are: 15
active cases in district Balaghat are: 5
active cases in district Barwani are: 9
active cases in district Betul are: 4
```

### State Cases(state-cases)

Command state-cases accepts 1 flag

 - statename


```
❯ covid19/bin/python3 covid.py state-cases 'Madhya Pradesh'

<-****************************************************->
Covid19 information for district Agar Malwa
<-****************************************************->
notes

active 2

confirmed 15

deceased 1

recovered 12

delta {'confirmed': 0, 'deceased': 0, 'recovered': 0}
```
