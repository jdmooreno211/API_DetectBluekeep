# Suponiendo que 'main' está definido en un módulo importado llamado 'FBI'
from detect_bluekeep import main as scan_main

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/{ip_address}")
def read_root(ip_address: str, debug: bool = False, notls: bool = True, logfile: Union[str, None] = None, workers: int = 300):
    # Llama a la función modificada y captura los resultados
    results = scan_main([ip_address], debug=debug, notls=notls, logfile=logfile, workers=workers)
    # Devuelve los resultados a través de la API
    return {"results": results}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}