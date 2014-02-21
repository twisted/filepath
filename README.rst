filepath 0.1

What is this?
=============

  filepath is an object-oriented API for manipulating filesystem paths on
  POSIX and Windows.  Its primary goal is to provide APIs which are less
  prone to bugs and security issues than the standard Python os.path APIs.
  Additionally, it offers access to the contents of zip archives via an
  alternate implementation of the same API used for accessing a normal
  filesystem.

  filepath is an independent package of the twisted.python.filepath module.
  Therefore, while this is a brand new package, the code is mature and has
  already seen a great deal of real-world use.

  Because of this, all bug reports should be submitted upstream to Twisted.

Compatibility
=============

  filepath is intended to be as compatible with twisted.python.filepath as
  possible.  All changes will be made in twisted.python.filepath first and
  then migrated to filepath.

  As a consequence, filepath inherits Twisted's policies regarding backwards
  compatibility.  As an exception, however, filepath will make no backwards
  compatibility guarantees for its first few releases.

Installing
==========

  Instructions for installing this software are in INSTALL.

Unit Tests
==========

  For simplicity of maintenance, filepath's unit tests depend on Twisted
  Trial.  You will only be able to run them with Twisted installed.  This is
  the only part of filepath which depends on Twisted.

  You can run the tests with the Trial runner:

    $ trial filepath

  You can probably run them with the stdlib unittest runner, but I can't
  figure out how right now.
