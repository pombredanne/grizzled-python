Version 1.1.0 (24 May, 2017)

- Updated `setup.py` and `setup.cfg` to support building a wheel.
- Updated README with instructions on building, installing, and running tests.
- Removed dependency on `enum34` package.
- Added dependency on `backports.tempfile` package, to allow using
  `with TemporaryDirectory()` on both Python 3 and Python 2.
- `grizzled.file.eglob` is now lazy, returning a generator, rather than a list.  
- Added tests for `grizzled.file.eglob`.  

Version 1.0.5 through 1.0.7 (12 February, 2016)

- Additional changes to support Python 3.

Version 1.0.4 (11 February, 2016)

- Changed dependency on `enum` to dependency on `enum34`, for compatibility
  between Python 2 and Python 3.

Version 1.0.3 (25 May, 2012)

- Merged pull request from github.com/cr33dog, which adds
  `from __future__ import with_statement` imports to `setup.py` and
  one unit test, to support older versions of Python.

---------------------------------------------------------------------------
Version 1.0.2 (29 May, 2011)

* Added installation dependency on `enum` module.

---------------------------------------------------------------------------
Version 1.0.1 (29 May, 2011)

* Changed `grizzled.net.ftp.parse` to support the FTP `MLST` command,
  based on (largely unmodified) code contributed by Andrew Scheller
  (*gcode /at/ loowis.durge.org*).
* Added `java` to the list of operating system types in `grizzled.os`,
  for Jython.
* Changed `setup.py` to copy stuff to the `gh-pages` directory, via local
  "gh" command.

---------------------------------------------------------------------------
Version 1.0 (14 March, 2011)

* Added `grizzled.proxy.Forwarder`, a mixin that aids writing wrappers that
  forward some, or all, unknown attributes to a wrapped object.
* Graduated to 1.0. It's been around long enough.
* Removed `setup.py` reliance on `ez_setup` module.
* Removed `grizzled.collections.namedtuple`.

---------------------------------------------------------------------------
Version 0.9.4 (10 June, 2010)

* Fixed various incorrect docstrings.
* Added `grizzled.file.list_recursively()` function.
* Fixes for PyPI.

---------------------------------------------------------------------------
Version 0.9.3 (24 October, 2009)

* Updated to latest `ez_setup.py`
* Fixed `grizzled.text.hexdump()` to honor `show_repeats=True` in all cases.

* Added `pidfile` argument to `grizzled.os.daemonize()`. `grizzled.os.spawnd()`
  was passing a `pidfile` argument to `daemonize()`, but `daemonize()`
  didn't support it.

---------------------------------------------------------------------------
Version 0.9.2 (26 May, 2009)

* Added `grizzled.misc.bitcount()`, to calculate the number of 1 bits in a
  number.
* Modified `grizzled.db` for Oracle so that `get_tables()` uses `ALL_TABLES`,
  not `USER_TABLES` (suppressing tables with "$" in them). Made similar change
  for `get_indexes()`.
* Moved `grizzled.misc.str2bool()` to `grizzled.text.`

---------------------------------------------------------------------------
Version 0.9.1 (5 December, 2008)

* Added missing import of `re` module to `grizzled.db.sqlite` module.
* Move `grizzled/net.py` to `grizzled/net/__init__.py`.
* Added `grizzled.net.ftp` package and `grizzled.net.ftp.parse` module, the
  latter containing a Python port of Dan Bernstein's `ftpparse` function,
  for parsing output from an FTP server's "LIST" command.

---------------------------------------------------------------------------
Version 0.9 (13 November, 2008)

* Added `get_rdbms_metadata()` function to `grizzled.db` drivers, to return
  information about the underlying RDBMS.
* Added `grizzled.collections.namedtuple()` function, which works like
  Python's new 2.6 `namedtuple()` function. If running under 2.6, the
  `grizzled.collections` version *is* the 2.6 `namedtuple()` function.
* Reorganized internals of `grizzled.db` for easier maintenance. Has no
  effect on the visible API.
* Moved package metadata from `setup.py` to `grizzled/__init__.py`, making
  it easier for other packages to use.

---------------------------------------------------------------------------
Version 0.8.4 (4 November, 2008)

* Improved Oracle support in `grizzled.db` package.

---------------------------------------------------------------------------
Version 0.8.3 (1 November, 2008)

* Added `@unimplemented` decorator
* Fixed bad references to `os` module in `grizzled.os.daemonize()`.
* Renamed `grizzled.cmdline.CommandLineParser's` `show_usage()` method to
  `die_with_usage()`. Provided a deprecated version of `show_usage()`.
* Added `init_simple_stream_logging()` to `grizzled.log` module.
* Added `get_one_of()` method to `grizzled.config.Configuration`
* Removed reference to nonexistent `InfoFilter` from `grizzled.log`

