#!/usr/bin/python3
'''Sever side rendering with Python'''

import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):

        raise TypeError('template must be a string')
    if not template:
        raise ValueError('Template is empty, no output files generated.')
    
    if not isinstance(attendees, list) or \
        not all(isinstance(dict_attendee, dict) 
                for dict_attendee in attendees):
        raise TypeError('attendees must be a list and with only dictionaries')
    if not attendees:
        raise ValueError('No data provided, no output files generated.')
    
    try:
        num = 1
        for attendee in attendees:
            mail = template
            keys = ['name', 'event_title', 'event_location', 'event_date']
            for key in keys:
                word = attendee.get(key, "N/A")
                mail = mail.replace(f'{{{key}}}', 
                                    word if word is not None else f"{key}: N/A")

            if os.path.exists(f'output_{num}.txt'):
                print(f'output_{num}.txt already exists, skipping writting')
                continue
            with open(f'output_{num}.txt', 'w') as file:
                file.write(mail)
            num = num + 1
    except TypeError as e:
        return e
    except ValueError as e:
        return e