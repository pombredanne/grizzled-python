#!/usr/bin/env python
#
# $Id$
# ---------------------------------------------------------------------------

"""
Deprecated in favor of the L{C{cmdline}<cmdline>} module.
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import warnings
from . import cmdline

# ---------------------------------------------------------------------------
# Exports
# ---------------------------------------------------------------------------

_all__ = ['CommandLineParser']

# ---------------------------------------------------------------------------
# Public symbols
# ---------------------------------------------------------------------------

CommandLineParser = cmdline.CommandLineParser

warnings.warn('grizzled.optparser is deprecated. Use grizzled.cmdline')