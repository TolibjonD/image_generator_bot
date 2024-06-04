import requests

def image_generator(category):
    YOUR_ACCESS_KEY = "LvUcxTAcQiqCcgwSVytdZpJ9o6CL3ZFN3EJ5d9a1Iv0"
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id={YOUR_ACCESS_KEY}"
    res = requests.get(url).json()
    image = res['urls']["full"]
    descr = res["description"]
    likes = res['likes']
    data = {
        "image": image,
        "descr": descr,
        "likes": likes
    }
    return data