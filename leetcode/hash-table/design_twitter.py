class Twitter:

    def __init__(self):
        self.following = dict()
        self.tweets = dict()

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[tweet_id] = user_id

    def getNewsFeed(self, user_id: int) -> list:
        result = []
        keys = list(reversed(self.tweets.keys()))
        for key in keys:
            if (self.following.get(user_id) and self.tweets[key] in self.following[user_id]) or \
                    self.tweets[key] == user_id:
                result.append(key)
            if len(result) == 10:
                break
        return result

    def follow(self, follower_id: int, followed_id: int) -> None:
        if self.following.get(follower_id):
            self.following[follower_id].add(followed_id)
        else:
            self.following[follower_id] = {followed_id}

    def unfollow(self, follower_id: int, followed_id: int) -> None:
        if self.following.get(follower_id) and followed_id in self.following[follower_id]:
            self.following[follower_id].remove(followed_id)
