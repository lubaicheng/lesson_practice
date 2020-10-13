DNA = 'ATCGCGCQTAGCATC'
DNA_len = len(DNA)
conding_area = DNA[:7]+DNA[8:]
ratio = (len(conding_area)/len(DNA))
print(conding_area) 
print(str((ratio)*100) + '%')
print(conding_area.upper())
print(DNA[7:8].lower())