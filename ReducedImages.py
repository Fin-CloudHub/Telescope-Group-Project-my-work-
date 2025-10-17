import numpy as np
from astropy.io import fits
import os

# Root directory
root_dir = "/Users/finlaysime/Desktop/Telescope Group Project/Pirate_Data"

###################### MASTER FLATS & BIAS ################################

# Find the master bias and flat fits files
master_bias_path = os.path.join(root_dir, "master_bias.fits")
master_flat_B_path = os.path.join(root_dir, "master_flat_B.fits")
master_flat_U_path = os.path.join(root_dir, "master_flat_U.fits")
master_flat_V_path = os.path.join(root_dir, "master_flat_V.fits")

# Open maser bias and flat files for each filter
with fits.open(master_flat_B_path) as hdul:
    master_flat_B = hdul[0].data
with fits.open(master_flat_U_path) as hdul:
    master_flat_U = hdul[0].data
with fits.open(master_flat_V_path) as hdul:
    master_flat_V = hdul[0].data
with fits.open(master_bias_path) as hdul:
    master_bias = hdul[0].data


############################### M52 #####################################

# Find the M52 fits files
M52_files = os.path.join(root_dir, "M52")

storage_M52_V = []
storage_M52_U = []
storage_M52_B = []

for file in os.listdir(M52_files):
    if file.lower().endswith('.fits'):
        file_path = os.path.join(M52_files, file)
        with fits.open(file_path) as hdul:
            data = hdul[0].data
            header = hdul[0].header
        
        if "Filter_V" in file:
            reduced_data = (data - master_bias) / master_flat_V
            storage_M52_V.append(reduced_data)
        if "Filter_U" in file:
            reduced_data = (data - master_bias) / master_flat_U
            storage_M52_U.append(reduced_data)
        if "Filter_B" in file:
            reduced_data = (data - master_bias) / master_flat_V
            storage_M52_B.append(reduced_data)
        
# Build final images of M52 star cluster
final_image_M52_V = np.mean(np.array(storage_M52_V), axis=0)
final_image_M52_U = np.mean(np.array(storage_M52_U), axis=0)
final_image_M52_B = np.mean(np.array(storage_M52_B), axis=0)

out_file = os.path.join(root_dir, "M52_V_Final.fits")
hdu = fits.PrimaryHDU(final_image_M52_V, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "M52_U_Final.fits")
hdu = fits.PrimaryHDU(final_image_M52_U, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "M52_B_Final.fits")
hdu = fits.PrimaryHDU(final_image_M52_B, header=header)
hdu.writeto(out_file, overwrite=True)

print("Finished M52")
            

############################ NGC6755 ######################################

# Find the NGC6755 fits files
NGC6755_files = os.path.join(root_dir, "NGC6755")            

storage_NGC6755_V = []
storage_NGC6755_U = []
storage_NGC6755_B = []

for file in os.listdir(NGC6755_files):
    if file.lower().endswith('.fits'):
        file_path = os.path.join(NGC6755_files, file)
        with fits.open(file_path) as hdul:
            data = hdul[0].data
            header = hdul[0].header
            
        if "Filter_V" in file:
            reduced_data = (data - master_bias) / master_flat_V
            storage_NGC6755_V.append(reduced_data)
        if "Filter_U" in file:
            reduced_data = (data - master_bias) / master_flat_U
            storage_NGC6755_U.append(reduced_data)
        if "Filter_B" in file:
            reduced_data = (data - master_bias) / master_flat_B
            storage_NGC6755_B.append(reduced_data)


# Build final images of NGC6755 star cluster
final_image_NGC6755_V = np.mean(np.array(storage_NGC6755_V), axis=0)
final_image_NGC6755_U = np.mean(np.array(storage_NGC6755_U), axis=0)
final_image_NGC6755_B = np.mean(np.array(storage_NGC6755_B), axis=0)

