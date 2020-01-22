class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def displayLinkedList(self,l1:ListNode):
        while(True):
            if l1 == None:
                break
            print(l1.val,end='->')
            l1=l1.next


    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        number1 = l1
        number2 = l2
        lsum = None
        carryon =0
        while(True):
            currentDigit = lsum

            sum = number1.val+number2.val+carryon
            if(sum>=10):
                carryon = 1
                sum = sum%10
            else:
                carryon =0

            number1 = number1.next
            number2 = number2.next


            currentDigit = ListNode(sum)
            if lsum == None:
                lsum = currentDigit
            else:
                lsum.next = currentDigit


            if number1==None:

                while number2 != None:
                    number2 = number2.next

                if(carryon>0):
                    print(carryon)
                    lsum.next = ListNode(carryon)
                break
            elif number2==None:
                if(carryon>0):
                    lsum.next = ListNode(carryon)
                break
        return lsum




number = ListNode(6)
number.next = ListNode(5)


solution = Solution()
sum= solution.addTwoNumbers(l1=number, l2=number)

solution.displayLinkedList(l1=sum)
