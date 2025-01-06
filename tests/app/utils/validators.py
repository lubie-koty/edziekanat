import pytest

from app.utils.validators import check_pesel


@pytest.mark.parametrize(
    "pesel",
    [
        "59020278737",
        "95021833999",
        "53113051461",
        "70043075154",
        "85101492983",
        "08281095162",
        "04320468553",
        "01212476465",
        "60031617961",
        "55030101193",
        "55030101230",
    ],
)
def test_check_pesel(pesel: str):
    assert pesel == check_pesel(pesel)


@pytest.mark.parametrize(
    "pesel",
    [
        "590202787371111",
        "95021833",
        "53113051462",
        "70043075155",
        "85101492984",
        "08281095167",
        "04320468550",
        "01212476460",
        "60031617911",
        "94072516899",
        "55030101231",
    ],
)
def test_check_pesel_with_errors(pesel: str):
    with pytest.raises(ValueError):
        check_pesel(pesel)