out_file = os.path.join(root_dir, "NGC6755_V_Final.fits")
hdu = fits.PrimaryHDU(final_image_NGC6755_V, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "NGC6755_U_Final.fits")
hdu = fits.PrimaryHDU(final_image_NGC6755_U, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "NGC6755_B_Final.fits")
hdu = fits.PrimaryHDU(final_image_NGC6755_B, header=header)
hdu.writeto(out_file, overwrite=True)

print("Finished NGC6755")


########################### SS 111773 #######################################
            
SS_111773_files = os.path.join(root_dir, "111773")

storage_SS_111773_V = []
storage_SS_111773_U = []
storage_SS_111773_B = []

for file in os.listdir(SS_111773_files):
    if file.lower().endswith('.fits'):
        file_path = os.path.join(SS_111773_files, file)
        with fits.open(file_path) as hdul:
            data = hdul[0].data
            header = hdul[0].header
            
        if "Filter_V" in file:
            reduced_data = (data - master_bias) / master_flat_V
            storage_SS_111773_V.append(reduced_data)
        if "Filter_U" in file:
            reduced_data = (data - master_bias) / master_flat_U
            storage_SS_111773_B.append(reduced_data)
        if "Filter_B" in file:
            reduced_data = (data - master_bias) / master_flat_B
            storage_SS_111773_B.append(reduced_data)
            
final_image_SS_111773_V = np.mean(np.array(storage_SS_111773_V), axis=0)
final_image_SS_111773_U = np.mean(np.array(storage_SS_111773_U), axis=0)
final_image_SS_111773_B = np.mean(np.array(storage_SS_111773_B), axis=0)

