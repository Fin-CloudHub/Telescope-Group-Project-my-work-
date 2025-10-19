
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.visualization import ImageNormalize, SquaredStretch, ZScaleInterval
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Get image and import fits data
image_file = '/Users/finlaysime/Desktop/Telescope Group Project/Pirate_Data/Trimmed_files/SS_PG2317_B_Final.fits'
image_data = fits.getdata(image_file)

# Perform image normalization
interval=ZScaleInterval()
stretch = SquaredStretch()
norm = ImageNormalize(image_data, interval=interval, stretch=stretch)


# Plot normalized image
fig, ax = plt.subplots()

# Set up colorbar
divider = make_axes_locatable(ax)
ax_colorbar = divider.append_axes("right", size="5%", pad=0.05)
fig = ax.get_figure()
fig.add_axes(ax_colorbar)


im = ax.imshow(image_data, origin='lower', norm=norm, cmap='bone')
plt.colorbar(im, cax=ax_colorbar, label="Counts")
ax.set_xlabel("Pixel no.")
ax.set_ylabel("Pixel no.")
ax.set_title("SS PG2317+046, B-band")
start, end = ax.get_ylim()
ax.yaxis.set_ticks(np.arange(np.abs(start), end, 1000))
plt.show()
