# Answers to questions from "Linux for Bioinformatics"

**Q1. What is your home directory?**

A: /home/ubuntu

**Q2. What is the output of this command?**

A: 

```bash
ubuntu@ip-172-31-36-94:~/my_folder$ ls
hello_world.txt
```

**Q3. What is the output of each `ls` command?**

A:

```bash
ubuntu@ip-172-31-36-94:~$ ls my_folder
ubuntu@ip-172-31-36-94:~$ ls my_folder2
hello_world.txt
```

**Q4. What is the output of each?**

A:

```bash
ubuntu@ip-172-31-36-94:~$ ls my_folder
ubuntu@ip-172-31-36-94:~$ ls my_folder2
ubuntu@ip-172-31-36-94:~$ ls my_folder3
hello_world.txt
```

**Q5. Why didn't that work?**

A: Because the generated keys work for the user `ubuntu`. The ssh authentication is using the public key authentication method, so until the `sudouser` gets its own key pair generated, it can't be used for ssh login.

As stated in the hints, another less secure solution would be to use the ssh password-based authentication instead of the key-based one. 

 **Q6. What was the solution?**

Generating a key-pair on my local machine, and then pasting the public key in `/home/sudouser/authorized_keys`. Then, when connecting with `sudouser` I should simply specify which keypair to use. This is the `~/.ssh/config` I used for convenience (noting that the HostName field is to be updated every time the machine is stopped and started again.)

```
Host aws_bio_training
        User ubuntu
        IdentityFile ~/.ssh/GlamorousNut.pem
        HostName ec2-3-19-75-208.us-east-2.compute.amazonaws.com

Host aws_bio_training_sudo
        User sudouser
        IdentityFile ~/.ssh/aws_sudouser
        HostName ec2-3-19-75-208.us-east-2.compute.amazonaws.com

```

[2FA authentication](https://aws.amazon.com/blogs/startups/securing-ssh-to-amazon-ec2-linux-hosts/) setup was not attempted.