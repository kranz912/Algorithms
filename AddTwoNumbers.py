class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def displayLinkedList(l1:ListNode):
        while(True):
            print(l1.value,end='->')


            if l1 == None:
                break

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
                break
            elif number2==None:
                break





number = ListNode(5)
number.next = ListNode(5)


solution = Solution()
solution.addTwoNumbers(l1=number, l2=number)
