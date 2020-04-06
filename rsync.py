#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

rsin = '/home/pnm/src/script/exch/'
rsout = '/home/usersrssh/src'

vps = {'hrbpart': '194.67.208.25', 'izko18': '194.67.213.148', 'alt':'194.67.200.122', 'amalgama': '185.5.249.195',\
       'spectrans': '194.67.193.3', 'egorov': '193.124.191.251', 'diana':'193.124.188.152', 'cherni':'185.5.251.4', \
       'avtoboss':'194.67.207.224', 'aperm':'94.142.140.194', 'gertek':'193.124.189.65', 'kcrezon':'193.124.191.44',\
       'konstr':'193.124.185.206','kotly':'194.67.217.185', 'kst':'193.124.181.74', 'lid':'185.117.155.152',
       'mozgabeton':'185.238.139.198', 'msk':'185.238.138.96', 'ooolidtorg':'194.67.211.92', 'promtech':'185.117.153.97',\
       'shibanov':'94.142.140.37', 'smu7':'194.67.208.70', 'nikagro':'193.124.176.113', 'special':'194.67.217.247',\
       'strdepo':'185.125.217.215', 'stek':'185.125.217.133', 'su4':'194.67.217.167', 'sysizol':'193.124.180.122',\
       'technoserv':'194.67.205.33', 'tios':'185.58.206.202', 'stroydom':'193.124.182.102', 'grata':'194.67.196.216',\
       'patrakeeva':'94.142.138.161', 'strtemp':'193.124.179.192', 'energipk':'185.238.138.220', 'oniks':'94.142.140.110',\
        }

for i in vps.values():
    print(i)
    os.system('rsync -az  '+ rsin +'  usersrssh@' + i + ':' + rsout + '')