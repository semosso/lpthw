from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}.')

# Zed: we could do these two on one line, how?
## maybe "indata = open(from_file).read()"? yep, exactly like that (p. 58)
in_file = open(from_file)
indata = in_file.read() # there's no need to copy (see ln 19)? read does it all? does it "store" data somewhere?

print(f'The input file is {len(indata)} bytes long.')

print(f'Does the output file exist? {exists(to_file)}')
print('Ready, hit RETURN to continue, CTRL-C to abort.')
input() # what does this do? what is inputed? oh, ok, it's just so I can either hit return or abort; could join ln 15 and 16, TBH

out_file = open(to_file, 'w')
out_file.write(indata)

print('Alright, all done.')

out_file.close()
in_file.close()