import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

prop =  fm.FontProperties(fname='./helvetica.ttf',size=20)


x = []
y1 = []
y2 = []

with open('data','r') as f:
    f.readline()
    for line in f:
        line = line.split()
        x.append(float(line[0]))
        y1.append(float(line[1]))
        y2.append(float(line[-1]))

fig = plt.figure()
ax  = fig.add_subplot(111)
ax.bar([i+0.5 for i in range(len(y2))],y2)
ax.set_xlim(0,9)
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
ax.set_xticklabels(['1','2','4','7','8','14','16','28'])
for item in ax.get_xticklabels():
    item.set_fontproperties(prop)

for item in ax.get_yticklabels():
    item.set_fontproperties(prop)

ax.set_xlabel('# of cores',fontproperties=prop)
ax.set_ylabel('Walltime (s)',fontproperties=prop)
plt.tight_layout()
plt.savefig('barplot.png',format='png',dpi=200)
