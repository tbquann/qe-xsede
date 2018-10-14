import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

prop = fm.FontProperties(fname='./helvetica.ttf',size=18)


y = []

with open('compiler','r') as f:
    for line in f:
        line = line.split()
        y.append(float(line[1]))

fig = plt.figure()
ax  = fig.add_subplot(111,aspect=0.00004)
ax.bar([0.5,1.5,2.5,3.5,4.5],y)
ax.set_xlim(0,6)
ax.set_ylabel('Wall Time (s)', fontproperties=prop)
plt.xticks([1,2,3,4,5],['IMPI + GCC','IMPI + Intel', 'MPICH+GCC', 'MPICH+Intel',
    'Openmpi+GCC'],rotation=300,fontproperties=prop)
for item in ax.get_yticklabels():
    item.set_fontproperties(prop)

plt.tight_layout()
plt.savefig('RM.png',format='png',dpi=200)
