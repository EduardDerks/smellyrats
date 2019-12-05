# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

xl = pd.ExcelFile('onions.xls')
# %%
# %% LOAD DATA
rat = (
    pd.read_excel(xl,sheet_name='X')
    .rename(columns=lambda col: col.lower().replace("'", '')) 
)
rat.head()

print('HNMR spectra shape:', rat.shape)
rat.head(5)

# %%
rat['delta/sample']

# %%

print('Spectra is ranging from (ppm)')
rat.index.min(), rat.index.max()

# %%
rat.plot(y='h2-12-')



# %%

from scipy import interpolate
x = rat['delta/sample']
y = rat['h4-31' ]
f = interpolate.interp1d(x, y)

%matplotlib auto
xnew = np.arange(1, 9, 0.002)
ynew = f(xnew)
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.grid()
plt.xlabel('Chemical Shift (Delta)')
plt.ylabel('Intensity')
plt.show()

 
# %%
np.array[rat['h4-31']]

# %%
y = np.array(rat)
plt.plot(y, label='data')

# %%
rat.plot(y='h4-31-')
