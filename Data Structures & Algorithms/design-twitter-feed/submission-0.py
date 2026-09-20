"""
following = {} #userId -> set(userId)
tweets = {} #userId -> [(timestamp, tweetId)]

getNewsFeed:
    - loop through all users in following
    - put all tweets into a max heap
    - return most recent 10 id's
"""
import heapq
class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        if userId in self.tweets:
            all_tweets.extend(self.tweets[userId])
        if userId in self.following:
            for user in self.following[userId]:
                if user in self.tweets:
                    all_tweets.extend(self.tweets[user])
        
        heapq.heapify(all_tweets)
        result = []
        for _ in range(10):
            if not all_tweets:
                break
            result.append(heapq.heappop(all_tweets)[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
