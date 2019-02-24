# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests for metadata."""

from nose.tools import assert_equals
from .._oclc import query


def test_query():
    """Test the query of metadata (oclc.org) with 'low level' queries."""
    assert_equals(len(repr(query('9780321534965'))) > 100, True)
    assert_equals(len(repr(query('9781118241257'))) > 100, True)
    assert_equals(len(repr(query('9780425284629'))) > 100, True)


def test_query_no_data():
    """Test the query of metadata (oclc.org) with 'low level' queries (no data)."""
    assert_equals(len(repr(query('9781849692341'))) == 2, True)
    assert_equals(len(repr(query('9781849692343'))) == 2, True)
