
"is_url()" filter
=================

The ``is_url()`` filter returns true if the specified text is a link, otherwise it returns false.

The filter reacts to links with and without protocol ("https://", "http://", etc.).

What kind of arguments does it take "is_url()"
----------------------------------------------

.. code-block:: python

   is_url(
       text: str       # Any string is accepted
   ) -> bool       # Returns a boolean value (true/false)

"is_url" usage example
----------------------

URL with protocol
^^^^^^^^^^^^^^^^^

.. code-block:: python


   import datasifter as ds

   text = "https://github.com"

   if ds.is_url(text):
       print("URL!")
   else:
       print("Not URL!")

In this example we specify the text where the link with the protocol is, then we check if it is a link by calling the ``is_url()`` function from the DataSifter module. The output will be "URL!" since the text is a link

URL without protocol
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import datasifter as ds

   text = "github.com"

   if ds.is_url(text):
       print("URL without protocol!")
   else
       print("Not URL!")

In this example we also specify the text where the link is already without protocol, then we check if it is a link by calling the ``is_url()`` function from the DataSifter module. The output will be "URL without protocol!" since the text is a link

Not URL
^^^^^^^

.. code-block:: python

   import datasifter as ds

   text = "PyPi is amazing!"

   if ds.is_url(text):
       print("It's link!")
   else:
       print("It's just text!")

In the example shown here we specify a plain text without protocols and subdomains, then we check if it is a link by calling the ``is_url()`` function from the DataSifter module. The output will be "It's just text!" since the text **isn't** a link
