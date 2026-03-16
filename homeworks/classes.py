class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize_image(self, new_resolution):
        self.resolution = new_resolution
        return self.resolution

    @staticmethod
    def create_message(tesx_one, text_two):
        return f"{tesx_one} {text_two}"
    
    def __str__(self):
        return f"Image {self.title}.{self.extension} has resolution: {self.resolution}"
        

    
my_image = Image("1920x1024", "My_cat", "png")

m_1 = my_image.create_message("Hello", "World")
print(m_1)

print(my_image.resize_image("1024x680"))
print(my_image.__str__())