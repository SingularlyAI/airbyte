#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

import datetime

import pytest
from airbyte_cdk.sources.declarative.interpolation.macros import macros


@pytest.mark.parametrize(
    "test_name, fn_name, found_in_macros",
    [
        ("test_now_local", "now_local", True),
        ("test_now_utc", "now_utc", True),
        ("test_today_utc", "today_utc", True),
        ("test_max", "max", True),
        ("test_day_delta", "day_delta", True),
        ("test_format_datetime", "format_datetime", True),
        ("test_duration", "duration", True),
        ("test_not_a_macro", "thisisnotavalidmacro", False),
    ],
)
def test_macros_export(test_name, fn_name, found_in_macros):
    if found_in_macros:
        assert fn_name in macros
    else:
        assert fn_name not in macros


def test_format_datetime():
    format_datetime = macros["format_datetime"]
    assert format_datetime("2022-01-01T01:01:01Z", "%Y-%m-%d") == "2022-01-01"
    assert format_datetime(datetime.datetime(2022, 1, 1, 1, 1, 1), "%Y-%m-%d") == "2022-01-01"


def test_duration():
    duration = macros["duration"]
    assert duration("P1D") == datetime.timedelta(days=1)
