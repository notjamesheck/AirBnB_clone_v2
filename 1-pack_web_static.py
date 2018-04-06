#!/usr/bin/python3
'''
    this is the comment
'''

from fabric.api import *
import time
import datetime
import os


def do_pack():
    '''
    '''
    theTime = datetime.datetime.now().strftime('%y%m%d%H%M%S')
    local('mkdir versions')
    theFile = 'versions/web_state_'
    try:
        '''
        '''
        local('tar -cvzf {}{}.tgz /data/web_static'.format(theFile, theTime))
        return '{}{}.tgz'.format(theFile, theTime)

    except:
        '''
        '''
        return None
