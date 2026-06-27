"""WA Department of Fire and Emergency Services (DFES) feed manager."""

from georss_client.feed_manager import FeedManagerBase

from .feed import WaDfesFeed


class WaDfesFeedManager(FeedManagerBase):
    """Feed Manager for Department of Fire and Emergency Services feed."""

    def __init__(
        self,
        generate_callback,
        update_callback,
        remove_callback,
        coordinates: tuple[float, float],
        feed: str,
        filter_radius: float | None = None,
        filter_categories=None,
    ):
        """Initialize the DFES Feed Manager."""
        feed = WaDfesFeed(
            coordinates,
            feed,
            filter_radius=filter_radius,
            filter_categories=filter_categories,
        )
        super().__init__(feed, generate_callback, update_callback, remove_callback)
