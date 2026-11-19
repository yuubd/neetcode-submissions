class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        ''' 9:57 paused at 10:04 resume at 10:09 stop at 36
            
            "255.0.0.7", n = 2
            "255.0.0.7" ~ "255.0.0.8"
             0000 0111     0000 1000
            
            ["255.0.0.7/32", "255.0.0.8/32"]
             0000 0111 => "255.0.0.7/32" 
             0000 1000 => "255.0.0.8/32"
             No range
            

            "255.0.0.7", n = 3
            "255.0.0.7" ~ "255.0.0.9"
             0000 0111     0000 1001
            
            ["255.0.0.7/32", "255.0.0.8/31"]
             0000 0111 => "255.0.0.7/32" 
             0000 100X => "255.0.0.8/31" => range of 2


            "255.0.0.7", n = 16
            "255.0.0.7" ~ "255.0.0.22"
             0000 0111     0001 0110
            
            ["255.0.0.7/31"]
             0000 0111 => "255.0.0.7/32" => 1
             0000 1XXX => "255.0.0.8/29" => range of 8
             0001 00XX => "255.0.0.16/30" => range of 4
             0001 010X => "255.0.0.20/31" => range of 2
             0001 0110 => "255.0.0.22/31" => 1

            Compute the range. What if 255 255 255 255 + 10 like that? Is it 0 0 0 9?

            12:04
            x & -x gives a 1 at kth position in a bin where 2^k address range might be covered.
            So states
            size
            remaining

            convert the ip to num
            get x
            get k the range
            halve k until it fits to the remaining
            convert the ip to str and append /x and append to res
            ip + k the size
            remaining - k
        '''
        
        ipInt = self.ipStrToInt(ip)
        remaining = n
        blocks = []
        while remaining > 0:
            # print(remaining)
            rangeSize = ipInt & -ipInt if ipInt else pow(2,32) # This is to see how many we could cover at ip at the moment. when 0.0.0.0 and n>0 we still wanna cover the adddresses but 0 & -0 is 0. So we need to pow(2, 32) go to max and reduce
            while remaining < rangeSize and rangeSize != 0:
                rangeSize //= 2
            
            postfix = 0
            tmp = rangeSize
            while tmp > 1:
                tmp //= 2
                postfix += 1
            prefixRange = 32 - postfix # (rangeSize.bit_length() - 1)  # 32
            blocks.append(self.idIntToStr(ipInt, prefixRange))

            ipInt += rangeSize
            remaining -= rangeSize

        return blocks

    def ipStrToInt(self, ip):
        ipInt = 0
        for part in ip.split('.'):
            ipInt = (ipInt << 8) + int(part)
        return ipInt
    
    def idIntToStr(self, ip, prefix):
        ipStrParts = [0] * 4
        for i in range(4):
            part = ip & 255 
            ipStrParts[3-i] = str(part)
            ip = ip >> 8
        return ".".join(ipStrParts) + "/" + str(prefix)











