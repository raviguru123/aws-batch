#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3
import time
session = boto3.session.Session(region_name='us-east-1')
dynamodb = session.resource('dynamodb')

table = dynamodb.Table('TestTableNext')

filler = 'x' * 1000

i = 0
while i < 10:
    j = 0
    while j < 10:
        milliseconds = int(round(time.time() * 1000))
        print (milliseconds, j)

        table.put_item(Item={'pk': milliseconds, 'sk': j,
                       'filler': {'S': filler}})

        j += 1
    i += 1

