# PROGRAMMING PROJECT 1
# CS 111 - GREEN
# UIC, OCTOBER 2016

# QUESTION 1:

def getORF(DNAseq):
    file_1 = open("X73525.fasta","r")
    DNAseq = file_1.read()
    file1.close()
    counter == 0
    for codon in range(len(DNAseq)):
        if DNAseq[codon:codon+3] == "TAG" or DNAseq[codon:codon+3] == "TAA" or DNAseq[codon:codon+3] == "TGA":
            counter = counter + 1
            print(counter)

# QUESTION 2:

def oneFrame(DNA):
    for index in range(len(DNA)):
        if DNA[index] == "ATG":
            getORF(DNA)
            myList = myList + [getORF(DNA)]
            print(myList)

# QUESTION 3:

def findAllORFs(DNA):
    if oneFrame(DNA) == "ATG":
        aList = getORF(DNA)
    elif oneFrame(DNA) != "ATG":
        bList = getORF(DNA)
    cList = aList + bList
    print(cList)

# QUESTION 4:

def gcCONTENT(getORF):
    counter = 0
    for content in range(len(DNAseq)):
        if content == "G" or content == "C":
            counter == counter + 1
            print(counter)

# QUESTION 5:

def geneFinder(DNA, minLen, minGC):
    if minLen < getORF(DNA) and minGC > getORF(DNA):
        list = [getORF(DNA), minLen, minGC]
        print(list)
