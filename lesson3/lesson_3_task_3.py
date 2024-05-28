from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Улица Пушкина", "10", "5")
from_address = Address("356700", "Кисловодск","Улица Карла Либкнехта","29","15")

mail = Mailing(to_address, from_address, 500, "ABC123")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")