# Kirjoita postinumerot-moduulin testit tähän tiedostoon
from postinumerot import hae_postitoimipaikat

MOCK_TEST_DATA = {
    "12345": "NAPAPIIRI"
}

SPECIAL_CASES = {
    "12345": "SMARTPOST",
    "45678": "SMART POST"
}


def test_finding_one_postalcode():
    assert hae_postitoimipaikat("särkisalmi") == ["59310"]


def test_finding_multiple_postalcodes():
    assert hae_postitoimipaikat("Parikkala") == ["59100", "59101"]


def test_finding_no_postalcodes():
    assert hae_postitoimipaikat("Ihantala") == []


def test_using_mock_data(mocker):
    mocker.patch("postinumerot.hae_p_numerot", return_value=MOCK_TEST_DATA)
    assert hae_postitoimipaikat("Napapiiri") == ["12345"]


def test_for_smart_post_with_spaces(mocker):
    mocker.patch("postinumerot.hae_p_numerot", return_value=SPECIAL_CASES)
    assert hae_postitoimipaikat("smart post") == ["12345", "45678"]


def test_for_smart_post_without_spaces(mocker):
    mocker.patch("postinumerot.hae_p_numerot", return_value=SPECIAL_CASES)
    assert hae_postitoimipaikat("smartpost") == ["12345", "45678"]
