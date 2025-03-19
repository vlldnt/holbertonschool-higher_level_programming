#!/usr/bin/python3
'''Sever side rendering with Python'''

import os


def generate_invitations(template, attendees):
    '''Generate invitations'''
    if not isinstance(template, str):
        print(f'template must be a string, got {type(template).__name__}')
        return
    if not template:
        print('Template is empty, no output files generated.')
        return

    if not isinstance(attendees, list) or \
        not all(isinstance(dict_attendee, dict)
                for dict_attendee in attendees):
        print(
            'attendees must be a list and '
            'with only dictionaries got {}'.format(type(attendees).__name__)
            )
        return
    if not attendees:
        print(f'No data provided, no output files generated.')
        return

    try:
        num = 1
        for attendee in attendees:
            mail = template
            keys = ['name', 'event_title', 'event_location', 'event_date']
            for key in keys:
                word = attendee.get(key, "N/A")
                mail = mail.replace(f'{{{key}}}',
                                    word if word
                                    is not None else f"{key}: N/A")

            if os.path.exists(f'output_{num}.txt'):
                print(f'output_{num}.txt already exists, skipping writting')
                continue

            with open(f'output_{num}.txt', 'w') as file:
                file.write(mail)
            print(f'output_{num}.txt created successfully.')

            num = num + 1

    except Exception as e:
        print(f'An error occured while writting output_{num}.txt: {e}')
