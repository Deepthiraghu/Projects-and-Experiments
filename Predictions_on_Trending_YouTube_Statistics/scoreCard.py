import pylab as pl
import numpy as np
import pandas as pd
dataFrame = pd.read_csv(r'youtube-new/dataset.csv', index_col=None, header=0)
data = dataFrame["likes"]
MIN, MAX = .01, 10.0

pl.figure()
pl.hist(data, bins = 10 ** np.linspace(np.log10(MIN), np.log10(MAX), 50))
pl.gca().set_xscale("log")
pl.show()