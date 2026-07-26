class Solution:
    def isValid(self, s: str) -> bool:
        #as stack in a Last in first otut data structure we can utilie it 
        #here what we can do is we can push the opening bracket if we found
        #closing bracket we will check if the last appended bracket was a 
        #match , if that is true then we would pop it else we would return
        #False straight away if the elem is not a closing bracket we will
        #append it in the end if the stack is not empty its false else true
        l,r =  0 , len(s)-1
        stack =list()
        closeToOpen = {']':'[',')':'(','}':'{'}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else :
                    return False 
            else :
                stack.append(c)
        return False if stack else True








































































        