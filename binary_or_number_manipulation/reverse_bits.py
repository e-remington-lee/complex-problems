'''
This is a very famous question if you are targeting companies like Apple,Qualcomm,Cisco,Juniper Networks etc especially for System/Networking position.
In one of the above companies for which I was interviewing for[I don't want to name the company] , I had given a solution using "for-loop", but interviewer wanted a solution without using a loop. At that point of time, I was not much familiar using Mask , [basically approach-3 of this article] and I answered ,"Sorry I am not aware of it".
However, interviewer was really kind and he led me to the solution. These are the question which he led up to the solution.

Interviewer:- "Do you know how to swap alternate bits in a number"?
Me:- I was aware of this and mentioned , (x&0xaaaaaaaa)>>1|x&(0x55555555)<<1
Interview:- "Ohk, this will form the first step, and now can think of a mask which can swap two bits at time, think how can you change 0xaaaaaaaa and 0x55555555",
Me:- Luckily, it clicked me at that point of time for the mask:- 0xcccccccc and 0x33333333
Interview:- "Good, do you know how to change endianness that is convert little to big endian and from big endian to little endiannes"
Me:- Here, it my mind clicked for the mask 0xff00ff00 and 0xf0f0f0f0, [though some modification is required]
Finally, I was able to come up with the solution.
There are many interview questions that forms a part of this solution like "swap alternating bits of a number", "converting endianness of a number". These are also being asked in these companies.

PS:- This approach has become entrenched in my mind, simply because of the way the "Interviewer" led me to the solution. I thank him for that
'''

class Solution:
    def manual_reconstruct(self, n):
        response, power = 0, 31 # if we have 1101, the first digit is 1 << 3, gives us 1000
        while n:
            response += (n & 1) << power
            power -= 1
            n >>= 1
        return response

print(0xff)