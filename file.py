import time
mp = {}
def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [word.strip() for word in file]

def is_compound(word, word_set):
    if word in mp:
        return mp[word]
    
    l = len(word)
    
    for i in range(l):
        prefix = word[:i+1]
        suffix = word[i+1:]
        
        if (prefix in word_set and suffix in word_set) or (prefix in word_set and is_compound(suffix, word_set)):
            mp[word] = True
            return True
    
    mp[word] = False
    return False

def find_all_concatenated_words(words):
    n = len(words)
    result = []
    st = set(words)
    
    for i in range(n):
        if is_compound(words[i], st):
            result.append(words[i])
    
    return result

def fetch_longest_and_second_longest(words):
    if not words:
        return None, None

    longest = ""
    second_longest = ""

    for word in words:
        if len(word) > len(longest):
            second_longest = longest
            longest = word
        elif len(word) > len(second_longest):
            second_longest = word

    return longest, second_longest

def main():
    start_time = time.time()

    input_file_paths = ['Input_01.txt', 'Input_02.txt']
    all_words = []

    for file_path in input_file_paths:
        all_words.extend(read_words_from_file(file_path))


        arr = find_all_concatenated_words(all_words)

        # Remove the longest compounded word from the list and find the second longest

        longest,sec_longest = fetch_longest_and_second_longest(arr)

        end_time = time.time()
        processing_time = end_time - start_time

        # Display results
        print(f"Longest Compounded Word: {longest}")
        print(f"Second Longest Compounded Word: {sec_longest}")
        print(f"Time taken to process: {processing_time * 1000} milli seconds")

if __name__ == "__main__":
    main()
