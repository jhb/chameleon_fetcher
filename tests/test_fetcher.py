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
    cf = ChameleonFetcher(template_dir, one=True, two=False, three=True, four=False, five=True, six=False)
    out = cf('boolean')
    expected = ('<option selected="selected">One</option>\n'
                '<option>Two</option>\n'
                '\n'
                '<input type="checkbox" checked="checked">Three\n'
                '<input type="checkbox">Four\n'
                '\n'
                '<option disabled="disabled">Five</option>\n'
                '<option>Six</option>\n'
                )
    assert out == expected
