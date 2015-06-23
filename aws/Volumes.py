import boto.ec2

class Volumes:
	def __init__(self):
		''' Volumes Constructor '''

	def list_volumes(self,conn):
		''' Lists Volumes from an AWS account '''
		vols = conn.get_all_volumes()
		i=0
		if vols:
			for v in vols:
				print 'Volume Id:', v.id
				print 'Volume Status:', v.status
				print 'Volume Size:', v.size
				print 'Zone:', v.zone 
				print 'Volume Type:', v.type 
				print 'Encrypted:', v.encrypted

				#print volume dictionary
				#print v.__dict__

				#print attachment set object
				attachmentData = v.attach_data
				print 'Instance Id:', attachmentData.instance_id
				print 'Attached Time:', attachmentData.attach_time
				print 'Device:', attachmentData.device
				print '**********************************'
				i = i + 1

				if i > 5:
					break

	def detach_volume(self,conn,volume_id):
		''' Detaches a specific volume '''
		#get a specific volume to be detached
		vols = conn.get_all_volumes(volume_id)
		#if volume found
		if vols:
			#retrieve only volume from the list
			volume = vols[0]
			#if volume status is in-use then proceed with detaching the volume
			if (volume.status == 'in-use'):
				#detach the volume
				isdetached = volume.detach()
				#print message
				if isdetached:
					print 'Volume ', volume_id, ' detached successfully!'
				else:
					print 'Error detaching volume ', volume_id
			else:
				print 'Volume has already been detached'

	def attach_volume(self,conn,volume_id,instance_id):
		''' Attaches volue to an EC2 instance '''

		#get a specific volume to be attached
		vols = conn.get_all_volumes(volume_id)
		if vols:
			#print volume status
			volume = vols[0]
			if (volume.status == 'available'):
				isattached = volume.attach(instance_id,'/dev/xvdh')
				if isattached:
					print 'Volume ', volume_id, ' attached successfully to instance ', instance_id
				else:
					print 'Error attaching volume ', volume_id, ' to instnace ', instance_id
				
			else:
				print 'Volume is in-use'	
