# Bing Image Dataset Downloader

A simple Python script to automatically collect images from Bing based on custom keywords.  
Useful for building image datasets for **machine learning**, **computer vision**, and **research projects**.

---

## 📦 Features
- Download images for multiple keywords at once.
- Customize the output directory and number of images.
- Supports both English and non-English keywords.
- Easy to extend for different dataset creation needs.

---

## 🛠️ Installation

Install the required package:

```bash
pip install bing-image-downloader
```
Clone this repository:

```bash
git clone https://github.com/TarkanAI/bing-image-dataset-downloader.git
cd bing-image-dataset-downloader
```

▶️ Usage

Edit the Python script and replace the keywords/output directory with your own:
```bash
from bing_image_downloader import downloader

query = ['forest fire',
         'house fire',
         'warehouse fire']

for query_string in query:
    try:
        downloader.download(query_string,
                            limit=200,             # number of images per keyword
                            page_limit=1000,       # max pages to scan
                            output_dir='dataset',  # output folder name
                            adult_filter_off=True,
                            force_replace=False,
                            timeout=1000,
                            verbose=True)
    except:
        continue
```
Run the script:
```bash
python downloader.py
```

📂 Example Output Structure
```
dataset/
│── forest fire/
│   ├── Image_1.jpg
│   ├── Image_2.jpg
│   └── ...
│── house fire/
│   ├── Image_1.jpg
│   └── ...
│── warehouse fire/
    ├── Image_1.jpg
    └── ...
```
## 🔮 Notes
This is just a small side script I often use when I need quick image datasets.  
I can’t share my thesis-related projects yet, but I wanted to keep this public as an example.  
Bigger projects are on the way 🚀


