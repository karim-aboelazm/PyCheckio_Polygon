def get_cipher(plain):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(get_cipher("hello"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_cipher("hello") == {4: {4: {8: {3: {7: {0: {4: {}, 7: {}}, 2: {2: {}}}, 8: {3: {}}}}}}}
    assert get_cipher("This is a plain text.") == {1: {3: {2: {1: {4: {7: {4: {1: {0: {}, 2: {}, 7: {}},4: {9: {}}, 8: {3: {}}},
                                                 6: {8: {1: {}, 4: {}, 9: {}}}}}, 9: {5: {5: {6: {1: {}, 4: {}}, 8: {}}}}}}}},
                                                 2: {6: {2: {8: {4: {9: {5: {2: {}, 8: {}}}}}}}}, 3: {2: {4: {1: {4: {8: {3: {0: {}, 
                                                 2: {}}}}}, 3: {5: {3: {5: {4: {}, 7: {}}}}}}}}}

    print("Coding complete? Click 'Check' to earn cool rewards!")
