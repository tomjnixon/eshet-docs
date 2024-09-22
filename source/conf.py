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

with (
    open("../submodules/eshetsrv/apps/eshetproto/src/messages.hrl") as f_in,
    open("protocol.rst", "w") as f_out,
):
    deliterate(f_in, f_out)
