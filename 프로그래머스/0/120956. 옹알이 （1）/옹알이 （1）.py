def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        i = 0
        while i < len(word):
            for sound in valid_sounds:
                if word[i:i+len(sound)] == sound:
                    i += len(sound)
                    break
            else:
                break
        if i == len(word):
            count += 1

    return count