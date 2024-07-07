import json

def update_json_file(file_path, data):
  
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            
        json_data[data["id"]] = {
            "prompt": data["prompt"],
            "files": data["files"],
            "result": data["result"]
        }
            
    except FileNotFoundError:
        json_data = {
            str(data["id"]): {
                "prompt": data["prompt"],
                "files": data["files"],
                "result": data["result"]
            }
        }
    
    # JSON形式でファイルに保存
    with open(file_path, 'w') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)


# 辞書型変数を定義
data = {
    "id": 1,
    "prompt": "xx",
    "files": [],
    "result": "zz"
}


update_json_file("/home/hajime/mylib/data.json", data)