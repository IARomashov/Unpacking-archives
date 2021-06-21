
# Потоковые распаковщики для TAR.* архивов.
 
Этот проект для ускорения процесса распаковки огромного количества архивов.  
"unpack_all" и "unpacker" используют потоки для быстрой распаковки архивов TAR.

## "unpacker"
Найдет и распакует нужные файлы, соответствующие шаблону регулярного выражения
из всех архивов, которые хранятся в указанном каталоге
в каталог, который вы указываете для распаковки. Если вы не укажете свой
шаблон регулярного выражения, тогда все файлы из всех архивов будут распакованы. Также 
вы можете указать сколько потоков хотите использовать.

## Help "unpacker"
см. список настраиваемых переменных: `python unpacker.py --help`

##### Используйте настраиваемые аргументы для ввода нужных данных:

```shell
'-a', '--address', action="store", help="the address of the folder containing the archives"
'-au', '--address_unpack', action="store", help="the address where the archives will be unpacked"
"-t", "--thread", action="store", type=int, help="number of threads used, default 1"
"-p", "--pattern", action="store", help="your sample regex template, by default will unpack everything"
```
##### пример:
```shell
python unpacker.py -a "/home/vango/archives/" --address_unpack "/home/vango/unpack/" -t 10 -p "прп"
```

## "unpack_all"
Распаковывает все файлы из архивов в указанном
каталоге в каталог, который вы указали для распаковки. Также 
вы можете указать сколько потоков хотите использовать.

## Help "unpack_all"
см. список настраиваемых переменных: `python unpack_all.py --help`

##### Используйте настраиваемые аргументы для ввода нужных данных:
```shell
'-a', '--address', action="store", help="the address of the folder containing the archives"
'-au', '--address_unpack', action="store", help="the address where the archives will be unpacked"
"-t", "--thread", action="store", type=int, help="number of threads used, default 1"
```
##### пример:
```shell
python unpack_all.py -a "/home/vango/archives/" --address_unpack "/home/vango/unpack/" --thread 10
```
