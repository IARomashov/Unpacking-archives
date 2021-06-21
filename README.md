
# Threaded unpackers for TAR.* archives.

This project is designed to quickly unpack a huge number of archives.  
"unpack_all" and "unpacker" use threads to quickly unpack TAR archives.

## "unpacker"
Will find and unpack the required file matching the regular expression pattern 
from all the archives that are stored in the specified directory 
into the directory, you specify for unpacking. If you do not specify your 
regular expression pattern, then all files will be unpacked. 
You can specify the number of threads you want.

## Help "unpacker"
see the list of configurable variables: `python unpacker.py --help`

#### Use optional arguments to enter the data you want:
```shell
'-a', '--address', action="store", help="the address of the folder containing the archives"
'-au', '--address_unpack', action="store", help="the address where the archives will be unpacked"
"-t", "--thread", action="store", type=int, help="number of threads used, default 1"
"-p", "--pattern", action="store", help="your sample regex template, by default will unpack everything"
```
#### example:
```shell
python unpacker.py -a "/home/vango/archives/" --address_unpack "/home/vango/unpack/" -t 10 -p "прп"
```

## "unpack_all"
Unpacks all files from archives in the specified 
directory to the directory you specified for unpacking. 
You can specify the number of threads you want.

## Help "unpack_all"
see the list of configurable variables `python unpack_all.py --help`

#### use optional arguments to enter the data you want:
```shell
'-a', '--address', action="store", help="the address of the folder containing the archives"
'-au', '--address_unpack', action="store", help="the address where the archives will be unpacked"
"-t", "--thread", action="store", type=int, help="number of threads used, default 1"
```
#### example:
```shell
python unpack_all.py -a "/home/vango/archives/" --address_unpack "/home/vango/unpack/" --thread 10
```
