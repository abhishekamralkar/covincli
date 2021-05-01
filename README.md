![Upload Python Package](https://github.com/abhishekamralkar/covincli/workflows/Upload%20Python%20Package/badge.svg)


<p align="center">
   <img src="https://raw.githubusercontent.com/abhishekamralkar/covincli/master/docs/static/images.jpeg" width="200">
</p>

# covcli — Covid India CLI
---


# COVIN-CLI

The Corona pandemic is on everyone's mind. There are many shiny GUI's available to visualize the
COVID19-India Data. Thanks to all of them.

On other note " I know nothing about epidemiology."

The data source for my tool is https://api.covid19india.org/. A big shout out to all the developers
for there amazing dedication and bring us the formated data and GUI.


# COVIN-CLI

A CLI written in Python3 to get the Covid19-India data.


### Prerequisite

  - You need nothing more than a basic installation of Python 3 or newer and time to work on it.
  - Virtualenv


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
     - This is a  project for me.
     - I am not Python expert. The code might not be well organised or upto mark as of now.
       But I will definitely try to make it upto mark.

## Run CLI

### Country(country)

Command country accepts 1 flag

 - active / confirmed / recovered / deceased

```
python3 covin-cli.py country -a confirmed
Total confirmed cases in India are : 19288819

python3 covin-cli.py country -a active
Total active cases in India are : 3321542

python3 covin-cli.py country -a recovered
Total recovered cases in India are : 15746000

python3 covin-cli.py country -a deceased
Total deceased cases in India are : 212497

```

### State(state)

Command state accepts 2 flags

 - statename
 - active / confirmed / deceased / recovered

Note:- To get Indian States and Union Territories names please refer below Wiki

[Indian State and Union Territories](https://en.wikipedia.org/wiki/States_and_union_territories_of_India)

or you can run a CLI itself to get Indian States and Union Territories names

```
python3 covin-cli.py states-name
```

```
India's States and Union Territories Names are:
------------------------------------------------------------
Total States and Union Territories count in India is: 37

['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Delhi', 'Dadra and Nagar Haveli and Daman and Diu', 'Goa', 'Gujarat', 'Himachal Pradesh', 'Haryana', 'Jharkhand', 'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Maharashtra', 'Meghalaya', 'Manipur', 'Madhya Pradesh', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Puducherry', 'Rajasthan', 'Sikkim', 'Telangana', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

```

```
python3 covin-cli.py state 'Madhya Pradesh' -a confirmed
Total confirmed cases in Madhya Pradesh are: 563327

python3 covin-cli.py state 'Madhya Pradesh' -a active
Total active cases in Madhya Pradesh are: 90796

python3 covin-cli.py state 'Madhya Pradesh' -a recovered
Total recovered cases in Madhya Pradesh are: 466915

python3 covin-cli.py state 'Madhya Pradesh' -a deceased
Total deceased cases in Madhya Pradesh are: 5616

```


### District(district)

Command district accepts 3 flags

 - statename
 - ditrictname
 - active / confirmed / deceased / recovered

Note:- To get Indian States and Union Territories names and respective districts please refer below Wiki

[Indian States and Union Territories and respective districts](https://en.wikipedia.org/wiki/List_of_districts_in_India)

or you can CLI itself to get the districts in a state

```
python3 covin-cli.py districts-name 'Madhya Pradesh'
```

```
State Madhya Pradesh districts names are:
------------------------------------------------------------
['Agar Malwa', 'Alirajpur', 'Anuppur', 'Ashoknagar', 'Balaghat', 'Barwani', 'Betul', 'Bhind', 'Bhopal', 'Burhanpur', 'Chhatarpur', 'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar', 'Dindori', 'Guna', 'Gwalior', 'Harda', 'Hoshangabad', 'Indore', 'Jabalpur', 'Jhabua', 'Katni', 'Khandwa', 'Khargone', 'Mandla', 'Mandsaur', 'Morena', 'Narsinghpur', 'Neemuch', 'Niwari', 'Other Region', 'Panna', 'Raisen', 'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Satna', 'Sehore', 'Seoni', 'Shahdol', 'Shajapur', 'Sheopur', 'Shivpuri', 'Sidhi', 'Singrauli', 'Tikamgarh', 'Ujjain', 'Umaria', 'Vidisha']
```

```
python3 covin-cli.py district 'Madhya Pradesh' 'Indore' -a active
active cases in district Indore are: 12278

python3 covin-cli.py district 'Madhya Pradesh' 'Indore' -a confirmed
confirmed cases in district Indore are: 110840

python3 covin-cli.py district 'Madhya Pradesh' 'Indore' -a recovered
recovered cases in district Indore are: 97423

python3 covin-cli.py district 'Madhya Pradesh' 'Indore' -a deceased
deceased cases in district Indore are: 1139

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
