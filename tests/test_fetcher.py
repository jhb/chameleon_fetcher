import os

import pytest

from chameleon_fetcher import ChameleonFetcher, all_boolean_attributes


@pytest.fixture
def template_dir():
    return os.path.join(os.path.dirname(__file__), 'templates')


def test_simple(template_dir):
    """Just check that it works"""
    cf = ChameleonFetcher(template_dir, some_var=42)
    output = cf('simple', myvar='test')
    assert output == '<test>simple test 42</test>'


@pytest.mark.parametrize('bool_name', all_boolean_attributes)
def test_boolean_true(template_dir, bool_name):
    cf = ChameleonFetcher(template_dir)
    values = {bool_name: True}
    out = cf('boolean', values=values)
    assert f'<div id="{bool_name}" {bool_name}="{bool_name}"></div>' in out


@pytest.mark.parametrize('bool_name', all_boolean_attributes)
def test_boolean_false(template_dir, bool_name):
    cf = ChameleonFetcher(template_dir)
    values = {bool_name: False}
    out = cf('boolean', values=values)
    assert f'<div id="{bool_name}"></div>' in out


def test_boolean_other_true(template_dir):
    cf = ChameleonFetcher(template_dir)
    values = {'other': True}
    out = cf('boolean', values=values)
    assert f'<div id="other" other="True"></div>' in out


def test_boolean_other_false(template_dir):
    cf = ChameleonFetcher(template_dir)
    values = {'other': False}
    out = cf('boolean', values=values)
    assert f'<div id="other" other="False"></div>' in out