---------------------------------------------------------------------------
Version 0.8.2 (8 September, 2008)

* Eliminated extra `fork()` in `grizzled.os.spawnd()` function.
* Added `grizzled.collections.LRUDict` class, implementating a fixed-size
  dictionary with least recently used semantics.
* The `grizzled.text` module now provides a `hexdump()` function.
* The `grizzled.text` module now provides a `str2bool()` function.
* `grizzled.file.include` module's `preprocess()` method is now a little more
  careful about temp file turds.
* Fixed some unconverted camelCase variables in `grizzled.file.include`
  module's `preprocess()` method, removing some runtime errors.
* Now properly bundles `ez_setup.py`
* `grizzled.db.DBDriver` now implements `paramstyle()` method that actually
  does something.
* `grizzled.db` now has simple support for the Gadly pure-Python SQL
  database. (See http://gadfly.sourceforge.net/)

---------------------------------------------------------------------------
Version 0.8.1 (5 August, 2008)

* `grizzled.db` now uses SQLite3 PRAGMAs to get table metadata and index
  metadata.

---------------------------------------------------------------------------
Version 0.8 (22 July, 2008)

* Added `grizzled.log` module (including a `WrappingLogFormatter` class)
  which contains some classes and functions for use with the standard
  logging module.
* Added `grizzled.misc.str2bool()` function.

---------------------------------------------------------------------------
Version 0.7.2 (18 July, 2008)

* Added `grizzled.history`.
* Converted some lingering Epytext markup to reStructuredText.

---------------------------------------------------------------------------
Version 0.7.1 (16 July, 2008)

* Added `grizzled.misc` module and `ReadOnly` class.
* Added the `spawnd()` function the `grizzled.os` module.
* Enhanced `grizzled.db SQLite3` driver to return better index and table
  metadata.

---------------------------------------------------------------------------
Version 0.7 (12 June, 2008)

* Deprecated `grizzled.os.file_separator()`. Silly me, there's a standard
  `os.path.sep` variable.
* In `grizzled.db`, the MySQL index metadata function wasn't detecting column
  uniqueness properly.
* In `grizzled.db`, the PostgreSQL table metadata function wasn't detecting
  NULL/NOT NULL properly.
* Added `find_command()` and `path_elements()` functions to `grizzled.os`.
* Documentation format changed from default Epydoc to reStructuredText.
* Fixed bug in `grizzled.db.add_driver()` function that prevented a driver
  from being added programmatically.
* Added `class_for_name()` function to `grizzled.system` module.
* `grizzled.config` now uses `grizzled.collections.OrderedDict`
* In `grizzled.config`, `Configuration.sections()` is now a property.

---------------------------------------------------------------------------
Version 0.6 (30 May, 2008)

* Removed deprecated methods.
* Removed deprecated `optparse` module.
* Added MySQL-specific logic for table metadata to `grizzled.db`
* Added PostgreSQL-specific logic for table metadata to `grizzled.db`
* Added ability to retrieve list of database tables to `grizzled.db`.
* Added `grizzled.io.filelock.locked_file()` function, for use with the
  `with` statement.

---------------------------------------------------------------------------

Version 0.5 (28 May, 2008)

* Added `grizzled.sys` module, with `python_version()`,
  `python_version_string()`, `split_python_version()` and
  `ensure_version()` functions.
* Added `grizzled.file.universal_path()` and `grizzled.file.native_path()`.
  A universal path always uses a '/' as the file separator, no matter what
  the underlying operating system uses. A native path uses the underlying
  operating system's path separator. These two functions convert between the
  two notations.
* Fixed bug in `grizzled.file.eglob()` stemming from camel case conversion.
* Added `grizzled.os.file_separator()` function.
* Changed `grizzled.os.get_path_separator()` to `grizzled.os.path_separator()`.

---------------------------------------------------------------------------

Version 0.4 (20 May, 2008)

* Converted public functions, methods, parameters and variables that use
  camel case names to names that are more consistent with standard Python
  naming conventions. Existing camel case functions are still in the API,
  but are deprecated. Calling them will result in a runtime warning.

---------------------------------------------------------------------------

Version 0.3 (8 May, 2008)

* Created `grizzled.io.filelock` module, with a `FileLock` class that
  provides a portable file locking interface.
* Added `grizzled.file.eglob()` function.
* Added `grizzled.os.withDirectory()`, a context manager for the `with`
  statement.
* Added `grizzled.io.PushbackFile` class
* Added `grizzled.file.copyRecursively()` function
* Moved `CommandLineParser` from `grizzled.optparse` to `grizzled.cmdline`
* Augmented `CommandLineParser` to permit specifying an epilogue to be printed
  at the end of the usage message.
* Added `grizzled.net.download()` function
* Added `grizzled.io.Zip` class

---------------------------------------------------------------------------

Version 0.2 (2 April, 2008)

* Initial version posted to the web.
