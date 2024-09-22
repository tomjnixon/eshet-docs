import os
import sys

project = 'eshet'
copyright = '2023, Thomas Nixon'
author = 'Thomas Nixon'

extensions = []

sys.path.append(os.path.abspath("./_ext"))
extensions.append("literal_ref")

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

sys.path.append(os.path.abspath("."))
from deliterate import deliterate
from pathlib import Path

eshetsrv = Path("../submodules/eshetsrv")
literate_files = [
    (eshetsrv / "apps/eshetproto/src/messages.hrl", "protocol.rst"),
    (eshetsrv / "apps/eshetproto/src/eshetnet_proto_impl.erl", "binary_protocol.rst"),
    (eshetsrv / "apps/eshethttp/src/eshethttp_ws.erl", "websocket_protocol.rst"),
]

for fname_in, fname_out in literate_files:
    with open(fname_in) as f_in, open(fname_out, "w") as f_out:
        deliterate(f_in, f_out)
