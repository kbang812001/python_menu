from os import system 
from subprocess import getstatusoutput
def docker():
	while True:
		system("clear")
		print("Docker Menu")
		print("\nPlease select an option: \n")
		print("1 : Install docker")
		print("2 : Start docker service")
		print("3 : Stop docker service")
		print("4 : View docker info")
		print("5 : View active containers")
		print("6 : View all containers")
		print("7 : View downloaded images")
		print("8 : Pull an image")
		print("9 : Launch a container")
		print("10 : Stop a container")
		print("11 : Start a container")
		print("12 : Remove an image")
		print("13 : Remove a container")
		print("0 : Exit")
		
		opt = input("Option selected: ")
		# Install Docker
		if opt == '1':
			system("clear")
			if not system("rpm -q docker-ce"):
				print("Docker is already installed. Exiting installation...")
				system("sleep 2")
				
			else:
				print("\tInstalling Docker...")
				
				f = open("/etc/yum.repos.d/docker-ce_install.repo","a")
				dockrepo = "[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0\n"
				f.write(dockrepo)
				f.close()
			system("yum install docker-ce --nobest")
			system("systemctl enable docker")
			system("systemctl start docker")
			system("sleep 2")
		# Start docker service
		elif opt == '2':
			system("clear")
			system("systemctl start docker")

		# Stop docker service
		elif opt == '3':
			system("clear")
			system("systemctl stop docker")

		# View docker info
		elif opt == '4':
			system("clear")
			cmd = "docker info | less"
			system(cmd)
			
		# View active containers
		elif opt == '5':
			system("clear")
			cmd = "docker ps | less"
			system(cmd)
			
		# View all containers
		elif opt == '6':
			system("clear")
			cmd = "docker ps -a | less"
			system(cmd)
			
		# View downloaded images
		elif opt == '7':
			system("clear")
			cmd = "docker images | less"
			system(cmd)
			
		# Pull an image
		elif opt == '8':
			system("clear")
			system("tput setaf 6")
			img = input("\n\tEnter image name: ")
			ver = input("\tEnter image version (optional): ")
			system("tput setaf 7")
			
			if img:
				cmd = f"docker pull {img}:{ver}" if ver != "" else f"docker pull {img}"
				system(cmd)
				system("sleep 2")
				break
			else:
				print("\n\tNo image name entered! Getting back to previous menu...\n")
				system("sleep 2")

		# Launch a container
		elif opt == '9':
			system("clear")
			flags = ""
			system("tput setaf 6")
			img = input("\tEnter image name: ")
			ver = input("\tEnter image version (optional): ")
			interact = input("\tInteractive (y/n): ")
			console = input("\tShell prompt (y/n): ")
			name = input("\tEnter container name (optional): ")
			system("tput setaf 7")
			
			if img:
				if interact or console:
					flags += '-'
					if interact.lower() in ['y','yes']: flags += 'i'
					if console.lower() in ['y','yes']: flags += 't'
				if name: flags += f" --name {name}"
			
				cmd = f"docker run {flags} {img}:{ver}" if ver else f"docker run {flags} {img}"
				system(cmd)
				
			else: print("\tPlease enter an image name!")
			system("sleep 2")
			
		# Stop a container
		elif opt == '10':
			system("clear")
			system("tput setaf 6")
			name_id = input("\tEnter container name or id: ")
			system("tput setaf 7")
			system(f"docker stop {name_id}") if name_id else print("\tPlease enter a container name/ID!")
			system("sleep 2")

		# Start a container
		elif opt == '11':
			system("clear")
			name_id = input("\tEnter container name or ID: ")
			system(f"docker start {name_id}") if name_id else print("\tPlease enter a container name/ID!")
			system("sleep 2")
			
		# Remove an image
		elif opt == '12':
			system("clear")
			flags,img = "",""
			system("tput setaf 6")
			img = input("\tEnter image name: ")
			ver = input("\tEnter image version (optional): ")
			force = input("\tForce remove (y/n): ")
			system("tput setaf 7")
			
			if force.lower() in ['y', 'yes']: flags += "--force"
			if img:
				cmd = (f"docker rmi {img}:{ver} {flags}" if ver != "" else f"docker rmi {img} {flags}")
				system(cmd)
			else:
				system("clear")
				print("\tPlease enter an image name!")
				
			system("sleep 2")
			
		# Remove a container
		elif opt == '13':
			system("clear")
			system("tput setaf 6")
			name_id = input("\tEnter container name or ID: ")
			system("tput setaf 7")
			system(f"docker rm {name_id}") if name_id else print("\tPlease enter a container name/ID!")
			system("sleep 2")

		# Previous menu	
		elif opt == '0':
			system("clear")
			break
			
		else:
			system("clear")
			print("\tPlease enter a valid option!\n")

