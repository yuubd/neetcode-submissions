class Twitter:

    def __init__(self):
        self.follower_to_followees = defaultdict(set)
        self.userID_to_tweets = defaultdict(deque)
        self.time_stamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userID_to_tweets[userId].append([self.time_stamp, tweetId])
        self.time_stamp += 1
        
        if len(self.userID_to_tweets[userId]) > 10:
            self.userID_to_tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        allUserIDs = self.follower_to_followees[userId].copy()
        allUserIDs.add(userId)

        h = []
        # Generate a heap of posts for each userid. 
        # Need the last index or idx-1 to keep track of the next after pop
        for uID in allUserIDs:
            tweets = self.userID_to_tweets[uID]
            if len(tweets) == 0:
                continue
            idx = len(tweets)-1
            [time, tweetID] = tweets[idx]
            
            # -time: to place most recent tweet at the top of heap
            # tweetID to return and order after time
            # uID to find the tweets for next
            # len(tweets)-1: the last(most recent) idx of the user's tweets
            tweetData = [-time, tweetID, uID, idx-1]
            heapq.heappush(h, tweetData)
        
        res = []
        # while we havent collected 10 tweets or there is still sth in the heap
        while not (len(res) == 10 or len(h) == 0):
            # most recent tweet heappop
            [_, tweetID, uID, nextIdx] = heapq.heappop(h)
            res.append(tweetID)
            
            # next tweet to backfill
            if nextIdx >= 0:
                tweets = self.userID_to_tweets[uID]
                [time, tweetID] = tweets[nextIdx]
                tweetData = [-time, tweetID, uID, nextIdx-1]
                heapq.heappush(h, tweetData)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_followees[followerId].discard(followeeId)
        
