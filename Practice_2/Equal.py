from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    all_the_same = bool


    bol = True
    for i in range(len(all_the_same)):
        if all_the_same[0] != all_the_same[i]:
            bol = False
            break
        else:
            bol = True
            i+=1
    if bol == True:
        return True
    else:
        return False
        
    #print("all_the_same (%s) == %s" %(all_the_same,bol))
    


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    #assert all_the_same([1, 1, 1]) == True
    #assert all_the_same([1, 2, 1]) == False
    #assert all_the_same(['a', 'a', 'a']) == True
    #assert all_the_same([]) == True
    #assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")