#hadoop() function for hadoop setup
def hadoop():
	while True:
		print("Hadoop Commands")
		print("Please select one option: ")
		print("""1: Install Hadoop Requirements
2: Configure Name Node
3: Configure Data Node
4: Configure Hadoop Client
5: Upload Data To Hadoop Cluster
6: Read Client Data from Hadoop Cluster
7: Delete Client Data
8: Stop Name Node
9: Stop Data Node
0: Exit""")
		ch = input("Enter your choice : ") 
		if int(ch) == 1:
			system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
			system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force')
			print("Hadoop Requirements Sucessfully Installed In Name Node")

			ab = input("Enter Your Data Node IP :")
			system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(ab))
			system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(ab))
			print("Hadoop Requirements Sucessfully Installed In Data Node")

			bb = input("Enter Your Client Node IP :")
			system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(bb))
			system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(bb))
			print("Hadoop Requirements Sucessfully Installed In Client Node")

		   
		elif int(ch) == 2:
			dir = input("Enter your Name Node directory name : ")
			print("Configuring hdfs-site.xml file ............")
			system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
			system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
			system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
			system('echo -e "\n<property>" >> /root/hdfs-site.xml')
			system('echo -e "<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
			system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dir))
			system('echo -e "</property>" >> /root/hdfs-site.xml')
			system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
			system('rm -rf /etc/hadoop/hdfs-site.xml')
			system('cp  /root/hdfs-site.xml  /etc/hadoop')
			system('rm -rf /root/hdfs-site.xml')
			system('hadoop namenode -format')

			nip = input("Enter Name Node IP :")
			print("Configuring core-site.xml file ...........")
			system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
			system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
			system('echo -e "\n<configuration>" >> /root/core-site.xml')
			system('echo -e "\n<property>" >> /root/core-site.xml')
			system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
			system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
			system('echo -e "</property>" >> /root/core-site.xml')
			system('echo -e "\n</configuration>" >> /root/core-site.xml')
			system('rm -rf /etc/hadoop/core-site.xml')
			system('cp  /root/core-site.xml  /etc/hadoop')
			system('rm -rf /root/core-site.xml')
			print("Starting Hadoop Name Node Services")
			system('hadoop-daemon.sh start namenode') 
			system('jps')

		elif int(ch) == 3:
			dip = input("Enter Data Node IP : ")
			dio = input("Enter your Data Node directory name : ")
			print("Configuring hdfs-site.xml file ............")
			system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
			system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
			system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
			system('echo -e "\n<property>" >> /root/hdfs-site.xml')
			system('echo -e "<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
			system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dio))
			system('echo -e "</property>" >> /root/hdfs-site.xml')
			system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
			system('scp  /root/hdfs-site.xml  {}:/etc/hadoop'.format(dip))
			system('rm -rf /root/hdfs-site.xml')
			niq = input("Enter Name Node IP :")
			print("Configuring core-site.xml file ...........")
			system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
			system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
			system('echo -e "\n<configuration>" >> /root/core-site.xml')
			system('echo -e "\n<property>" >> /root/core-site.xml')
			system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
			system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(niq))
			system('echo -e "</property>" >> /root/core-site.xml')
			system('echo -e "\n</configuration>" >> /root/core-site.xml')
			system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(dip))
			system('rm -rf /root/core-site.xml')

			system('ssh {} hadoop-daemon.sh start datanode'.format(dip))
			system('ssh {} jps'.format(dip))
			system('ssh {} hadoop dfsadmin -report'.format(dip))

	      
		elif int(ch) == 4:
			nip = input("Enter Name Node IP : ")
			print("Configuring core-site.xml file ...........")
			ip = input("Enter Client IP : ")
			system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
			system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
			system('echo -e "\n<configuration>" >> /root/core-site.xml')
			system('echo -e "\n<property>" >> /root/core-site.xml')
			system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
			system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
			system('echo -e "</property>" >> /root/core-site.xml')
			system('echo -e "\n</configuration>" >> /root/core-site.xml')
			system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(ip))
			print("Hadoop Client Sucessfully Configured.........")

	       
	       
		elif int(ch) == 5:
			ci = input("Enter Client IP : ")
			filename = input("Enter The Name of File You want to upload on Hadoop Cluster : ")
			os.system('ssh {} hadoop fs -put {} /'.format(ci , filename))
			print("File Sucessfully Uploaded .......................")
			os.system('ssh {} hadoop fs -ls /'.format(ci))

		elif int(ch) == 6:
			cip = input("Enter Client IP : ")
			filename = input("Enter Your File Name : ")
			system('ssh {} hadoop fs -cat /{}'.format(cip ,filename))

		elif int(ch) == 7:
			cip = input("Enter Client IP : ")
			filename = input("Enter Your File Name : ")
			system('ssh {} hadoop fs -rm /{}'.format(cip , filename))
			print("Sucessfully Deleted File {} ".format(filename))
	       
		elif int(ch) == 8:
			system('hadoop-daemon.sh stop namenode')
			system('jps')

		elif int(ch) == 9:
			ip = input("Enter Data Node IP : ")
			system('ssh {} hadoop-daemon.sh stop datanode'.format(ip))
			system('ssh {} jps'.format(ip))
	       
		elif int(ch) == 0:
			break

		else:
			system("clear")
			print("\tPlease enter a valid option!\n")
	
 
