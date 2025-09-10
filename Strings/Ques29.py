# from collections import Counter
def secFrequent(self, arr, n):
        # count=Counter(arr)
        # sorted_items= sorted(count.items(),key=lambda x:x[1],reverse=True)
        # return sorted_items[1][0]


        freq=dict()
        for s in arr:
            freq[s]= freq.get(s,0)+1
            
            
        if len(freq)<2:
            return ""
            
        max_freq=-1
        sec_freq= -1
        maxstr, secstr= None, None
        
        for key,value in freq.items():
            if value>=max_freq:
                sec_freq=max_freq
                secstr=maxstr
                maxstr=key
                max_freq=value
                
            elif value>=sec_freq:
                sec_freq= value
                secstr=key
        
                