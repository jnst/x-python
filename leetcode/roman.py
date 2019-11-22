from typing import Dict


class Solution:

    roman_dict: Dict[str, int] = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    @classmethod
    def roman_to_int(cls, s: str) -> int:
        n = cls.roman_dict[s]
        return n