def cli_check():
	print("checking requirements...")
	x = getstatusoutput("aws --version")
	if x[0] != 0 :
		print("AWS cli not installed on your system")
		print("please install aws cli")
		ch = input("press [y/n] = " )
		if ch == "y" or ch == "Y":
			system(" curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\"")
			system("unzip awscliv2.zip")
			system("sudo ./aws/install")
		else:
			print("aws cli is required to run aws commands")
			
	else:
		print("aws cli is installed on system..")
		print("Everything is okay!!")
		print("Configuring aws cli..")
		system("aws configure")

# aws() is a function for all the aws commands.
def aws():
	cli_check()
	if not getstatusoutput("aws --version"):
		while True:
			print("1. Create a key pair")
			print("2. Create a new aws instance")
			print("3. Start a aws instance")
			print("4. Describe ec2 instance")
			print("5. Create a EBS volume")
			print("6. Attach a EBS volume to ec2 instance")
			print("7. Create s3 bucket")
			print("8. Upload a file in bucket")
			print("9. Create a distribution in aws CloudFront")
			print("0. Exit")
			
			opt = (input("Enter Choice : "))
			if opt == '1' :
				key_name = input("Enter key name : ")
				system("aws ec2 create-key-pair --key-name " + key_name + " --output text > "+ key_name+".pem")

			elif opt == '2':
				imageId = "ami-052c08d70def0ac62"
				instancetype = "t2.micro"
				instance_count = "1"
				key_name = input("key-name : ")
				print("imageId = " + imageId + "\nInstance type = " + instancetype + "\nInstance count = " + instance_count)
				system("aws ec2 run-instances --image-id "+ imageId + " --instance-type " + instancetype + " --count " + instance_count + " --key-name " + key_name)

			elif opt == '3':
				instanceId = input("Enter instance id to start a instance : ")
				system("aws ec2 start-instances --instance-ids "+ instanceId)

			elif opt == '4':
				system("aws ec2 describe-instances")

			
			elif opt == '5':
				size = input("Enter size of ebs volume : ")
				region = input("Enter availability zone : ")
				system("aws ec2 create-volume --volume-type gp2 --size " + size + " --availability-zone " + region)

			elif opt == '6':
				volume_id = input("Enter Volume id of ebs storage : ")
				instance_id = input("Enter Instance id :")
				device = input("Enter device name[ex - /dev/sdf] : ")
				system("aws ec2 attach-volume --volume-id " + volume_id + " --instance-id " + instance_id + " --device " + device)
			
			elif opt == '7':
				bucket_name = input("Enter bucket name : ")
				regions3 = input("Enter region : ")
				system("aws s3api create-bucket --bucket " + bucket_name + " --region " + regions3)

			elif opt == '8':
				file_path = input("Enter file path[ex - c:\\users\\d\\desktop\\image.jpg] : ")
				bucket_name1 = input("Enter bucket name")
				filename = input("What should be the file name of your file in s3 bucket? :  ")

				system("aws s3 cp " + file_path + " s3://" + bucket_name1 + "/" + filename)
			
			elif opt == '9':
				domain_name = input("Enter a domain to create a distribution : ")
				system("aws cloudfront create-distribution --origin-domain-name " + domain_name)
			

			elif opt == '0':
				break
	else:
		print("Unable to run cli command.")


