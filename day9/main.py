# %%
import re

# %%
input_text = "2333133121414131402"

# %%
def get_files_block(size: int, value: int) -> list:
    return ([str(value) for element in range(size)])

def get_free_block(size: int) -> str:
    return (["." for element in range(size)])

def generate_disc(input_text: str) -> list:
    disc = []
    id = 0
    for i, value in enumerate(input_text):
        if i % 2 == 0:
            element = get_files_block(size=int(value), value=id)
            disc.extend(element)
            id = id + 1
        else:
            element = get_free_block(size=int(value))
            disc.extend(element)
    return disc

# %%
def replace_two_elements(disc: list, id1: int, id2: int) -> list:

    disc[id1] = disc[id2]
    disc[id2] = "."
    return disc

def get_last_number(disc: list)-> int:

    result = 0
    for id, element in enumerate(disc):
        try:
            value = int(element)
            result = id
        except:
            pass
    return result

def move_file_blocks(disc: list) -> list:
    while True:
        print("Disc:", end=" ")
        to_print = "".join(disc)
        print(to_print)
        result = disc.index(".")
        last_num_id = get_last_number(disc)
        if last_num_id < result:
            break
        disc = replace_two_elements(disc, result, last_num_id)
    return disc

def get_control_sum(text: list) -> int:
    sum = 0
    with open("SumControl.txt", "w") as file:
        for id, element in enumerate(text):
            try:
                sum = sum + int(element)*id
                file.write(str(id) + " * " + element + " = " + str(sum) + "\n")
            except:
                pass 
    return sum

# %%
input_text = input()
print("Calculating")
disc = generate_disc(input_text=input_text)
with open("disc.txt", "w") as file:
    to_file = "".join(disc)
    file.write(to_file)

disc = move_file_blocks(disc=disc)
print("Control sum....")
result = get_control_sum(disc)
print("Result: " + str(result))

# %%


# %%



