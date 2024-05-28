from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "GalaxyS20", "+79123456789")
catalog.append(phone1)

phone2 = Smartphone("Apple", "IPhon12", "+791834567867")
catalog.append(phone2)

phone3 = Smartphone("Xiaomi","Redmi Note10","+793834567892")
catalog.append(phone3)

phone4 = Smartphone("One Plus","One Plus9 Pro", "+796298763428")
catalog.append(phone4)

phone5 = Smartphone("Huawei", "P40 Pro", "+792850976034")
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand}-{phone.model}.{phone.phone_number}")