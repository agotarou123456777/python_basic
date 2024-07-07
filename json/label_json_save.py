import json


def update_json_file(file_path, labels):
    print(labels)
    with open(file_path, 'w') as file:
        json.dump(labels, file, ensure_ascii=False, indent=4)


file_path = "/home/hajime/mylib/data/others/FashionMNIST_label.json"
labels = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

update_json_file(file_path, labels)
