# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# %%
xl = pd.ExcelFile('onions.xls')
# %%
# %% LOAD SPECTRAL DATA
hNMR = (
    pd.read_excel(xl,sheet_name='X')
    .rename(columns=lambda col: col.lower().replace("'", '')) 
)
hNMR.head()
# %% LOAD ONION DATA
onions = (
    pd.read_excel(xl,sheet_name='y')
    .rename(columns=lambda col: col.lower().replace("'", '')) 
)
onions.head()

print('Onions shape:', onions.shape)
onions.head(5)

# %%
hNMR['delta/sample']

# %%

print('Spectra is ranging from (ppm)')
hNMR.index.min(), hNMR.index.max()

# %%
hNMR.plot(y='h2-12-')


# %%
X = hNMR.transpose()





# %%

from scipy import interpolate
x = hNMR['delta/sample']
y = hNMR['h4-31' ]
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
np.array[hNMR['h4-31']]

# %%
y = np.array(hNMR)
plt.plot(y, label='data')

# %%
hNMR.plot(y='h4-31-')
