def is_valid_mapping(mapping, encoded_strings, target):
    total_sum = sum(encoded_strings[:-1])  # Sum of all encoded strings except the target
    return total_sum == encoded_strings[-1] and len(set(mapping.values())) == len(set(mapping.keys()))

def encode_string(s, mapping):
    return int("".join(str(mapping[char]) for char in s))

def find_mapping(arr, target):
    unique_chars = set("".join(arr) + target)
    if len(unique_chars) > 10:
        return None  # More than 10 unique characters, not possible to map to 0-9

    def backtrack(index, mapping):
        if index == len(unique_chars):
            encoded_strings = [encode_string(s, mapping) for s in arr] + [encode_string(target, mapping)]
            if is_valid_mapping(mapping, encoded_strings, target):
                return mapping
            return None

        char = list(unique_chars)[index]
        for digit in range(10):
            if digit not in mapping.values():
                mapping[char] = digit
                result = backtrack(index + 1, mapping)
                if result:
                    return result
                mapping[char] = None

        return None

    initial_mapping = {char: None for char in unique_chars}
    return backtrack(0, initial_mapping)

# Example usage:
arr = ["SEND", "MORE"]
target = "MONEY"
mapping = find_mapping(arr, target)

if mapping:
    print("Yes, mapping is possible:", mapping)
else:
    print("No, mapping is not possible.")
