from abc import ABC, abstractmethod
from dataclasses import dataclass
from time import time


class SocialChannel(ABC):
    def __init__(self, followers: int):
        self.followers = followers

    @abstractmethod
    def post_a_message(self, message: str):
        pass


class YouTubeChannel(SocialChannel):
    def post_a_message(self, message: str):
        print(f"YouTube: {message}")


class FacebookChannel(SocialChannel):
    def post_a_message(self, message: str):
        print(f"Facebook: {message}")


class TwitterChannel(SocialChannel):
    def post_a_message(self, message: str):
        print(f"Twitter: {message}")


@dataclass
class Post:
    message: str
    timestamp: int

    def is_time_to_publish(self, publish_time: int):
        return self.timestamp <= publish_time


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    current_time = time()
    for post in posts:
        if post.is_time_to_publish(current_time):
            for channel in channels:
                channel.post_a_message(post.message)


process_schedule(
    [
        Post("Past post 1", timestamp=int(time()) - 10),
        Post("Current post", timestamp=int(time())),
        Post("Not yet.", timestamp=int(time()) + 60),
        Post("Past post 2", timestamp=int(time()) - 20)
    ],
    [
        YouTubeChannel(followers=100),
        FacebookChannel(followers=50),
        TwitterChannel(followers=222)
    ]
)
