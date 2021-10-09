# Emerton Q&A Test

### Description
A program that counts unique words from an English text file, treating hyphen and apostrophe as part of the word. 
The program must output the ten most frequent words and mention the number of occurrences. 

The expected output is (using `Temptest.txt` file as input`: \
and (514) \
the (513) \
i (446) \
to (324) \
a (310) \
of (295) \
my (288) \
you (211) \
that (188) \
this (185) 


### Environment
This program been tested on **Windows 10** and **Ubuntu 18.04 LTS** operating systems.
- The running time environment are python 3.9.2 on Windows 10, Python 3.6.2 on Ubuntu.
- The used libraries with Python runtime environment: itertools, re, argparse. all standard libraries, so it should run without need to install them.


### Run the program 
From the CLi run the command and provide the path to:
- input file. e.g. `./here/the/path/to/Tempest.txt`.
- output file. e.g. `./here/is/the/path/to/result.txt`.

The path should be correct thus the directories and file existed and have permission to read and write to.

Example on **Linux**:
```terminal
python3 main.py --input ./Tempest.txt --ouput result.txt
```
Or you can sue the code below

```terminal
python3 main.py -i ./Tempest.txt -o result.txt
```

<br>

Example on **Windows 10**
```terminal
python main.py --input ./Tempest.txt --output result.txt
```
Or you can use the code below 
```terminal
python main.py -i ./Tempest.txt -o result.txt
```

#### Author: Sqoor