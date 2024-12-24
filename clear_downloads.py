import os
import shutil

def clear_downloads():
    # Get the path to the Downloads folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Check if the Downloads folder exists
    if os.path.exists(downloads_folder):
        # Iterate over the items in the Downloads folder
        for item in os.listdir(downloads_folder):
            item_path = os.path.join(downloads_folder, item)
            
            # If the item is a directory, remove it recursively
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                # If the item is a file, delete it
                os.remove(item_path)
        
        print("Downloads folder cleared.")
    else:
        print("Downloads folder does not exist.")

# Call the function to clear the Downloads folder
clear_downloads()
