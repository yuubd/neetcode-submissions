class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        set or map
        Need a map of the string that represents the counts of the word eg. abc => 111000... alphabet counter
        key:alphabet counter, val is a list of words
        reuturn the values
        
        for each word
            create counter string
            see if the string is found in the map
            if not, add the key and the val array with the word
            if found, append in the value
        return the list of values        
        '''

        d = defaultdict(list)

        for word in strs:
            counter = self.create_counter(word)
            d[counter].append(word)
        
        return [v for v in d.values()] # generator


    def create_counter(self, w):
        counter = [0] * 26
        for char in w:
            counter[ord(char) - ord('a')] += 1 
        counter = tuple(counter) # ['1','0']
        print(counter)
        return counter