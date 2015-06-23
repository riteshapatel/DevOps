#import EC2
import boto.ec2
import boto.vpc

class Connection:
	def __init__(self):
		''' Connection Constructor '''
		self.region = 'us-east-1'

	def ec2Connection(self):
		''' Create an EC2 Connection '''
		conn = boto.ec2.connect_to_region(self.region)
		return conn

	def vpcConnection(self):
		''' Create a VPC Connection '''
		vpc = boto.vpc.connect_to_region(self.region)
		return vpc