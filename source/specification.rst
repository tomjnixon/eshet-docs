.. _specification:

ESHET Protocol Specifications
=============================

This section loosely defines the protocols used by ESHET clients to talk to an
ESHET server, including a :ref:`binary protocol <binary_protocol>` for
communication over TCP sockets and a :ref:`wesocket protocol
<websocket_protocol>` for use by web clients.

Both are defined as a serialisation of an :ref:`generic protocol
<generic_protocol>`, using common :ref:`conventions <conventions>`.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   conventions
   protocol
   binary_protocol
   websocket_protocol
