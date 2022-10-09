#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Dict,Optional,Tuple,Any
from enum import Enum


class Action(Enum):
    LOGIN = "login"
    LOGOUT = "logout"
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"
    BALANCE = "balance"


class UserState(Enum):
    AUTHORIZED = "authorized"
    UNAUTHORIZED = "unauthorized"


class State:
    def __init__(self):
        super().__init__()

    @staticmethod
    def checker(param: Optional, password: str, balance: int) -> Tuple[bool, int, str]:
        if not password:
            return False, 0, UserState.UNAUTHORIZED.value
        return True, balance, UserState.AUTHORIZED.value

def checker(param: Optional, password: str, balance: int) -> Tuple[bool, int, str]:
    if not password:
        return False,0,UserState.UNAUTHORIZED.value
    return True,balance,UserState.AUTHORIZED.value

# Implement the transition_tablehere
transition_table = {
    UserState.UNAUTHORIZED: [
        [Action.LOGIN.value, checker, UserState.AUTHORIZED.value]
    ],
    UserState.AUTHORIZED: [
        [Action.LOGOUT.value, checker, UserState.UNAUTHORIZED.value],
        [Action.BALANCE.value, checker, UserState.AUTHORIZED.value],
        [Action.WITHDRAW.value, checker, UserState.AUTHORIZED.value],
        [Action.DEPOSIT.value, checker, UserState.UNAUTHORIZED.value],
    ]
}

# Implement the init_state here
init_state = UserState.UNAUTHORIZED

# Look for the implementation of the ATM class in the below Tail section

if __name__ == "__main__":
    class ATM:
        def __init__(self, init_state: State, init_balance: int, password: str, transition_table: Dict):
            self.state = init_state
            self._balance = init_balance
            self._password = password
            self._transition_table = transition_table

        def next(self, action: Action, param: Optional) -> Tuple[bool, Optional[Any]]:
            try:
                for transition_action, check, next_state in self._transition_table[self.state]:
                    print(action, transition_action)
                    if action == transition_action:
                        passed, new_balance, res = check(param, self._password, self._balance)
                        if passed:
                            self._balance = new_balance
                            self.state = next_state
                            return True, res
            except KeyError:
                pass
            return False, None


    if __name__ == "__main__":
        # fptr = open(os.environ['OUTPUT_PATH'], 'w')
        password = input()
        init_balance = int(input())
        atm = ATM(init_state, init_balance, password, transition_table)
        q = int(input())
        for _ in range(q):
            action_input = input().split()
            action_name = action_input[0]
            try:
                action_param = action_input[1]
                if action_name in ["deposit", "withdraw"]:
                    action_param = int(action_param)
            except IndexError:
                action_param = None
            success, res = atm.next(action_name, action_param)
            if res is not None:
                # fptr.write(f"Success={success} {atm.state} {res}\n")
                print(f"Success={success} {atm.state} {res}\n")
            else:
                # fptr.write(f"Success={success} {atm.state}\n")
                print(f"Success={success} {atm.state}\n")

        # fptr.close()
