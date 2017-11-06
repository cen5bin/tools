#!/usr/bin/env python
#coding=utf-8
import os
import sys
import re

root = os.path.dirname(os.path.realpath(__file__))

machine_list_file = os.path.join(root, 'machine.list')
if not os.path.exists(machine_list_file):
    os.system('cp %s %s' % (os.path.join(root, 'machine.list.example'), machine_list_file))
    os.system('vim %s' % (os.path.join(root, 'machine.list.example')))

f = open(os.path.join(root, machine_list_file))
machines = [x.strip(' \r\n') for x in f.readlines()]
machines = [x for x in machines if len(x) > 8 and x[0] != '#' and len(re.split('\s*', x)) >= 2]
f.close()

if len(sys.argv) > 1:
    if sys.argv[1] == 'config' or sys.argv[1] == 'c':
        os.system("vim %s" % machine_list_file)
    elif sys.argv[1] == 'help' or sys.argv[1] == '-h':
        print 'qssh.py: run qssh'
        print 'qssh.py c: config'
else:
    try:
        print '%s%s%s' % ('-' * 20, 'machine list', '-' * 20)
        print ''
        for i in xrange(1, len(machines) + 1):
            print '    [%d] %s' % (i, machines[i-1])

        print ''
        print '-' * 52

        x = int(raw_input('input id: '))
        if x < 1 or x > len(machines):
            print 'id not in valid range'
            exit()

        ip = machines[x-1].split()[0]
        if '@' in ip:
            os.system('ssh %s' % ip)
        else:
            os.system("ssh wubin.cwb@%s" % ip)
    except KeyboardInterrupt:
        print ''
        print 'Bye!'
    except ValueError:
        print 'value error'
        print 'Bye!'
