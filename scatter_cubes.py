import matplotlib.pyplot as plt
x_values = range(1,5000)
y_values = [x**3 for x in x_values]

fig,ax = plt.subplots()
ax.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues,s=10)

ax.set_title("cube numbers", fontsize = 24)
ax.set_xlabel("value", fontsize = 14)
ax.set_ylabel("cube of value", fontsize = 14)
ax.axis([0,5000,0,150_000_000_000])
# ax.ticklabel_format(style="plain")

ax.tick_params(labelsize=10)
plt.savefig("generating-data/cube_plot.png")
plt.show()