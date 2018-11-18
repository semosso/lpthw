# SD 

from sys import argv; from os.path import exists

script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}.')

indata = open(from_file).read()

print(f'The input file is {len(indata)} bytes long. Does the output file exist? {exists(to_file)}')

out_file = open(to_file, 'w') # SD 4 related: why have out_file at all? see 17duvidas.py
out_file.write(indata) 

print(type(out_file))
# SD 4, Zed: find out why you had to write this
## why not "to_file.close()"? Takai: to_file é só uma string que foi inputada, não é um objeto tipo file
### to_file é uma string. voce abriu e nao guardou a referencia do arquivo aberto
### open(to_file) funciona porque é o PATH do arquivo, não o ARQUIVO itself
## as per ln 13, why have out_file at all?
### no need, see 17duvidas.py