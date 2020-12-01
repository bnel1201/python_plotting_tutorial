#%% 
1 + 1

#%%

import matplotlib.pyplot as plt
import numpy as np
# %%
plt.plot([1,2,3,4], [1,4,2,6])
plt.show()
# %%

# %%
x = 10
y = 12

z = np.array([[i*j for i in range(10)] for j in range(10)])
# %%

plt.imshow(z)
plt.show()

# %%
