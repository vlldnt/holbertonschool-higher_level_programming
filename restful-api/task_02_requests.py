#!/usr/bin/python3
'''
Requests to send http requests to the server, parse and manipulate
the response JSON data.
Convert into other format like CSV
'''

import requests
import csv


def fetch_and_print_posts():
    '''
    Fetch posts from server and print them
    '''
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(req.status_code))
    if req.status_code == 200:
        post = req.json()
        for element in post:
            print(element['title'])


def fetch_and_save_posts():
    '''
    Fetch posts from server and save them in CSV format
    '''
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    json = req.json()
    filednames = ["id", "title", "body"]

    if req.status_code == 200:
        with open('posts.csv', 'w', encoding='utf-8') as csv_file:
            new_csv = csv.DictWriter(csv_file, fieldnames=filednames)
            new_csv .writeheader()

            fetch_titles = [{"id": value['id'],
                             'title': value['title'],
                             'body': value['body']} for value in json]

            new_csv.writerows(fetch_titles)
