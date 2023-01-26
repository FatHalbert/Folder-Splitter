import os

# specify the source folder where the files are currently located
source_folder = r"C:\"

# specify the destination folder where the subfolders and files will be created
destination_folder = r"C:\"

# Initialize the folder counter and image counter
folder_count = 0
image_count = 0

# create the first folder
os.makedirs(f"{destination_folder}/folder{folder_count}")

# Iterate through all files in the source folder
for filename in os.listdir(source_folder):
    # Check if the file has a .JPG extension
    if filename.endswith(".JPG"):
        # Check if the current subfolder has less than 25 images.
        if image_count < 25:
            # Rename the file to move it to the current subfolder
            os.rename(f"{source_folder}/{filename}", f"{destination_folder}/folder{folder_count}/{filename}")
            # Increment the image counter
            image_count += 1
        else:
            # If the current subfolder has 25 images, increment the folder counter
            folder_count += 1
            # Reset the image counter
            image_count = 0
            # Create a new subfolder with the name format "folder{folder_count}"
            os.makedirs(f"{destination_folder}/folder{folder_count}")
