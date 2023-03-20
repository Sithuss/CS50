import seasons
from datetime import date
import sys

def test_seasions():
    assert seasons.get_date("2000-5-16") == date(2000, 5, 16)
