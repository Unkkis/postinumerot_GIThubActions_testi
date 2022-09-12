# Esimerkkisuoritus:
#
# Kirjoita postitoimipaikka: Porvoo
# Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500
from doctest import ELLIPSIS_MARKER
import urllib.request
import json


def hae_p_numerot():
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        data = response.read()

    p_numerot = json.loads(data)
    return p_numerot


def hae_postitoimipaikat(p_toimipaikka: str) -> str:
    aineisto = hae_p_numerot()

    p_toimipaikka = p_toimipaikka.upper()
    if p_toimipaikka or p_toimipaikka.replace(" ", "") in aineisto.values():
        hakutulokset = []
        for postinumero, toimipaikka in aineisto.items():
            if toimipaikka == p_toimipaikka or toimipaikka == p_toimipaikka.replace(" ", "") or toimipaikka == p_toimipaikka.replace("SMARTPOST", "SMART POST"):
                hakutulokset.append(postinumero)
        hakutulokset.sort()
        return hakutulokset


if __name__ == "__main__":

    p_toimipaikka = input("Kirjoita postitoimipaikka: ")
    toimipaikat = hae_postitoimipaikat(p_toimipaikka)

    if toimipaikat:
        print(f"Postinumerot: ", end="")
        print(", ".join(toimipaikat))
    else:
        print("Tuntematon postitoimipaikka")
