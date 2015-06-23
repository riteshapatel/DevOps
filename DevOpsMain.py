#!/usr/bin/Python

#Import classes from aws package
from aws import Connection
from aws import EC2Instance
from aws import Volumes
from aws import Security

connInst = Connection()
conn = connInst.ec2Connection()


#Manage EC2 Instances
'''
instance = EC2Instance()
instance.list_instances(conn)
instance.start_instance(conn, instance_id)
instance.stop_instance(conn, instance_id)
'''

#Manage EBS Volumes
'''
volumeInst = Volumes()
volumeInst.list_volumes(conn)
volumeInst.detach_volume(conn,volume_id)
volumeInst.attach_volume(conn, volume_id, instance_id)
'''

#Manage Security Groups
sgInst = Security()
#sgInst.list_security_groups(conn)
#sgInst.add_security_group(conn)
#sgInst.revoke_security_rule(conn,'RAP-DB-SG','oracle','68.255.14.150/32')
sgInst.remove_security_group(conn,'RAP-DB-SG')