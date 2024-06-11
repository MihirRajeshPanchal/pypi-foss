import requests
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

def get_foss_logo():
    foss_logo_dict = {
        "foss_club": "https://github.com/fossunited/Branding/blob/main/asset/foss-club/foss-club-black-and-white.png?raw=true",
        "foss_united": "https://raw.githubusercontent.com/fossunited/Branding/10b0e974094761b454306d9b8b65aac26834a2ca/asset/general-logos/black-on-white.svg",
        "india_foss": "https://raw.githubusercontent.com/fossunited/Branding/10b0e974094761b454306d9b8b65aac26834a2ca/asset/indiafoss/indiafoss.svg",
        "mon_school": "https://raw.githubusercontent.com/fossunited/Branding/10b0e974094761b454306d9b8b65aac26834a2ca/asset/monschool/monschool-colored.svg",
        "support_foss": "https://raw.githubusercontent.com/fossunited/Branding/10b0e974094761b454306d9b8b65aac26834a2ca/asset/project-grant/fossunited-badge.svg",
        "stickers": "https://github.com/fossunited/Branding/blob/main/asset/stickers/un-by-fu-sticker.png?raw=true"
    }

    print("Available logos:")
    for key in foss_logo_dict.keys():
        print(f"- {key}")
    
    logo_choice = input("Enter the name of the logo you want to download: ")

    logo_choice = "foss_club"
    if logo_choice not in foss_logo_dict:
        print("Invalid choice. Please run the program again and choose a valid option.")
        return

    download_url = foss_logo_dict[logo_choice]

    root = Tk()
    root.withdraw()

    save_path = asksaveasfilename(
        title="Save Image As",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("SVG files", "*.svg"), ("All files", "*.*")]
    )

    root.destroy()

    if not save_path:
        print("Save operation cancelled.")
        return

    response = requests.get(download_url)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully and saved to {save_path}")
    else:
        print("Failed to download the image. Please check the URL or your internet connection.")

def hello_foss():
    print("Hello, FOSS!")

def speaker_info():
    print("Speaker Name : Mihir Panchal")
    print("Talk Title : From Code to Community: Publishing PyPI Packages in the Open Source World")
    print("Talk Description : Embark on a journey into the heart of open-source collaboration as we delve into the process of publishing Python packages on PyPI. In this talk, we'll explore the ins and outs of packaging your Python projects for distribution, navigating the intricacies of versioning, documentation, and dependencies. Learn how to harness the power of the Python Package Index to share your creations with the world and contribute to the vibrant ecosystem of free and open-source software. Whether you're a seasoned developer looking to share your latest creation or a newcomer eager to join the ranks of open-source contributors, this talk will equip you with the knowledge and tools needed to publish your projects with confidence and make a meaningful impact in the world of Python development.")

