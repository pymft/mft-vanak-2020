* `pwd` : present working directory
* `cd` : change directory
    * `cd ~` : go to home
    * `cd /` : go to root
    * `cd ..` : go to home
    
    
* ssh stuff
    * **generate key**
```bash
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/User/.ssh/id_rsa):
Created directory '/c/Users/User/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/User/.ssh/id_rsa.
Your public key has been saved in /c/Users/User/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:Qwvj8fgh62YS1PsbdK2u4wcZdDC3bllCS10X9P/HDFk Teacher-204@Teacher-204
The key's randomart image is:
+---[RSA 2048]----+
|        o.+. .ooo|
        ...
|    ..o oo.     .|
|     +..+=.      |
+----[SHA256]-----+
```

    * get public key
```bash 
$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3Nz ... very long string. ..HjQB94B Teacher-204@Teacher-204

``` 

    * add identity
```bash
$ ssh-agent bash
$ ssh-add ~/.ssh/id_rsa 
```