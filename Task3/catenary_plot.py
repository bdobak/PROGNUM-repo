import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-5,6)
y=np.cosh(x)
plt.plot(x,y,marker='o', label='shape')
plt.grid()
plt.title('Catenary', fontsize=14)
plt.legend(fontsize=12)
plt.show()
