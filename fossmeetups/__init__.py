import requests
from tkinter import * 
from tkinter.filedialog import asksaveasfilename
import os

def get_foss_logo(directory=None):
    """
    Downloads images from the given URLs and saves them to the specified directory.
    Args:
    - directory (str): The directory where the images will be saved.

    Returns:
    - None
    """
    foss_logo_dict = {
    "foss_club": "https://github.com/fossunited/Branding/blob/main/asset/foss-club/foss-club-black-and-white.png?raw=true",
    "foss_united": "https://raw.githubusercontent.com/fossunited/Branding/10b0e974094761b454306d9b8b65aac26834a2ca/asset/general-logos/black-on-white.svg",
    "india_foss": "https://raw.githubusercontent.com/fossunited/Branding/10b0e974094761b454306d9b8b65aac26834a2ca/asset/indiafoss/indiafoss.svg",
    "mon_school": "https://raw.githubusercontent.com/fossunited/Branding/10b0e974094761b454306d9b8b65aac26834a2ca/asset/monschool/monschool-colored.svg",
    "support_foss": "https://raw.githubusercontent.com/fossunited/Branding/10b0e974094761b454306d9b8b65aac26834a2ca/asset/project-grant/fossunited-badge.svg",
    "stickers": "https://github.com/fossunited/Branding/blob/main/asset/stickers/un-by-fu-sticker.png?raw=true"
    }
    if directory is None:
        directory = os.getcwd()

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for name, url in foss_logo_dict.items():
        print(" -> "+name)

    try:
        image_name = input(f"Enter a name for the image : ")

        url = foss_logo_dict[image_name]
        response = requests.get(url)
        response.raise_for_status()
        file_extension = url.split('.')[-1].split('?')[0] 
        file_path = os.path.join(directory, f"{image_name}.{file_extension}")
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Saved {image_name} to {file_path}")
    except KeyError:
        print(f"Invalid image name. Please choose from the following: {', '.join(foss_logo_dict.keys())}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

def hello_foss():
    print("Hello, FOSS!")

def speaker_info():
    print("Speaker Name : Mihir Panchal")
    print("Talk Title : From Code to Community: Publishing PyPI Packages in the Open Source World")
    print("Talk Description :\nEmbark on a journey into the heart of open-source collaboration as we delve into the process of publishing Python packages on PyPI. In this talk, we'll explore the ins and outs of packaging your Python projects for distribution, navigating the intricacies of versioning, documentation, and dependencies. Learn how to harness the power of the Python Package Index to share your creations with the world and contribute to the vibrant ecosystem of free and open-source software. Whether you're a seasoned developer looking to share your latest creation or a newcomer eager to join the ranks of open-source contributors, this talk will equip you with the knowledge and tools needed to publish your projects with confidence and make a meaningful impact in the world of Python development.")


speaker_info()
