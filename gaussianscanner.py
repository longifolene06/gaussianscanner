import re

filename = input('Input the filename. Try THE ABSOLUTE path if doesn\'t work.')
exset = ['Eigenvalues --']
flag = 1
while flag != 0:
    ipt = input('Input scanned variants. (In the form of R3,A11,D22.) Leave blank to continue.')
    if ipt != '':
        exset.append(ipt)
    else:
        flag = 0

patset = []
for ex in exset:
    patset.append(' *' + ex + '( *[-, ]?[0-9]{1,}\.[0-9]{5})*\n')
with open(filename,'r') as inp:
    lines = inp.readlines()
    output = []
    for i in range(len(patset)):
        output.append([])
    flag = 1
    while flag != 0:
        for i in range(len(patset)):
            if re.fullmatch(patset[i],lines[-1]) != None:
                for value in re.findall('[-, ]?[0-9]{1,}\.[0-9]{5}',lines[-1]):
                    output[i].append(float(value))
        if lines[-1] == ' GradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGrad\n':
            flag = 0
        del lines[-1]

result = input('Transpose or not?(Y/N)')
if result == 'Y':
    output2 = []
    for i in range(len(output[0])):
        output2.append([])
        for j in range(len(output)):
            output2[-1].append(output[j][i])
    print('\n',output2,'\n\nprint(output) For untransposed result.')
else:
    print(output)

input('\n四界の闇を統べる王\n\n汝の欠片の縁に從い\n\n汝ら全員の力もて\n\n我にさらなる魔力を与えよ\n')
