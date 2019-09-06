import glob

def get_photos():
    p_list = glob.glob("static/img/*.png")
    photos_list = []
    for p in p_list:
        p = p[11::]
        photos_list.append(p)
        print(p)
    return photos_list

if __name__ == '__main__':
    print(get_photos())
