#!/bin/env python
from paramiko import SSHClient
from scp import SCPClient
import psycopg2
import sys

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "usage: python fetchvolume.py servername month"
		exit(1)
	servername = sys.argv[1]
	month = sys.argv[2]
	volf = '/tmp/volume.log'

	conn = psycopg2.connect("dbname=mysite user=flextrade")
	cur = conn.cursor()
	sqllan = r"SELECT * from volume_server where name= '" + servername + r"'"
	cur.execute(sqllan)
	res=cur.fetchone()
	print res
	cur.close()
	conn.close()

	if res:
		ssh = SSHClient()
		ssh.load_system_host_keys()
		ssh.connect(res[2], username=res[3], password=res[4])
		client = SCPClient(ssh.get_transport())
		client.get(res[5] + '/volume.' + month+ '.csv', volf)
		conn = psycopg2.connect("dbname=mysite user=flextrade")
		cur = conn.cursor()
		with open(volf) as f:
			for line in f:
				line = line.strip()
				fs = line.split(',')
				fs.append(servername)
				datestr = fs[0]
				fs[0] = datestr[0:4] + '-' + datestr[4:6] + '-' + datestr[6:8]
				print fs
				cur.execute("INSERT INTO volume_volume VALUES(%s %s %s %s %s %s %s %s %s %s)", fs)
		cur.close()
		conn.close()
	else:
		print "can not fetch server information for ", servername 




