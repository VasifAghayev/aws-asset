import tablib
import subprocess

profile = input('Enter the name of aws profile: ').strip()

out_format = 'csv'

regions = [
         'us-east-2', 
         'us-east-1', 
         'us-west-1', 
         'us-west-2', 
         'ap-south-1', 
         'ap-northeast-2', 
         'ap-southeast-1', 
         'ap-southeast-2', 
         'ap-northeast-1', 
         'ca-central-1', 
         'eu-central-1', 
         'eu-west-1', 
         'eu-west-2', 
         'eu-west-3', 
         'eu-north-1', 
         'sa-east-1'
        ]
awless_commands = {
	'vpc':['availabilityzones', 'vpcs', 'internetgateways', 'elasticips', 'natgateways', 'subnets', 'routetables'],
	'ec2':['instances', 'images', 'keypairs', 'networkinterfaces', 'securitygroups', 'volumes','snapshots'],
	'ecs':['containerclusters', 'containerinstances', 'containers', 'containertasks'],
	'ecr':['repositories'],
	'rds':['databases', 'dbsubnetgroups'],
	'asg':['scalinggroups', 'launchconfigurations', 'scalingpolicies'],
	'alb':['loadbalancers', 'targetgroups'],
	'iam':['groups', 'users', 'accesskeys', 'mfadevices', 'roles', 'policies', 'instanceprofiles'],
	's3':['buckets', 's3objects'],
	'sns':['subscriptions'],
        'sqs':['queues'],
        'cdn':['distributions'],
	'route53':['zones', 'records'],
	'lambd':['functions'],
        'cloudformation':['stacks'],
	'cloudwatch':['alarms', 'metrics'],
	'acm':['certificates']
}

for region in regions:
	l = []
	for service, command in awless_commands.items():
		for i in range(len(command)):
			with open(f'{service}_{command[i]}.csv', 'w') as f:
				subprocess.run(['awless', 'list', command[i], '-p', profile, '-r', region, '--format', out_format], check=True, universal_newlines=True, stdout=f)
			data = tablib.Dataset(title=f'{service}_{command[i]}').load(open(f'{service}_{command[i]}.csv').read())
			l.append(data)

	book = tablib.Databook(l)
	with open(f'{profile}_{region}.xlsx', 'wb') as f:
			f.write(book.xlsx)


