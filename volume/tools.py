__author__ = 'feng'

from paramiko import SSHClient
from scp import SCPClient
import psycopg2
import sys
import datetime
from dateutil.relativedelta import  relativedelta
from volume.models import server, volume, process




def get_month_day_range(date):
    first_day = date + relativedelta(day=1)
    last_day = date + relativedelta(day=1, months=+1, days=-1)
    return first_day, last_day

def get_rawdata(server, month, tmpfile):
    serv = server.objects.get(name=server)
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(serv.ipaddress, username=serv.username, password=serv.password)
    client = SCPClient(ssh.get_transport())
    client.get(serv.path + '/volume.' + month+ '.csv', tmpfile)

def process_data(server, date):
    if not volume.objects.filter(server=server).filter(date=date).exist():
        tmpfile = '/tmp/volume.log'
        get_rawdata(server, date.strftime("%Y%m"), tmpfile)
        with open(tmpfile) as f:
            for line in f:
                line = line.strip()
                fs = line.split(',')
                v = volume()
                v.server  = server
                v.date = datetime.date(fs[0])
                v.time = datetime.time(fs[1])
                v.side = fs[2]
                v.symbol = fs[3]
                v.bank = fs[4]
                v.size = int(fs[5])
                v.price = float(fs[6])
                v.termsize = float(fs[7])
                v.save()
        p = process()
        p.server = server
        p.date = date
        p.save()