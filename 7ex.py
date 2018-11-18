print('Mary had a little lamb.')
print('Its fleece was white as {}.'.format('snow')) # not actually calling a variable, just inserting a string within {}
print('And everywhere that Mary went.')
print('.' * 10) # what did that do?
# prints tem times the "."

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# watch end = '' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') # every print ends with a \n; END tells it otherwise
print(end7 + end8 + end9 + end10 + end11 + end12)