"""WA Department of Fire and Emergency Services (DFES) constants."""

from georss_client.consts import CUSTOM_ATTRIBUTE

ADDITIONAL_NAMESPACES = {"http://emergency.wa.gov.au/xmlns/dfes": "dfes"}
ATTRIBUTION = "Department of Fire and Emergency Services"
REGEXP_ATTR_CATEGORY_WARNINGS = f"<b>Category: </b>(?P<{CUSTOM_ATTRIBUTE}>[^<]+)</div>"
REGEXP_ATTR_CATEGORY_ALL_INCIDENTS = f"^(?P<{CUSTOM_ATTRIBUTE}>[^<]+) <"
REGEXP_ATTR_REGION = f"<region>(?P<{CUSTOM_ATTRIBUTE}>[^<]+)</region>"
URL_PREFIX = "https://www.emergency.wa.gov.au/data/"
URLS = {
    "warnings": URL_PREFIX + "message.rss",
    "all_incidents": URL_PREFIX + "incident_FCAD.rss",
}
XML_TAG_DFES_REGION = "dfes:region"
