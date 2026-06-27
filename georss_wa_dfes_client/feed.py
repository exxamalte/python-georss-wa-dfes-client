"""WA Department of Fire and Emergency Services (DFES) feed."""

import logging

from georss_client import GeoRssFeed
from georss_client.exceptions import GeoRssException

from georss_wa_dfes_client import (
    ADDITIONAL_NAMESPACES,
    URLS,
    WaDfesAllIncidentsFeedEntry,
    WaDfesWarningsFeedEntry,
)

_LOGGER = logging.getLogger(__name__)


class WaDfesFeed(GeoRssFeed):
    """Department of Fire and Emergency Services (DFES) feed."""

    def __init__(
        self, home_coordinates, feed, filter_radius=None, filter_categories=None
    ):
        """Initialise this service."""
        if feed in URLS:
            super().__init__(
                home_coordinates,
                URLS[feed],
                filter_radius=filter_radius,
                filter_categories=filter_categories,
            )
            self._feed = feed
        else:
            _LOGGER.error("Unknown feed category %s", feed)
            raise GeoRssException("Feed category must be one of %s")

    def _new_entry(self, home_coordinates, rss_entry, global_data):
        """Generate a new entry."""
        if self._feed == "warnings":
            return WaDfesWarningsFeedEntry(home_coordinates, rss_entry)
        if self._feed == "all_incidents":
            return WaDfesAllIncidentsFeedEntry(home_coordinates, rss_entry)
        return None

    def _additional_namespaces(self):
        """Provide additional namespaces, relevant for this feed."""
        return ADDITIONAL_NAMESPACES

    def _filter_entries(self, entries):
        """Filter the provided entries."""
        entries = super()._filter_entries(entries)
        if self._filter_categories:
            return list(
                filter(lambda entry: entry.category in self._filter_categories, entries)
            )
        return entries
