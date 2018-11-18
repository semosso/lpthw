# Excluindo o out_file, e reduzindo mais ainda
from sys import argv

script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}.')

indata = open(from_file).read()

open(to_file, 'w').write(indata)
to_file.close()
# why do I get an error in ln 11? "'str' object has no attribute 'close'"
## Stack Overflow: "the file descriptor you open with open(to_file) will be closed automatically; file sessions are closed after
## the file-objects exit the scope (in this case, immediately after .write())."
## Takai: to_file é uma string. voce abriu e nao guardou a referencia do arquivo aberto