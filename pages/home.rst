Presentation
============

Pyphen is a pure Python module to hyphenate text using included or external
Hunspell hyphenation dictionaries.

Usage
=====

.. code-block:: python

   >>> import pyphen
   >>> 'nl_NL' in pyphen.LANGUAGES
   True
   >>> dic = pyphen.Pyphen(lang='nl_NL')
   >>> dic.inserted('lettergrepen')
   'let-ter-gre-pen'
   >>> dic.wrap('autobandventieldopje', 11)
   ('autoband-', 'ventieldopje')
   >>> for pair in dic.iterate('Amsterdam'):
   ...     print(pair)
   ...
   ('Amster', 'dam')
   ('Am', 'sterdam')

Features
========

- 100% pure Python with no dependencies
- a lot of included dictionaries
- caches dict files and hyphenated words
- supports nonstandard hyphenation patterns

Included Dictionaries
=====================

The dictionaries included in LibreOffice are distributed with Pyphen:

- Afrikaans
- Bulgarian
- Catalan
- Croatian
- Czech
- Danish
- Dutch
- English
- Estonian
- French
- Galician
- German
- Greek
- Hungarian
- Italian
- Lithuanian
- Latvian
- Norwegian Bokmål
- Norwegian Nynorsk
- Polish
- Portuguese
- Romanian
- Russian
- Serbian (cyrillic and latin)
- Slovak
- Slovenian
- Swedish
- Telugu
- Ukrainian
- Zulu

Download
========

Pyphen is `available on PyPI <http://pypi.python.org/pypi/Pyphen/>`_. To
install, just type ``pip install pyphen`` as superuser.

If you want the development version, take a look at the :codelink:`git
repository on GitHub`, or clone it thanks to ``git clone
git://github.com/Kozea/Pyphen.git``.

You can also download `the Pyphen package of the git repository
<https://github.com/Kozea/Pyphen/tarball/master>`_.


Contribute
==========

Features, bugs, hacks, documentation, tests, dictionaries? Fork us on
:codelink:`GitHub`, or chat with us on IRC (``##kozea`` on Freenode).

License
=======

Pyphen is a friendly fork of the unmaintained `python-hyphenator
<https://code.google.com/p/python-hyphenator/>`_ module.

Pyphen is released under the GPL 2.0+ ~ LGPL 2.1+ ~ MPL 1.1 tri-license.  See
``COPYING.GPL``, ``COPYING.LGPL`` and ``COPYING.MPL`` for more details.

The dictionaries included in Pyphen come from the LibreOffice’s git repository
and are distributed under GPL, LGPL and/or MPL. See the dictionaries and `the
LibreOffice's repository
<http://cgit.freedesktop.org/libreoffice/dictionaries/tree/>`_ for more details.
