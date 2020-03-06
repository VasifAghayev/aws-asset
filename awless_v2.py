import tablib
import subprocess

region = input('Enter the name of amazon region: ').strip()
profile = input('Enter the name of aws profile: ').strip()

out_format = 'csv'

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
	'route53':['zones', 'records'],
	'lambd':['functions'],
	'cloudwatch':['alarms'],
	'acm':['certificates']
}

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


