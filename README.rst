*******
pythOCR
*******

.. contents::

Overview
========

This project intends to accomplish the following goals

  * Ability to recognize handwritten numbers and arithmetic operators
    (``+``, ``-``, ``/``, ``*``, ``=``) in real-time from a video feed
  * Arithmetic expressions are parsed by the software into a plain-text format
  * The expression is sent to WolframAlpha (api?) 
  * The result is displayed on the screen
  
Roadmap
=======

  * Ability to read expressions from video feed

    - efficient means to extract video frames and resample if needed
    - fast edge detection on said frames
    - custom algorithm needed for symbol detection

      + Standard OCR will not work (eg. pyTesseract)

    - validation & sanity checking

  * Ability to evaluate expression through Wolfram (or similar)

    - API available?
    - If not, is the webpage scrape-able

  * Ability to display results

    - Load browser in frame with query result? 

      + Possibly easiest method; query can be inserted into URL without needing 
        any API call

    - Parse results and convert to alternate format? 

Tooling
=======
  
+----------------------------------------------------------------+------------------------------+
| Tool                                                           | Function                     |
+================================================================+==============================+
| Python 3.X                                                     | implementation language      |
+----------------------------------------------------------------+------------------------------+
| scikit                                                         | edge detection               |
+----------------------------------------------------------------+------------------------------+
| numpy                                                          | general purpose math library |
+----------------------------------------------------------------+------------------------------+
| `umlet <http://www.umlet.com/>`_                               | diagramming                  |
+----------------------------------------------------------------+------------------------------+
| `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ | documentation language       |
+----------------------------------------------------------------+------------------------------+

