

a = []
a1 = []
a2 = []
b = []
c= []
f = open(r'D:\1.PYTHON\baitap\conditii_test_VN4_SORTATE_GC.txt','r')
k = open(r'D:\1.PYTHON\baitap\SUTDS_Shapefie-FCODE.txt','r')
fr= f.readlines()
f.close()
kr = k.readlines()
k.close()
# print(fr)


for line in fr:
    l= line.rstrip('\n')
    ll= line.split(',')
    # print(ll)
    a.append(ll[0])
    # a1.append(ll[1])
    # a2.append(ll[2])
    print(a)
for lin in kr:
    lk= lin.rstrip('\n')
    llk= lin.split(';')
    print(ll)
    # b.append(llk[0])
    # c.append(llk[1])
    # print(c)
p = open(r'result_abc.txt','w')
for i in range(len(a)):
    if a1[i] == b[i]:

        # dùng dic

#         p.write(str(a[i] +','+ str(c[i])+'_C'+ ","+ str(a2[i]))
# # p.close()

# filenames = ['file1.txt', 'file2.txt', 'file3.txt']
# with open('output_file', 'w') as outfile:
#
#     for fname in filenames:
#         with open(fname) as infile:
#             for line in infile:
#         outfile.write(line)



#     x= float(ll[1])
#     y= float(ll[2])
#     j3= float(ll[3])
#     Xpro.append(x)
#     Ypro.append(y)
#     pro_val.append(j3)
#     X = af_val[0] * x + af_val[1] * y + af_val[4]
#     Y = af_val[2] * x + af_val[3] * y + af_val[5]
#     Xnew.append(X)
#     Ynew.append(y)
#
# p = open('ProbeConv.txt','w')
# p.write('ProbeNo\tX\tY\tP_V\n')
# form = '.2f'
# for i in range(len(fread)):
#     p.write(str(No[i]) + '\t' + format(Xnew[i], form) + '\t' + format(Ynew[i], form) + '\t' + format(pro_val[i],form) + '\n')
#
#
# print('\nDone. completed take 17c')
# p.close()
#

#