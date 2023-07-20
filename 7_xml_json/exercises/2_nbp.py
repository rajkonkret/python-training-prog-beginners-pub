# Prezes NBP po ostatnim posiedzeniu Rady Polityki Pieniężnej ogłosił (oprócz decyzji o stopach procentowych),
# że xml API do tabeli kursów walut stało się DEPRECATED i w terminie kilku miesięcy jedynym dostępnym
# formatem przez API będzie JSON. Twoim zadaniem jest przerobić poniższy program używający XML API tak, aby używał JSON
# Więcej na temat tego API: http://api.nbp.pl/

import requests
import xml.etree.ElementTree as ET
from requests import Response

response: Response = requests.get('http://api.nbp.pl/api/exchangerates/tables/A?format=xml')

xml_data: bytes = response.content
money_in_pln: float = float(input("Put amount of money in PLN: "))
currency_code: str = "EUR"

root: ET.Element = ET.fromstring(xml_data.decode())
rates: list[ET.Element] = root.findall('.//Rate')

exchange_rate: float | None = None
for rate in rates:
    if currency_code == rate.find('Code').text:
        exchange_rate = float(rate.find('Mid').text)

if exchange_rate is None:
    print(f"Exchange rate for {currency_code} unavailable")
else:
    print(f"Today we can get {money_in_pln/exchange_rate:.2f}{currency_code} for {money_in_pln:.2f}PLN")
