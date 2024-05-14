import pytest
from source.app import name

def test_app():
  assert name == "Bartek"