out_file = os.path.join(root_dir, "SS_111773_V_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_111773_V, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_111773_U_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_111773_U, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_111773_B_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_111773_B, header=header)
hdu.writeto(out_file, overwrite=True)

print("Finished SS 111773")

            
######################### SS GD246 #####################################

SS_GD246_files = os.path.join(root_dir, "GD246")

storage_SS_GD246_V = []
storage_SS_GD246_U = []
storage_SS_GD246_B = []

for file in os.listdir(SS_GD246_files):
    if file.lower().endswith('.fits'):
        file_path = os.path.join(SS_GD246_files, file)
        with fits.open(file_path) as hdul:
            data = hdul[0].data
            header = hdul[0].header
            
        if "Filter_V" in file:
            reduced_data = (data - master_bias) / master_flat_V
            storage_SS_GD246_V.append(reduced_data)
        if "Filter_U" in file:
            reduced_data = (data - master_bias) / master_flat_U
            storage_SS_GD246_U.append(reduced_data)
        if "Filter_B" in file:
            reduced_data = (data - master_bias) / master_flat_B
            storage_SS_GD246_B.append(reduced_data)

final_image_SS_GD246_V = np.mean(np.array(storage_SS_GD246_V), axis=0)
final_image_SS_GD246_U = np.mean(np.array(storage_SS_GD246_U), axis=0)
final_image_SS_GD246_B = np.mean(np.array(storage_SS_GD246_B), axis=0)

out_file = os.path.join(root_dir, "SS_GD246_V_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_GD246_V, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_GD246_U_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_GD246_U, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_GD246_B_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_GD246_B, header=header)
hdu.writeto(out_file, overwrite=True)

print("Finished GD 246")


###################### SS 11223 #######################################

SS_11223_files = os.path.join(root_dir, "11223")

storage_SS_11223_V = []
storage_SS_11223_U = []
storage_SS_11223_B = []

for file in os.listdir(SS_11223_files):
    if file.lower().endswith('.fits'):
        file_path = os.path.join(SS_11223_files, file)
        with fits.open(file_path) as hdul:
            data = hdul[0].data
            header = hdul[0].header
            
        if "Filter_V" in file:
            reduced_data = (data - master_bias) / master_flat_V
            storage_SS_11223_V.append(reduced_data)
        if "Filter_U" in file:
            reduced_data = (data - master_bias) / master_flat_U
            storage_SS_11223_U.append(reduced_data)
        if "Filter_B" in file:
            reduced_data = (data - master_bias) / master_flat_B
            storage_SS_11223_B.append(reduced_data)
            
final_image_SS_11223_V = np.mean(np.array(storage_SS_11223_V), axis=0)
final_image_SS_11223_U = np.mean(np.array(storage_SS_11223_U), axis=0)
final_image_SS_11223_B = np.mean(np.array(storage_SS_11223_B), axis=0)

out_file = os.path.join(root_dir, "SS_11223_V_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_11223_V, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_11223_U_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_11223_U, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_11223_B_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_11223_B, header=header)
hdu.writeto(out_file, overwrite=True)

print("Finished SS 11223")


############################ SS 114750 ###################################

SS_114750_files = os.path.join(root_dir, "114750")

storage_SS_114750_V = []
storage_SS_114750_U = []
storage_SS_114750_B = []

for file in os.listdir(SS_114750_files):
    if file.lower().endswith('.fits'):
        file_path = os.path.join(SS_114750_files, file)
        with fits.open(file_path) as hdul:
            data = hdul[0].data
            header = hdul[0].header
            
        if "Filter_V" in file:
            reduced_data = (data - master_bias) / master_flat_V
            storage_SS_114750_V.append(reduced_data)
        if "Filter_U" in file:
            reduced_data = (data - master_bias) / master_flat_U
            storage_SS_114750_U.append(reduced_data)
        if "Filter_B" in file:
            reduced_data = (data - master_bias) / master_flat_B
            storage_SS_114750_B.append(reduced_data)
            
final_image_SS_114750_V = np.mean(np.array(storage_SS_114750_V), axis=0)
final_image_SS_114750_U = np.mean(np.array(storage_SS_114750_U), axis=0)
final_image_SS_114750_B = np.mean(np.array(storage_SS_114750_B), axis=0)

out_file = os.path.join(root_dir, "SS_114750_V_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_114750_V, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_114750_U_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_114750_U, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_114750_B_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_114750_B, header=header)
hdu.writeto(out_file, overwrite=True)

print("Finished SS 114750")

########################### SS PG2317 #################################

SS_PG2317_files = os.path.join(root_dir, "PG2317")

storage_SS_PG2317_V = []
storage_SS_PG2317_U = []
storage_SS_PG2317_B = []

for file in os.listdir(SS_PG2317_files):
    if file.lower().endswith('.fits'):
        file_path = os.path.join(SS_PG2317_files, file)
        with fits.open(file_path) as hdul:
            data = hdul[0].data
            header = hdul[0].header
            
        if "Filter_V" in file:
            reduced_data = (data - master_bias) / master_flat_V
            storage_SS_PG2317_V.append(reduced_data)
        if "Filter_U" in file:
            reduced_data = (data - master_bias) / master_flat_U
            storage_SS_PG2317_U.append(reduced_data)
        if "Filter_B" in file:
            reduced_data = (data - master_bias) / master_flat_B
            storage_SS_PG2317_B.append(reduced_data)

final_image_SS_PG2317_V = np.mean(np.array(storage_SS_PG2317_V), axis=0)
final_image_SS_PG2317_U = np.mean(np.array(storage_SS_PG2317_U), axis=0)
final_image_SS_PG2317_B = np.mean(np.array(storage_SS_PG2317_B), axis=0)

out_file = os.path.join(root_dir, "SS_PG2317_V_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_PG2317_V, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_PG2317_U_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_PG2317_U, header=header)
hdu.writeto(out_file, overwrite=True)

out_file = os.path.join(root_dir, "SS_PG2317_B_Final.fits")
hdu = fits.PrimaryHDU(final_image_SS_PG2317_B, header=header)
hdu.writeto(out_file, overwrite=True)

print("Finished SS PG2317")
print("FINISHED ALL")
