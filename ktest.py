import matplotlib.pyplot as plt
file=open('Yeast.fasta')
file.readline()
data=""
while True:
	temp=file.readline()
	data+=temp[:-1]
	if temp=="":
		break
cp ={'A':'U', 'C':'G', 'G':'C', 'T':'A'}
bp = ('u','c','a','g')
rp=""
amine={
	'Phenylalanine':(('U','U','C'),('U','U','U')),
	'Leucine':(('U','U','A'),('U','U','G'),('C','U','U'),('C','U','A'),('C','U','G'),('C','U','C')), 
	'Isoleucine':(('A','U','C'),('A','U','A'),('A','U','U')), 
	'Methionine':(('A','U','G'),('A','U','G')),
	'Valine':(('G','U','U'),('G','U','A'),('G','U','C'),('G','U','G')), 
	'Serine':(('U','C','U'),('U','C','A'),('U','C','G'),('U','C','C'),('A','G','U'),('A','G','C')), 
	'Pruline':(('C','C','U'),('C','C','A'),('C','C','G'),('C','C','C')), 
	'Threonine':(('A','C','U'),('A','C','A'),('A','C','G'),('A','C','C')), 
	'Alanine':(('G','C','U'),('G','C','A'),('G','C','G'),('G','C','C')), 
	'Tyrosine':(('U','A','U'),('U','A','C')), 
	'Stop':(('U','A','G'),('U','A','A'),('U','G','A')),
	'Histidine':(('C','A','U'),('C','A','C')),
	'Glutamine':(('C','A','A'),('C','A','G')),
	'Asparagine':(('A','A','U'),('A','A','C')),
	'Lysine':(('A','A','A'),('A','A','G')),
	'Aspartic Acid':(('G','A','U'),('G','A','C')),
	'Glutamic Acid':(('G','A','A'),('G','A','G')),
	'Cysteine':(('U','G','U'),('U','G','C')),
	'Tryptophan':(('U','G','G'),('U','G','G')),
	'Arginine':(('C','G','U'),('C','G','C'),('C','G','A'),('C','G','G'),('A','G','A'),('A','G','G')),
	'Glycine':(('G','G','U'),('G','G','C'),('G','G','A'),('G','G','G'))
}
count={}
for x in amine:
	count[x]=0
for i in data:
	for bp in i:
		if bp not in cp:
			rp+=bp
		else:
			rp+=cp[bp]
print(rp)
def trna(bp):
	amine={
	'Phenylalanine':(('U','U','C'),('U','U','U')),
	'Leucine':(('U','U','A'),('U','U','G'),('C','U','U'),('C','U','A'),('C','U','G'),('C','U','C')), 
	'Isoleucine':(('A','U','C'),('A','U','A'),('A','U','U')), 
	'Methionine':(('A','U','G'),('A','U','G')),
	'Valine':(('G','U','U'),('G','U','A'),('G','U','C'),('G','U','G')), 
	'Serine':(('U','C','U'),('U','C','A'),('U','C','G'),('U','C','C'),('A','G','U'),('A','G','C')), 
	'Pruline':(('C','C','U'),('C','C','A'),('C','C','G'),('C','C','C')), 
	'Threonine':(('A','C','U'),('A','C','A'),('A','C','G'),('A','C','C')), 
	'Alanine':(('G','C','U'),('G','C','A'),('G','C','G'),('G','C','C')), 
	'Tyrosine':(('U','A','U'),('U','A','C')), 
	'Stop':(('U','A','G'),('U','A','A'),('U','G','A')),
	'Histidine':(('C','A','U'),('C','A','C')),
	'Glutamine':(('C','A','A'),('C','A','G')),
	'Asparagine':(('A','A','U'),('A','A','C')),
	'Lysine':(('A','A','A'),('A','A','G')),
	'Aspartic Acid':(('G','A','U'),('G','A','C')),
	'Glutamic Acid':(('G','A','A'),('G','A','G')),
	'Cysteine':(('U','G','U'),('U','G','C')),
	'Tryptophan':(('U','G','G'),('U','G','G')),
	'Arginine':(('C','G','U'),('C','G','C'),('C','G','A'),('C','G','G'),('A','G','A'),('A','G','G')),
	'Glycine':(('G','G','U'),('G','G','C'),('G','G','A'),('G','G','G'))
	}
	for a in amine.items():
		for aa in a:
			for aaa in aa:
				if aaa==bp:
					count[a[0]]+=1
					return a[0]
	return('404')
gene = rp
for x in range(0,len(gene),3):
	print(trna((gene[x],gene[x+1],gene[x+2])),gene[x],gene[x+1],gene[x+2])
print(count)
'''l=[]
for x in count:
	l.append(x[1])
plt.plot(l,"x")
plt.show()'''