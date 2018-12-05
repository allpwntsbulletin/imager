# by larik
import requests, string, urllib, random, os, urllib.request, threading
try: from PIL import ImageFile
except: print("Please install Pillow `python3 -m pip install pillow`")
url_length = 6
# Imgur has moved to 7 character image names,
# so changing this to 7 will get you newer images
# but at a much slower rate.
total_threads = 25
def get():
    while True:
        try:
            img_name = "".join(random.choice(string.ascii_letters +
                            string.digits) for l in range(url_length))
            img_get = requests.head(
                    url = f"http://i.imgur.com/{img_name}.png",
                    allow_redirects = False)
            if img_get.status_code == 200:
                img = urllib.request.urlopen(img_get.url)
                parse = ImageFile.Parser()
                while True:
                    data = img.read(1024)
                    if not data:
                        break
                    parse.feed(data)
                    if parse.image:
                        img_len, img_width = parse.image.size
                        break
                if img_len <= 300: img_size = "small"
                elif img_len <= 600: img_size = "medium"
                elif img_len <= 2000: img_size = "large"
                else: img_size = "huge"
                print(f"Got {img_get.url} size {img_size}")
                urllib.request.urlretrieve(img_get.url, f"{img_size}/imgur-{img_name}.png")
        except Exception as ex: print(ex)

try:
    os.mkdir("small")
    os.mkdir("medium")
    os.mkdir("large")
    os.mkdir("huge")
except FileExistsError: pass

for i in range(total_threads): threading.Thread(target=get).start()
