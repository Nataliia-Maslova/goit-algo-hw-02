from collections import deque


def is_palindrome(s) -> bool:
    s = s.lower().replace(" ", "")
    deq = deque(s)

    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False
        else:
            return True
    # Якщо пройшли всі символи і не було різних то поліндром

print(is_palindrome("Pan ap"))