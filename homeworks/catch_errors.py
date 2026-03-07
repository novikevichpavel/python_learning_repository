def image_info(dict):
    new_dict = {**dict}
    if ("image_id" not in new_dict) or ("image_title" not in new_dict):
        raise TypeError("Missing an argument")
    return f"Image {new_dict["image_title"]} has id {new_dict["image_id"]}"

try:
    print(image_info({"image_id": 123, "image_title": "my_cat"}))
    print(image_info({"iamge_id":222, "id": 123}))
except TypeError as e:
    print(e)