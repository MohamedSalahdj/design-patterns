from dataclasses import dataclass, field

from subscriber import Subscriber
from subscription_type import SubscriptionType
from blog import Blog
from newsletter import Newsletter


@dataclass
class BlogManagment:
    _subscribers: dict[SubscriptionType, list[Subscriber]] = field(default_factory=dict)
    _blogs: list[Blog] = field(default_factory=list)
    _newsletters: list[Newsletter] = field(default_factory=list)

    def subscribe(self, subscription_type: SubscriptionType, subscriber: Subscriber) -> None:
        self._subscribers.setdefault(subscription_type, []).append(subscriber)

    def unsubscribe(self, subscription_type: SubscriptionType, subscriber: Subscriber) -> None:
        self._subscribers.get(subscription_type).remove(subscriber)

    def add_new_blog(self, blog: Blog) -> None:
        self._blogs.append(blog)
        self.notify_subscriber(subscription_type=SubscriptionType.NEW_BLOG, message=f"New blog is added: {blog.title}")

    def add_newsletter(self, newsletter: Newsletter) -> None:
        self._newsletters.append(newsletter)
        self.notify_subscriber(subscription_type=SubscriptionType.NEWSLETTER, message=f"New newsletter is added: {newsletter.title}")

    def notify_subscriber(self, subscription_type: SubscriptionType, message: str) -> None:
        for subscriber in self._subscribers.get(subscription_type):
            subscriber.notify(notify_message=message)
