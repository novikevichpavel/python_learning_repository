class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize_image(self, new_resolution):
        self.resolution = new_resolution

    def __str__(self):
        return f"The image {self.title}.{self.extension} is {self.resolution}"

    
my_image = Image("1920x1024", "My_cat", "png")
my_image.__str__()

my_image.resize_image("1024x680")
print(my_image)