def construct_sentence(file_path):
    with open(file_path, 'r') as file:

        # Read the text file line by line, separate words and numbers from the space between and store in a dictionary
        nums_and_chars = {}
        for i in [line.rstrip('\n') for line in file]:
            if " " in i:
                nums_and_chars[int(i[:i.index(" ")])] = i[i.index(" ") + 1:]

        # Sort dictionary by keys
        sorted_dict = {key: nums_and_chars[key] for key in sorted(nums_and_chars)}

        # Store the position of every line's last word in the position variable
        position = 1
        sentence = []
        for k, v in sorted_dict.items():
            if k > 1:
                position += k
            if position > max(sorted_dict.keys()):
                break

            # Append every value of that position in the sentence list
            sentence.append(sorted_dict[position])

        # Join list members by a space and print the sentence
        sentence = ' '.join(sentence)

        return sentence


print(construct_sentence('file.txt'))

