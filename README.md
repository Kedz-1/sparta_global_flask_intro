# EC2 Instance + Flask

## Setup for EC2 instance (console)
1. Go to AWS console and search EC2
2. Create an instance, giving it a unique name
3. Choose the image i.e Ubuntu and setup accordingly, RAM requirements etc
4. Set up key pair (see below for more detail)
5. Confirm secuirty group details


## Set up key/pair
1. Create key pair on AWS through the EC2 instance and download it
2. Using the terminal move the file to .ssh

    `mv /Downloads/...pem .ssh`
3. Make sure it's not publically readable

    `chmod 400 "khadar-***-.pem"`
4. Connect to it 

    `ssh -i "khadar-***.pem" ubuntu@***.eu-*-*.compute.amazonaws.com` 

## Set up environment
1. sudo apt update
2. sudo apt upgrade
3. sudo apt install python3.14-venv
4. python3 venv venv
5. source venv/bin/activate 

## Clone repository 

1. Go to github and get repository ensuring it's public - otherwise steps differ if repo is private.
2. git clone *repo*
3. cd *repo*

