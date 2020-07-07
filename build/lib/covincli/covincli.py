#!/usr/bin/env python3

import urllib.request
import json
import click
import pprint
import os

__author__ = "Abhishek Anand Amralkar"


api_url = "https://api.covid19india.org/state_district_wise.json"
operands = ['active', 'confirmed', 'deceased', 'recovered']

@click.group()
def main():
    """
    CLI for querying Covid19 Data for India by Abhishek Amralkar
    """
    pass


def states_data(statename):
    '''
    function queries the covid19 india api and get the state data
    district wise
    '''
    try:
        with urllib.request.urlopen(api_url) as response:
            if response.getcode() == 200:
                source = response.read()
                states_data = json.loads(source)
                result = states_data[statename]['districtData']
                return result
            else:
                print('An error occurred while attempting to retrieve data from the API.')
    except Exception as e:
        click.echo(
            print(hello))

@main.command()
@click.option(
    '--acrd', '-a',
    help='active, deceased, recovered, confirmed'
)
def country(acrd):
    '''
    function return the total cases across country(India)
    '''
    with urllib.request.urlopen(api_url) as response:
        if response.getcode() == 200:
            source = response.read()
            states_data = json.loads(source)
            count = 0
            try:
                for state, state_info in states_data.items():
                    for district, district_info in state_info['districtData'].items():
                        count += district_info.get(acrd)
                click.echo(
                    print(f"Total {acrd} cases in India are : {count}", end=''))
            except Exception as e:
                click.echo(
                    print(f"Unsupported Operand {acrd}. Supported Operands are: \n{os.linesep.join(operands)}"))
        else:
            click.echo(
                print('An error occurred while attempting to retrieve data from the API.'))
 

@main.command()
def states_name():
    '''
    function return the Indian States and Union Territories Name
    '''
    with urllib.request.urlopen(api_url) as response:
        if response.getcode() == 200:
            source = response.read()
            states_data = json.loads(source)
            print(f"India's States and Union Territories Names are:")
            print("-" * 60)
            state_list = []
            try:
                for state, info in states_data.items():
                    state_list.append(state)
                
                click.echo(
                    print(f"Total States and Union Territories count in India is: {len(state_list)}")
                )
                click.echo(
                    print(state_list[1:]))
                return state_list[1:]
            except Exception as e:
                click.echo(
                    print('An error occurred while attempting to retrieve States names.'))
        else:
            click.echo(
                print('An error occurred while attempting to retrieve data from the API.'))


@main.command()
@click.argument('statename')
def districts_name(statename):
    '''
    function return the districts name given the state name
    '''
    try:
        state = states_data(statename)
        print(f"State {statename} districts names are:")
        print("-" * 60)
        district_list = []
        for district, info in state.items():
            district_list.append(district)
        click.echo(
            print(district_list))
    except Exception as e:
        click.echo(
            print(f"Please check State/Union Territory Name. Below is the list {states_name()}"))


@main.command()
@click.argument('statename')
@click.option(
    '--acrd', '-a',
    help='active, deceased, recovered, confirmed'
)
def state(statename, acrd):
    '''
    function returns the total statewise cases like
    active, recovered, deceased, confirmed
    '''
    state = states_data(statename)
    #print(state)
    count = 0
    for district, info in state.items():
        count += info.get(acrd)
    click.echo(
                print(f"Total {acrd} cases in {statename} are: {count}", end=''))
    return count


@main.command()
@click.argument('statename')
def state_cases(statename):
    '''
    fucntion returns the state data district wise
    with all the keys
    '''
    state = states_data(statename)
    #pprint(type(state))
    for district, info in state.items():
        print("-" * 60)
        print('Covid19 information for district', district)
        print("-" * 60)
        for key in info:
            click.echo(print(f"{key} {info[key]}"))


@main.command()
@click.argument('statename')
@click.option(
    '--acrd', '-a',
    help='active, deceased, recovered, confirmed'
)
def districts_cases(statename, acrd):
    '''
    function returns the district wise data for the key
    active, deceased, confirmed, recovered, delta.
    It takes input as a state name and the key mentioned above
    with flag -a or --acrd.
    '''
    state = states_data(statename)
    for district, info in state.items():
        #print(type(info))
        click.echo(
            print(f"{acrd} cases in district {district} are: {info.get(acrd)}", end=''))


@main.command()
@click.argument('statename')
@click.argument('districtname')
@click.option(
    '--acrd', '-a',
    help='active, deceased, recovered, confirmed'
)
def district(statename, districtname, acrd):
    '''
    function returns the district wise data for the key
    active, deceased, confirmed, recovered, delta.
    It takes input as a state name and the key mentioned above
    with flag -a or --acrd.
    '''
    state = states_data(statename)
    for district, info in state.items():
        if district.lower() == districtname.lower():
            click.echo(
                print(f"{acrd} cases in district {districtname} are: {info.get(acrd)}", end=''))



if __name__ == '__main__':
    main()
