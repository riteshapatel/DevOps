#import EC2
import boto.ec2
import time

class EC2Instance:
	def __init__(self):
		''' EC2Instance Constructor '''
	
	def check_instance(self,conn):
		self.instance_id = 'i-f587655c'
		reservations = conn.get_all_instances(filters={'instance-id':self.instance_id})
		if(reservations):
			instance = reservations[0].instances[0]
			if(instance and instance.state == 'running' and instance.id == self.instance_id):
				self.stop_instance(conn,instance.id)
			else:
				self.start_instance(conn,instance.id)	

	def stop_instance(self,conn,instance_id):
		''' Stops an instance '''
		reservations = conn.get_all_instances(filters={'instance-id':instance_id})
		if(reservations):
			instance = reservations[0].instances[0]
			if(instance and instance.state == 'running' and instance.id == instance_id):
				instance.stop()
				print 'Attempting to stop instance...', instance.id
				while not instance.update() == 'stopped':
					time.sleep(10)
				print 'Instance is ', instance.state, ' now!'


	def start_instance(self,conn,instance_id):
		''' Starts an instance '''
		
		reservations = conn.get_all_instances(filters={'instance-id':instance_id})
		if(reservations):
			instance = reservations[0].instances[0]
			print 'Attempting to start ', instance.id
			if(instance and instance.state == 'stopped' and instance.id == instance_id):
				instance.start()
				while not instance.update() == 'running':
						time.sleep(10)
				print 'Instance is ', instance.state, ' now!'

	def create_instance(self,conn):
		''' Creates an EC2 instance '''
		'''
			vpc vpc-c65a29a3
			subnet subnet-2805db03
			instance type t2.micro
			root device type ebs
			root device /dev/xvda
			block devices /dev/xvda
			availability zone us-east-1a
			security groups launch-wizard-4
			ami id amzn-ami-hvm-2015.03.0.x86_64-gp2 (ami-1ecae776)
			key-pair rpatel-kp
			termination protection FALSE
			monitoring basic
			
		'''


	def list_instances(self,conn):
		''' Print EC2 Instances '''

		# get all instance reservations with your account
		reservations = conn.get_all_reservations()

		# print instance metadata (dictionary)
		for r in reservations:
			# get instances
			instances = r.instances
			for i in instances:
				#print i.__dict__

				#get instance name from tags
				tags = i.tags
				instanceName = 'Default'
				if 'Name' in tags:
						instanceName = tags['Name']
				# extract fields to your heart's desire
				#instance id
				print 'Instance Name:', instanceName, ' Id:', i.id, ' Instance Type: ', i.instance_type, ' State:', i.state

				#get volumes attached to the instance
				volumes = conn.get_all_volumes(filters={'attachment.instance_id':i.id})

				#print volumes
				volumestr = ''
				if volumes:
					for v in range(len(volumes)):

						volumestr = volumestr + '\n'

						device = volumes[v].attach_data.device
						attachStatus = volumes[v].attach_data.status
						encrypted = volumes[v].encrypted
						
						volumetype = volumes[v].type
						size = volumes[v].size

						if device:
							volumestr = volumestr + 'Device: ' + device
						if volumetype:
							volumestr = volumestr + ' | Type: ' + volumetype
						if size:
							volumestr = volumestr + ' | Size: ' + str(size)
						if attachStatus == 'attached':
							volumestr = volumestr + ' | Encrypted: TRUE' if encrypted else volumestr + ' | Encrypted: FALSE'
						print volumestr
