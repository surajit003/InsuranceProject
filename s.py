from enum import Enum


class PolicyStatus(Enum):
    NEW = 0
    ACCEPTED = 1
    PAID = 2


breakpoint()
p = PolicyStatus.NEW.name
print(p)