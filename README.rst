===============================
🍌🥧: Banano Python Library
===============================

.. image:: https://img.shields.io/pypi/l/bananopy.svg
    :target: https://github.com/milkyklim/bananopy/blob/master/LICENSE
    :alt: License

.. image:: https://github.com/milkyklim/bananopy/workflows/CI/badge.svg
    :target: https://github.com/milkyklim/bananopy/actions
    :alt: Build Status

.. image:: https://img.shields.io/github/workflow/status/milkyklim/bananopy/CI?label=docs
    :target: https://milkyklim.github.io/bananopy
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/pyversions/bananopy.svg
    :target: https://pypi.python.org/pypi/
    :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/v/bananopy.svg
    :target: https://pypi.python.org/pypi/bananopy
    :alt: Package Version

.. image:: https://img.shields.io/badge/Banano%20Node-v20.0-yellow
    :alt: Banano Node Version

🍌🥧 is a python wrapper for Banano node communication.
It takes care of RPC responses (type conversions) and exposes a pythonic API for making RPC calls.

Full list of RPC calls is coming from `docs <https://docs.nano.org/commands/rpc-protocol/>`_.

**Setup**

.. code-block:: bash

    pip install bananopy

Bananopy checks if ``BANANO_HTTP_PROVIDER_URI`` environment variable is set.

To set it run:

.. code-block:: bash

    export BANANO_HTTP_PROVIDER_URI=<ip_address>


Otherwise, bananopy will fallback and use public node (``https://api-beta.banano.cc``) for API calls.

**Note:** Public node is running Banano Node v18, meaning some requests might fail.

**Development**

Repository uses `poetry <https://python-poetry.org/>`_ to keep track of dependances. Once you have poetry installed make sure
you are on Python 3.7+ and run these commands:

.. code-block:: bash

    git clone https://github.com/milkyklim/bananopy.git
    poetry install

To run the tests:

.. code-block:: bash

    poetry run pytest -v

**Note:** Only public requests are actually tested. Dangerous RPC calls controlled by ``enable_control`` are checked for error response only.

**Conversion**

``float`` type is not supported in conversion, e.g. ``ban_to_banoshi`` cause it might lead to unexpected precision loss.
Use ``str``, ``int`` or ``Decimal`` types instead.

**Example**

.. code-block:: python

    >>> import bananopy.banano as ban
    Using https://api-beta.banano.cc as API provider on port 443

    >>> account = "ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr"
    >>> ban.account_balance(account)
    {'balance': 1626688000000000000017763568393401, 'pending': 0}

**Support**

Benis to ``ban_1dsarukqn5y8oqho43praocn97wjs17t8eppzgfb78nzzxmjapkidxrcgsqc``
