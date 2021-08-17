def get_plain(cipher):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(get_plain({1: {6: {3: {}}}, 2: {6: {5: {}}, 9: {0: {}, 5: {}}},3: {4: {5: {}}}, 6: {6: {4: {}}}}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_plain({1: {6: {3: {}}}, 2: {6: {5: {}}, 9: {0: {}, 5: {}}}, 3: {4: {5: {}}}, 6: {6: {4: {}}}}) == 'python'
    assert get_plain({1: {1: {8: {8: {8: {0: {0: {1: {3: {9: {6: {}, 9: {}}}, 6: {2: {0: {}}}}},
                      1: {8: {0: {1: {1: {}, 7: {}, 9: {}},7: {0: {}, 2: {}, 3: {}}}, 5: {7: {8: {}}}}}, 
                      2: {1: {0: {2: {2: {}}}}, 4: {8: {9: {0: {}, 5: {}}}}}}}}}}}}) == 'You can read me.'

    print("Coding complete? Click 'Check' to earn cool rewards!")
