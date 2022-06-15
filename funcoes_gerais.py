import os, time, unicodedata

def limpar():
    os.system("cls")

def esperar(segundos):
    time.sleep(segundos)

def remove_acento(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8')