
class Samsung_GalaxyS:
    def _init_(self, model, RAM, storage, processor, camera, battery, display, os, year):
        self.model = model
        self.RAM = RAM
        self.storage = storage
        self.processor = processor
        self.camera = camera
        self.battery = battery
        self.display = display
        self.os = os
        self.year = year

    def intro(self):
        return f"This is Samsung_GalaxyS series {self.model} with {self.RAM} RAM, {self.storage} storage, {self.processor} processor, {self.camera} camera, {self.battery} battery, {self.display} display, running {self.os} and released in {self.year}"

    def display_specs(self):
        return f"Display: {self.display}"

    def processor_info(self):
        return f"Processor: {self.processor}"

    def camera_capabilities(self):
        return f"Camera: {self.camera}"

    def battery_life(self):
        return "Up to 12 hours of internet use"

    def additional_features(self):
        return "Supports 5G, IP67 water-resistant, and wireless charging"


class Samsung_GalaxyS24Ultra(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S24 Ultra", "12GB", "512GB", "Qualcomm Snapdragon 8 Gen 2", "50MP", "5000mAh", "6.8-inch Dynamic AMOLED", "Android 13", "2024")

    def camera_capabilities(self):
        return "50MP primary sensor, 12MP front camera, 8K video recording"

    def battery_life(self):
        return "Up to 15 hours of internet use"

    def additional_features(self):
        return "IP67 water-resistant, 120Hz refresh rate, 1500 nits peak brightness"

class Samsung_GalaxyS24plus(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S24+", "12GB", "512GB", "Qualcomm Snapdragon 8 Gen 2", "50MP", "5000mAh",
                         "6.6-inch Dynamic AMOLED", "Android 13", "2024")

    def camera_capabilities(self):
        return "50MP primary sensor, 12MP front camera, 8K video recording"

    def battery_life(self):
        return "Up to 12 hours of internet use"

    def additional_features(self):
        return "Supports 5G, IP67 water-resistant, and wireless charging"

class Samsung_GalaxyS23Ultra(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S23 Ultra", "12GB", "512GB", "Qualcomm Snapdragon 8 Gen 1", "108MP", "5000mAh",
                         "6.8-inch Dynamic AMOLED", "Android 12", "2023")

    def camera_capabilities(self):
        return "108MP primary sensor, 40MP front camera, 8K video recording"

    def battery_life(self):
        return "Up to 14 hours of internet use"



class Samsung_GalaxyS23Pro(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S23 Pro", "8GB", "256GB", "Qualcomm Snapdragon 8 Gen 1", "50MP", "4500mAh", "6.2-inch Dynamic AMOLED", "Android 12", "2023")

    def camera_capabilities(self):
        return "50MP primary sensor, 12MP front camera, 4K video recording"

    def battery_life(self):
        return "Up to 12 hours of internet use"


class Samsung_GalaxyS22Ultra(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S22 Ultra", "12GB", "512GB", "Qualcomm Snapdragon 8 Gen 1", "108MP", "5000mAh", "6.8-inch Dynamic AMOLED", "Android 12", "2022")

    def camera_capabilities(self):
        return "108MP primary sensor, 40MP front camera, 8K video recording"

    def battery_life(self):
        return "Up to 14 hours of internet use"


class Samsung_GalaxyS22Pro(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S22 Pro", "8GB", "256GB", "Qualcomm Snapdragon 8 Gen 1", "50MP", "4500mAh", "6.2-inch Dynamic AMOLED", "Android 12", "2022")

class Samsung_GalaxyS21Ultra(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S21 Ultra", "12GB", "512GB", "Qualcomm Snapdragon 888", "108MP", "5000mAh", "6.8-inch Dynamic AMOLED", "Android 11", "2021")


class Samsung_GalaxyS21Lite(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S21 Lite", "6GB", "128GB", "Qualcomm Snapdragon 765G", "64MP", "4500mAh", "6.5-inch Dynamic AMOLED", "Android 11", "2021")

    def battery_life(self):
        return "Up to 12 hours of internet use"

    def camera_capabilities(self):
        return "64MP primary sensor, 32MP front camera, 4K video recording"


class Samsung_GalaxyS20Ultra(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S20 Ultra", "12GB", "128GB", "Qualcomm Snapdragon 865", "108MP", "5000mAh", "6.8-inch Dynamic AMOLED", "Android 10", "2020")

    def camera_capabilities(self):
        return "108MP primary sensor, 40MP front camera, 8K video recording"

    def battery_life(self):
        return "Up to 14 hours of internet use"


class Samsung_GalaxyS20Plus(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S20+", "8GB", "128GB", "Qualcomm Snapdragon 865", "12MP", "4500mAh", "6.7-inch Dynamic AMOLED", "Android 10", "2020")

    def camera_capabilities(self):
        return "12MP primary sensor, 10MP front camera, 4K video recording"


class Samsung_GalaxyS10Plus(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S10+", "8GB", "128GB", "Qualcomm Snapdragon 855", "12MP", "4100mAh", "6.7-inch Dynamic AMOLED", "Android 9.0 (Pie)", "2019")

    def camera_capabilities(self):
        return "12MP primary sensor, 10MP front camera, 4K video recording"

class Samsung_GalaxyS10e(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S10e", "6GB", "128GB", "Qualcomm Snapdragon 855", "12MP", "3100mAh", "5.8-inch Dynamic AMOLED", "Android 9.0 (Pie)", "2019")

    def camera_capabilities(self):
        return "12MP primary sensor, 10MP front camera, 4K video recording"

    def battery_life(self):
        return "Up to 10 hours of internet use"


class Samsung_GalaxyS9Plus(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S9+", "6GB", "64GB", "Qualcomm Snapdragon 845", "12MP", "3500mAh", "6.2-inch Super AMOLED", "Android 8.0 (Oreo)", "2018")

    def camera_capabilities(self):
        return "12MP primary sensor, 8MP front camera, 4K video recording"

    def battery_life(self):
        return "Up to 12 hours of internet use"

class Samsung_GalaxyS8Plus(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S8+", "4GB", "64GB", "Qualcomm Snapdragon 835", "12MP", "3500mAh", "6.2-inch Super AMOLED", "Android 7.0 (Nougat)", "2017")

    def camera_capabilities(self):
        return "12MP primary sensor, 8MP front camera, 4K video recording"

    def battery_life(self):
        return "Up to 12 hours of internet use"

    def additional_features(self):
        return "IP68 water-resistant, wireless charging, and 64GB storage option"

class Samsung_GalaxyS8(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S8", "4GB", "32GB", "Qualcomm Snapdragon 835", "12MP", "3000mAh", "5.8-inch Super AMOLED", "Android 7.0 (Nougat)", "2017")


    def camera_capabilities(self):
        return "12MP primary sensor, 8MP front camera, 4K video recording"

    def battery_life(self):
        return "Up to 10 hours of internet use"

class Samsung_GalaxyS7Edge(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S7 Edge", "4GB", "32GB", "Qualcomm Snapdragon 820", "12MP", "3600mAh", "5.5-inch Super AMOLED", "Android 6.0 (Marshmallow)", "2016")

    def camera_capabilities(self):
        return "12MP primary sensor, 5MP front camera, 4K video recording"

    def battery_life(self):
        return "Up to 12 hours of internet use"

class Samsung_GalaxyS7(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S7", "4GB", "32GB", "Qualcomm Snapdragon 820", "12MP", "3000mAh", "5.1-inch Super AMOLED", "Android 6.0 (Marshmallow)", "2016")

    def camera_capabilities(self):
        return "12MP primary sensor, 5MP front camera, 4K video recording"

    def battery_life(self):
        return "Up to 10 hours of internet use"

class Samsung_GalaxyS6Edge(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S6 Edge", "3GB", "32GB", "Samsung Exynos 7420", "16MP", "2600mAh", "5.1-inch Super AMOLED", "Android 5.0 (Lollipop)", "2015")


    def camera_capabilities(self):
        return "16MP primary sensor, 5MP front camera, 4K video recording"

    def battery_life(self):
        return "Up to 12 hours of internet use"

class Samsung_GalaxyS5(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S5", "2GB", "16GB", "Qualcomm Snapdragon 801", "16MP", "2800mAh", "5.1-inch Super AMOLED", "Android 4.4 (KitKat)", "2014")


    def camera_capabilities(self):
        return "16MP primary sensor, 2MP front camera, 4K video recording"

    def battery_life(self):
        return "Up to 10 hours of internet use"

    def additional_features(self):
        return "IP67 water-resistant, fingerprint sensor, and 16GB storage option"

class Samsung_GalaxyS4(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S4", "2GB", "16GB", "Qualcomm Snapdragon 600", "13MP", "2600mAh", "5.0-inch Super AMOLED", "Android 4.2 (Jelly Bean)", "2013")

    def display_specs(self):
        return "5.0-inch Super AMOLED, 1080 x 1920 pixels"

    def processor_info(self):
        return "Qualcomm Snapdragon 600, Quad-core CPU"

    def camera_capabilities(self):
        return "13MP primary sensor, 2MP front camera, 1080p video recording"

    def battery_life(self):
        return "Up to 8 hours of internet use"

    def additional_features(self):
        return "Air Gesture, Smart Scroll, and 16GB storage option"


class Samsung_GalaxyS3(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S3", "1GB", "16GB", "Qualcomm Snapdragon 400", "8MP", "2100mAh", "4.8-inch Super AMOLED", "Android 4.0 (Ice Cream Sandwich)", "2012")

    def camera_capabilities(self):
        return "8MP primary sensor, 1.9MP front camera, 1080p video recording"

    def battery_life(self):
        return "Up to 12 hours of internet use"

    def additional_features(self):
        return "Supports 4G LTE, Wi-Fi, Bluetooth 4.0, and NFC"

class Samsung_GalaxyS2(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("S2", "1GB", "16GB", "Exynos 4210", "8MP", "1650mAh", "4.3-inch Super AMOLED", "Android 2.3 (Gingerbread)", "2011")

    def camera_capabilities(self):
        return "8MP primary sensor, 0.3MP front camera, 1080p video recording"

    def battery_life(self):
        return "Up to 10 hours of internet use"

    def additional_features(self):
        return "Supports 4G LTE, Wi-Fi, Bluetooth 3.0, and NFC"

class Samsung_GalaxyS_S(Samsung_GalaxyS):
    def __init__(self):
        super()._init_("Galaxy S", "512MB", "8GB", "Hummingbird", "5MP", "1500mAh", "4-inch Super AMOLED", "Android 2.1 (Eclair)", "2010")

    def camera_capabilities(self):
        return "5MP primary sensor, 0.3MP front camera, 720p video recording"

    def battery_life(self):
        return "Up to 10 hours of internet use"

    def additional_features(self):
        return "Supports 4G LTE, Wi-Fi, Bluetooth 3.0, and NFC"


models = {
    "samsung galaxy s24 ultra": Samsung_GalaxyS24Ultra(),
    "samsung galaxy s23 ultra": Samsung_GalaxyS23Ultra(),
    "samsung galaxy s23 pro": Samsung_GalaxyS23Pro(),
    "samsung galaxy s22 ultra": Samsung_GalaxyS22Ultra(),
    "samsung galaxy s22 pro": Samsung_GalaxyS22Pro(),
    "samsung galaxy s21 ultra": Samsung_GalaxyS21Ultra(),
    "samsung galaxy s21 lite": Samsung_GalaxyS21Lite(),
    "samsung galaxy s20 ultra": Samsung_GalaxyS20Ultra(),
    "samsung galaxy s20 plus": Samsung_GalaxyS20Plus(),
    "samsung galaxy s10 plus": Samsung_GalaxyS10Plus(),
    "samsung galaxy s10e": Samsung_GalaxyS10e(),
    "samsung galaxy s9 plus": Samsung_GalaxyS9Plus(),
    "samsung galaxy s8 plus": Samsung_GalaxyS8Plus(),
    "samsung galaxy s8": Samsung_GalaxyS8(),
    "samsung galaxy s7 edge": Samsung_GalaxyS7Edge(),
    "samsung galaxy s7": Samsung_GalaxyS7(),
    "samsung galaxy s6 edge": Samsung_GalaxyS6Edge(),
    "samsung galaxy s5": Samsung_GalaxyS5(),
    "samsung galaxy s4": Samsung_GalaxyS4(),
    "samsung galaxy s3": Samsung_GalaxyS3(),
    "samsung galaxy s2": Samsung_GalaxyS2(),
}


def show_all_models():
    for model_name, model in models.items():
        print(f"--- {model_name} ---")
        model.intro()
        print()


def show_model_details(model_name):
    if model_name in models:
        model = models[model_name]
        print(model.intro())
        print()
        print(model.display_specs())
        print(model.processor_info())
        print(model.camera_capabilities())
        print(model.battery_life())
        print(model.additional_features())
    else:
        print("Model not yet available. Please try other models.")

while True:
    user_input = input("Enter 'show all' to display all models or enter a specific model name: ")
    print()
    if user_input.lower() == 'show all':
        show_all_models()
    else:
        show_model_details(user_input)
