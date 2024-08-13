from pathlib import Path

base= Path.home()
#guide= Path(base, 'Paris', 'Eiffel_Tower.txt')
#guide= Path(base, 'Europe', 'France', Path('Paris', 'Eiffel_Tower.txt'))
#guide2= guide.with_name('Notre_Dam.txt')
#print(base)
#print(guide)
#print(guide2)
#print(guide.parent)
#print(guide.parent.parent)
#print(guide.parent.parent.parent)
#print(guide.parent.parent.parent.parent)





#guide= Path(Path.home(), 'Europe')
#for txt in Path(guide).glob('*.txt'):
    #print(txt)



guide3=Path('Europe', 'France', 'Paris', 'Eiffel_Tower.txt')

in_europe= guide3.relative_to(Path('Europe'))
in_france = guide3.relative_to(Path('Europe','France'))

print(in_europe)
print(in_france)