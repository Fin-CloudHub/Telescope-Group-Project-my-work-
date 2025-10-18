
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import ImageNormalize, SquaredStretch, ZScaleInterval

# import image and retrieve data
image_file = '/Users/finlaysime/Desktop/Telescope Group Project/Pirate_Data/Trimmed_files/M52_V_Final.fits'
image_data = fits.getdata(image_file)

# Calculate the interval and modify the contrast
interval=ZScaleInterval(contrast=0.4)

# Stertch the values of the image
stretch = SquaredStretch()

# Normalize the image
norm = ImageNormalize(image_data, interval=interval, stretch=stretch)

# Display the normalized image
plt.imshow(image_data, origin='lower', norm=norm, cmap='bone')
plt.colorbar()
plt.xlabel("Pixel no.")
plt.ylabel("Pixel no.")
