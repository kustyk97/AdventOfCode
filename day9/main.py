# %%
import re

# %%
#input_text = "2333133121414131402"

# %%
def get_files_block(size: int, value: int) -> str:
    result =  "".join([str(value) for element in range(size)])
    return result

def get_free_block(size: int) -> str:
    result = "".join(["." for element in range(size)])
    return result

# %%
def generate_disc(input_text: str) -> str:
    disc = ""
    id = 0
    for i, value in enumerate(input_text):
        if i % 2 == 0:
            element = get_files_block(size=int(value), value=id)
            disc = disc + element
            id = id + 1
        else:
            element = get_free_block(size=int(value))
            disc = disc + element
    return disc

# %%
def replace_two_elements(disc: str, id1: int, id2: int) -> str:

    disc = [element for element in disc]
    disc[id1] = disc[id2]
    disc[id2] = "."
    disc = "".join(disc)
    return disc

# %%
def move_file_blocks(disc: str) -> str:
    while True:
        result = re.search(r"[.]", disc)
        result2 = re.search(r"[0-9]", disc[::-1])
        last_num_id = len(disc) - result2.start() -1 
        if last_num_id < result.start():
            break
        disc = replace_two_elements(disc, result.start(), last_num_id)
    return disc

# %%
def get_control_sum(text: str) -> int:
    sum = 0
    for id, element in enumerate(text):
        try:
            sum = sum + int(element)*id
        except:
            pass 
    return sum

# %%
input_text = input()
disc = generate_disc(input_text=input_text)
disc = move_file_blocks(disc=disc)
result = get_control_sum(disc)
print(result)

# %%


# %%



