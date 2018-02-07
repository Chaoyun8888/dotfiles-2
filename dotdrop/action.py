"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2017, deadc0de6
Represent an action in dotdrop
"""

import subprocess

# local imports
from dotdrop.logger import Logger


class Action:

    def __init__(self, key, action):
        self.key = key
        self.action = action
        self.log = Logger()

    def execute(self):
        self.log.sub('executing \"%s\"' % (self.action))
        try:
            subprocess.call(self.action, shell=True)
        except KeyboardInterrupt:
            self.log.warn('action interrupted')

    def transform(self, arg0, arg1):
        '''execute transformation with {0} and {1}
        where {0} is the file to transform and
        {1} is the result file'''
        cmd = self.action.format(arg0, arg1)
        self.log.sub('transforming with \"%s\"' % (cmd))
        try:
            subprocess.call(cmd, shell=True)
        except KeyboardInterrupt:
            self.log.warn('action interrupted')
        return arg1

    def __str__(self):
        return 'key:%s -> \"%s\"' % (self.key, self.action)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.key) ^ hash(self.action)
