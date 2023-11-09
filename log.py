#! /home/gitpod/.pyenv/shims/tutorial-env python3

import os
import logging
from logging import handlers

log_level = os.getenv("LOG_level", "WARNING").upper()
log = logging.Logger("Maicon", log_level)
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=300, #10**6
    backupCount=10,
)
fh.setFormatter(log.level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)

#ch.setFormatter(fmt)
fh.setFormatter(fmt)
#log.addHandler(ch)
log.addHandler(fh)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erroa geral ex: banco de dados sumiu")
"""
print("---")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("[ERRO] Deu erro %s",str(e))
    # stdout
    #stderr