#python() function for basic python
def python():
	while True:
		system("clear")
		print("Python Commands")
		print("Please select an option: \n")
		print("1 : Date command")
		print("2 : Cal command")
		print("3 : Start Httpd service")
		print("4 : Reboot")
		print("5 : Ifconfig")
		print("0 : Exit")
		opt = input("Option selected: ")
		if opt == '0':
			break
		
		print("Where you want to run this command?")
		print("Press (l) for local execution and (r) for remote execution.")
		option = input("Enter your choice: ")
		if (option == 'l') or (option == 'L'):
			if opt == '1':
				system("date")
				system("sleep 2")

			elif opt == '2':
				system("cal")
				system("sleep 2")
			
			elif opt == '3':
				system("clear")
				system("yum install httpd")
				system("sleep 2")

			elif opt == '4':
				system("reboot")
				system("sleep 2")

			elif opt == '5':
				system("ifconfig")
				system("sleep 2")
				
			else:
				system("clear")
				print("\tPlease enter a valid option!\n")

		elif (option == 'r') or (option == 'R'):
			ip = input("Enter remote IP: ")
			user = input("Enter remote username: ")
			if opt == '1':
				system("ssh {} date".format(ip))

			elif opt == '2':
				system("ssh {} cal".format(ip))
			
			elif opt == '3':
				system("clear")
				system("ssh {}@{} yum install httpd".format(ip,user))
				system("sleep 2")

			elif opt == '4':
				system("ssh {} reboot".format(ip))

			elif opt == '5':
				system("ssh {} ifconfig".format(ip))
				
			else:
				system("clear")
				print("\tPlease enter a valid option!\n")

		else:
			print("Invalid choice.")


while True:
	print("Welcome User !!!!")
	print("Which Service do you want to use?")
	print("Press 1 for AWS CLI")
	print("Press 2 for Hadoop Service")
	print("Press 3 for Docker")
	print("Press 4 for LVM")
	print("Press 5 for Python Commands")
	print("Press 6 for exit")
	opt=input("\nOption selected:")
	if opt=='1':
		aws()
	elif opt=='2':
		hadoop()
	elif opt=='3':
		docker()
	elif opt=='5':
		python()	
	elif opt=='6':
		exit()
	else:
		pass

