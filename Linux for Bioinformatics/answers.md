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

**Q7. what does the `sudo docker run` part of the command do? and what does the `salmon swim` part of the command do?**

A: Based on [this documentation](https://docs.docker.com/get-started/overview/), the `sudo docker run`  part creates a container and loads the `combinelab/salmon` image in it to execute the command `salmon swim`. This can be confirmed by executing `sudo docker ps -a`, which gives the following output.

```bash
sudouser@ip-172-31-36-94:~$ sudo docker ps -a
CONTAINER ID   IMAGE               COMMAND         CREATED          STATUS                      PORTS     NAMES
81ff756bac35   combinelab/salmon   "salmon -h"     5 minutes ago    Exited (0) 5 minutes ago              festive_jang
c7710b0b2d74   combinelab/salmon   "salmon swim"   7 minutes ago    Exited (0) 7 minutes ago              silly_cori
1a169e8e715a   hello-world         "/hello"        24 minutes ago   Exited (0) 24 minutes ago             competent_mendel
```

These are all of the containers created. Each `run` command created a separate container. Docker doesn't delete any of them unless told so, so here we have the trace.

According the to the `salmon -h` command, `salmon swim` performs a super-secret operation! Out of curiosity, [Salmon.cpp](https://github.com/COMBINE-lab/salmon/blob/master/src/Salmon.cpp), lines 93-106.

**Q8. What is the output of this command?**

A:

```
serveruser@ip-172-31-36-94:~$ sudo ls /root
[sudo] password for serveruser:
serveruser is not in the sudoers file.  This incident will be reported.
```

**Q9. what does `-c bioconda` do?**

A: It tells conda to look for the package in the "channel" called bioconda.

**Q10. What does the `-o athal.ga.gz` part of the command do?**

A: It specifies the output file name for curl. If it was not specified, and if I'm not mistaken, curl would write to stdout instead of a file.

**Q11. What is a `.gz` file?**

A: It is a gzip compressed file

**Q12. What does the `zcat` command do?**

A: From the `man` page of `gzip`: 

> `zcat` uncompresses either a list of files on the command line or  its  standard  input  and writes  the uncompressed data on standard output. `zcat` will uncompress files that have the correct magic number whether they have a `.gz` suffix or not.

**Q13. what does the `head` command do?**

A: It prints out the `x` first lines of its input. The default value for `x` is  lines. It has CLI options that alter its basic functioning (number of bytes instead of lines, change the number of bytes/lines...)

**Q14. what does the number `100` signify in the command?**

A: First 100 lines of the input to `head`, to be printed.

**Q15. What is `|` doing?**

A: This is a pipe, and it redirects the left hand side command's standard output (`stdout`) to the right hand side command's standard input (`stdin`). This design option showcases certain aspects of the [UNIX Tools Philosophy](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/c1089.htm).

**Q16. What format are the downloaded sequencing reads in?**

A: It's in compressed SRA format. (`.sra`)

**Q17. What is the total size of the disk?**

A: 7.7 GB

**Q18. How much space is remaining on the disk?**

2.4 GB (I had deleted the .gz file after I decompressed it for indexing)

**Q19. What went wrong?**

A: Storage exhausted while writing file within file system module

 **Q20: What was your solution?** 

I gzipped the `.fa` file to save more space, and then I used the `--gzip` option when executing the `fastq-dump` command. There are still 1.6 GB free after the success of the command.

