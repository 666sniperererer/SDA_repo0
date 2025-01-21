class Camera:
    #Kameru potřebujeme "otevřít" - nakonfigurovat - uzávěrka, ISO, další parametry....
    def __enter__(self):
        print("tady něco nastavujeme.....")
        return self

    #S kamerou pracujeme - vememe z ní snímky
    def get_image(self):
        print("fotíme snímek")

    #Na konci potřebujeme kameru "uzavřít" - tzn. vyčištění chyb, vyčištění mezisnímků, ...
    def __exit__(self, a, b, c):
        print("tady něco čistíme..")
        pass

with Camera() as camera_4mpx:
    camera_4mpx.get_image()
    camera_4mpx.get_image()