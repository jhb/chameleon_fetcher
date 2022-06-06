import os

import pytest

from chameleon_fetcher import ChameleonFetcher


@pytest.fixture
def template_dir():
    return os.path.join(os.path.dirname(__file__), 'templates')


def test_simple(template_dir):
    """Just check that it works"""
    cf = ChameleonFetcher(template_dir, some_var=42)
    output = cf('simple', myvar='test')
    assert output == '<test>simple test 42</test>'


def test_boolean(template_dir):
    """"Boolean attributes are needed for options and checkboxes"""
    cf = ChameleonFetcher(template_dir, one=True, two=False, three=True, four=False)
    out = cf('boolean')
    expected = ('<option selected="selected">one</option>\n'
                '<option>two</option>\n'
                '\n'
                '<input type="checkbox" checked="checked">Three\n'
                '<input type="checkbox">Four\n')
    assert out == expected
