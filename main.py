import datetime
import requests
import dacite
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Dato:
    fecha: str
    dato: str

@dataclass
class Serie:
    idSerie: str
    titulo: str
    datos: Optional[List[Dato]] = None

@dataclass
class Bmx:
    series: List[Serie]

@dataclass
class BmxResponse:
    bmx: Bmx


def obtener_tipo_cambio(fecha: str) -> BmxResponse:
    token = ""
    serie = "SF43718"
    url = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/{serie}/datos/{fecha}/{fecha}"
    headers = {
        "Bmx-Token": token
    }

    if token == "" or token is None:
        raise Exception("No se tiene el token de acceso.")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Error al obtener el tipo de cambio.")

    data = response.json()
    return dacite.from_dict(data_class=BmxResponse, data=data)

if __name__ == "__main__":
    fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
    res = obtener_tipo_cambio(fecha_hoy)

    if (res.bmx.series[0].datos is None):
        print("Aún no se tiene el tipo de cambio del día.")
        exit(0)

    tipo_cambio = float(res.bmx.series[0].datos[0].dato)
    print(tipo_cambio)
    exit(0)