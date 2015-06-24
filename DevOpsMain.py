#!/usr/bin/Python

#Import classes from aws package
from aws import Connection
from aws import EC2Instance
from aws import Volumes
from aws import Security

connInst = Connection()
conn = connInst.ec2Connection()

'''
Uncomment code as required. Replace instance_id with actual values
'''
#Manage EC2 Instances
'''
instance = EC2Instance()
instance.list_instances(conn)
instance.start_instance(conn, instance_id)
instance.stop_instance(conn, instance_id)
'''

'''
Uncomment code as required. Replace instance_id and volume_id with actual values
'''
#Manage EBS Volumes
'''
volumeInst = Volumes()
volumeInst.list_volumes(conn)
volumeInst.detach_volume(conn,volume_id)
volumeInst.attach_volume(conn, volume_id, instance_id)
'''

#Manage Security Groups
'''
Uncomment code as required. Replace security_group_name, rule_type, ip_address with actual values
'''
'''
sgInst = Security()
sgInst.list_security_groups(conn)
sgInst.add_security_group(conn)
sgInst.revoke_security_rule(conn,security_group_name,rule_type,ip_address)
sgInst.remove_security_group(conn,security_group_name)
'''