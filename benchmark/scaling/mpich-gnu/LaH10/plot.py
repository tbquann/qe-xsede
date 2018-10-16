import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

prop  = fm.FontProperties(fname='./helvetica.ttf',size=20)
prop1 = fm.FontProperties(fname='./helvetica.ttf',size=17) 

x = []
y1 = []
y2 = []

with open('rm-data','r') as f:
    f.readline()
    for line in f:
        line = line.split()
        x.append(float(line[0]))
        y1.append(float(line[1]))
        y2.append(float(line[-1]))

lx = []
ly1 = []
ly2 = []

with open('lm-data','r') as f:
    f.readline()
    for line in f:
        line = line.split()
        lx.append(float(line[0]))
        ly1.append(float(line[1]))


fig = plt.figure()
ax  = fig.add_subplot(121)
ax1 = fig.add_subplot(122)

ax.bar([i+0.5 for i in range(len(y2))],y2)
ax.set_xlim(0,6)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels(['2','4','7','14','28'])

ax1.set_xlim(0,6)
ax1.bar([i+0.5 for i in range(len(ly1))],ly1)
ax1.set_xticks([1,2,3,4,5])
ax1.set_xticklabels(['2','4','8','16','32'])
ax1.set_xlabel('# of cores',fontproperties=prop)

for item in ax.get_xticklabels():
    item.set_fontproperties(prop)

for item in ax.get_yticklabels():
    item.set_fontproperties(prop)

for item in ax1.get_xticklabels():
    item.set_fontproperties(prop)

for item in ax1.get_yticklabels():
    item.set_fontproperties(prop)

ax.set_ylim(0,7000)
ax1.set_ylim(0,7000)

ax.set_title("Regular Memory",fontproperties=prop1)
ax1.set_title("Large Memory",fontproperties=prop1)

ax.set_xlabel('# of cores',fontproperties=prop)
ax.set_ylabel('Walltime (s)',fontproperties=prop)

plt.tight_layout()
plt.savefig('barplot.png',format='png',dpi=200)
