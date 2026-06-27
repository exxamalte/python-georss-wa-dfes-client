"""WA Department of Fire and Emergency Services (DFES) constants."""

from typing import Final

from georss_client.consts import CUSTOM_ATTRIBUTE

ADDITIONAL_NAMESPACES: Final = {"http://emergency.wa.gov.au/xmlns/dfes": "dfes"}

ATTRIBUTION: Final = "Department of Fire and Emergency Services"

REGEXP_ATTR_CATEGORY_WARNINGS: Final = (
    f"<b>Category: </b>(?P<{CUSTOM_ATTRIBUTE}>[^<]+)</div>"
)
REGEXP_ATTR_CATEGORY_ALL_INCIDENTS: Final = f"^(?P<{CUSTOM_ATTRIBUTE}>[^<]+) <"
REGEXP_ATTR_REGION: Final = f"<region>(?P<{CUSTOM_ATTRIBUTE}>[^<]+)</region>"

URL_PREFIX: Final = "https://www.emergency.wa.gov.au/data/"
URLS: Final = {
    "warnings": URL_PREFIX + "message.rss",
    "all_incidents": URL_PREFIX + "incident_FCAD.rss",
}

XML_TAG_DFES_REGION: Final = "dfes:region"
