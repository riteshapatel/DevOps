import boto.ec2

class Security:
	def __init__(self):
		''' Security Constructor '''

	def list_security_groups(self,conn):
		''' Lists Security Groups '''
		groups = conn.get_all_security_groups()
		if groups:
			for g in groups:
				print 'Group Name: ', g.name
				print 'Description: ', g.description 
				print 'VPC Id: ', g.vpc_id

				rules = g.rules
				i = 0
				if rules:
					ruleStr = ""
					for r in range(len(rules)):

						protocol = rules[r].ip_protocol
						from_port = rules[r].from_port
						to_port = rules[r].to_port
						grants = rules[r].grants

						if r == 0:
							ruleStr = ""
						else:
							ruleStr = ruleStr + '\n'

						if protocol:
							ruleStr = ruleStr + 'Protocol: ' + protocol
						if from_port:
							ruleStr = ruleStr + ' | From Port: ' + from_port
						if to_port:
							ruleStr = ruleStr + ' | To Port: ' + to_port
						if grants:
							ruleStr = ruleStr + ' | Grants: ' + str(grants).strip('[]')

						print ruleStr
						print '****************************************'
						i = i + 1
						if i > 5:
							break

	def add_security_group(self,conn):
		''' Creates a new Security Group '''

		#create a database security group
		dbsg = conn.create_security_group('RAP-DB-SG','Database Security Group')

		if dbsg:
			#add an ingress rule for Oracle
			dbsg.authorize('tcp','1521','1521','68.255.14.150/32')

			#add an ingress rule for SQL Server
			dbsg.authorize('tcp','1433','1433','68.255.14.150/32')
			dbsg.authorize('udp','1434','1434','68.255.14.150/32')


	def revoke_security_rule(self,conn,sgname,ruletype,ip):
		''' Revoke a security rule '''

		#get a specific security group
		grp = conn.get_all_security_groups(sgname)

		#revoke a rule from the security group
		if grp:
			for g in grp:
				if ruletype == 'oracle':
					g.revoke('tcp',1521,1521,ip)


	def remove_security_group(self,conn,sgname):
		''' Remove a security group '''

		grp = conn.get_all_security_groups(sgname)

		if grp:
			for g in grp:
				g.delete()















