"""WA Department of Fire and Emergency Services (DFES) feed entry."""

from georss_client import FeedEntry

from .consts import (
    ATTRIBUTION,
    REGEXP_ATTR_CATEGORY_ALL_INCIDENTS,
    REGEXP_ATTR_CATEGORY_WARNINGS,
    REGEXP_ATTR_REGION,
    XML_TAG_DFES_REGION,
)


class WaDfesFeedEntry(FeedEntry):
    """Department of Fire and Emergency Services (DFES) feed entry."""

    def __init__(self, home_coordinates, rss_entry):
        """Initialise this service."""
        super().__init__(home_coordinates, rss_entry)

    @property
    def attribution(self) -> str:
        """Return the attribution of this entry."""
        return ATTRIBUTION


class WaDfesWarningsFeedEntry(WaDfesFeedEntry):
    """Department of Fire and Emergency Services (DFES) Warnings feed entry."""

    @property
    def category(self) -> str:
        """Return the type of this entry."""
        return self._search_in_description(REGEXP_ATTR_CATEGORY_WARNINGS)

    @property
    def region(self) -> str | None:
        """Return the region of this entry."""
        if self._rss_entry:
            return self._rss_entry.get_additional_attribute(XML_TAG_DFES_REGION)
        return None


class WaDfesAllIncidentsFeedEntry(WaDfesFeedEntry):
    """Department of Fire and Emergency Services (DFES) All Incidents feed entry."""

    @property
    def category(self) -> str:
        """Return the type of this entry."""
        return self._search_in_description(REGEXP_ATTR_CATEGORY_ALL_INCIDENTS)

    @property
    def region(self) -> str:
        """Return the region of this entry."""
        return self._search_in_description(REGEXP_ATTR_REGION)
