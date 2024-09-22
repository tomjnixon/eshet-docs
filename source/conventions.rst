.. _conventions:

Conventions
===========

This specification is slightly odd, because it is derived from comments in
erlang implementation files. This makes it easy to keep in sync with the
implementation, but the syntax may be unfamiliar. This also makes it harder to
fix some obvious inconsistencies, so that hasn't been done yet.

This document briefly describes most of the erlang syntax used in the rest of
the specification, with links to the erlang manual if you need more details.

Values
------

* Integers are written as decimal, or in hex as ``16#ff`` for 255.
* Atoms are values which only compare equal to themselves, and are written as
  lowercase words with underscores, like ``foo_bar``.
* Lists are written with square brackets and commas, like ``[some, atoms]``.
* Tuples are written with curly brackets and commas, like ``{a, tuple}``.
* Variables are written as a capitalised word, like ``SomeVariable``.

A complete list can be found in the `erlang data types manual`_.

.. _erlang data types manual: https://www.erlang.org/doc/system/data_types.html

Binaries
--------

A Binary is a sequence of bytes, written with double angle brackets and commas,
for example ``<<1, 2>>`` is the two-byte binary containing bytes 1 and 2. Each
element of the binary can represent more than one byte (actually, bits, but
this is not used), and the result is the concatenation of the bytes of all
elements. Elements can be:

* A plain integer value (either a literal value or variable) results in a
  single byte with the given value.
* An integer and a number of bits separated by a colon is a big-endian binary
  number, e.g. ``<<256:16>>`` is ``<<1, 0>>``.
* An existing binary value followed by ``/binary``, e.g. ``<<Foo/binary,
  Bar/binary>>`` is the concatenation of ``Foo`` and ``Bar``.

More details can be found in the `erlang bit syntax manual`_.

.. _erlang bit syntax manual: https://www.erlang.org/doc/system/bit_syntax

Types
-----

Types are generally a superset of values, so for example a value of type
``foo`` can only be the atom ``foo``. The following syntax is used to build
types that can contain more than one value:

* ``type_a | type_b``: a sum type, in this case either ``type_a`` or ``type_b``.
* ``1..5``: a range of integers, in this case between 1 and 5 inclusive.
* ``type_name()`` is a referenced to a type name defined elsewhere, including some built-in types:

  * ``binary()``: a binary string (series of bytes).
  * ``integer()``: an arbitrary-size integer.
  * ``any()``: any type.

* ``[integer()]``: a list of values, in this case, integers.

More details can be found in the  `erlang type syntax manual`_.

.. _erlang type syntax manual: https://www.erlang.org/doc/system/typespec.html

Defining Types
--------------

New types can be defined like:

.. code-block:: erlang

   -type type_name() :: type_expression.

Now, ``type_name()`` is equivalent to ``type_expression``.

The type of a function is written:

.. code-block:: erlang

   -spec func_name(argument_type) -> result_type.

Defining Functions
------------------

Functions are written with multiple patterns and bodies. A simplified example
from :ref:`binary_protocol`:

.. code-block:: erlang

    pack_payload({hello, Version, TimeoutS}) ->
        <<16#01, Version:8, TimeoutS:16>>;
    pack_payload({hello_id, Version, TimeoutS, ClientID}) ->
        <<16#02, Version:8, TimeoutS:16, (msgpack_pack(ClientID))/binary>>.

With this definition, ``pack_payload({hello, 0, 5})`` is ``<<1, 0, 0, 5>>``,
because the first pattern matches, making ``Version`` equal to 0 and
``TimeoutS`` equal to 5.

More details can be found in the `erlang function reference`_.

.. _erlang function reference: https://www.erlang.org/doc/system/ref_man_functions.html
