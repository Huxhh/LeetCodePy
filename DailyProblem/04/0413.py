# coding=utf-8
# author huxh
# time 2020/4/13 11:01 AM


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts.append((userId, tweetId))
        if userId not in self.users:
            self.users[userId] = []

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        u = [userId]
        if userId in self.users:
            for followee in self.users[userId]:
                u.append(followee)
        res = []
        for i in range(len(self.posts) - 1, -1, -1):
            uid, pid = self.posts[i]
            if uid in u:
                res.append(pid)
            if len(res) >= 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:
            self.users[followerId] = []
        self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.users and followerId != followeeId and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

