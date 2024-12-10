# %%
import numpy as np
path_to_input = "input.txt"

# %%
def load_input_data(path: str) -> np.array:
    with open(path, "r") as file:
        lines = file.readlines()
    filtred_lines = []
    for line in lines:
        line = line.replace("\n", "")
        filtred_lines.append(line)
        
    data = np.array([list(map(int, line)) for line in filtred_lines])
    return data

# %%
def get_zero_coords(map: np.array) -> list:
    (x_coords, y_coords)= np.where(map == 0)
    coords = [(x_coord, y_coord) for x_coord, y_coord in zip(x_coords, y_coords)]
    return coords
def is_coord_inside(map_size: list, coord: list) -> bool:
    if coord[0] < 0 or coord[1] < 0 or coord[0] >= map_size[0] or coord[1] >= map_size[1]:
        return False
    return True

# %%
def calculate_for_cell(map: np.array, coord: list, number: int, mask: np.array, flag: bool) -> int:
    if is_coord_inside(map_size=map.shape, coord=coord) is False:
        return 0, mask 
    try:
        cell =  map[coord[0], coord[1]]
        if cell  == number + 1:
            if cell == 9:
                if flag is True:
                    if mask[coord[0], coord[1]] == False:
                        mask[coord[0], coord[1]] = True
                        return 1, mask
                else:
                    return 1, mask
            else: 
                result, mask =  find_higher_value(map, coord, number + 1, mask, flag)
                return result, mask
    except:
        pass
    return 0, mask

def find_higher_value(map: np.array, coord: list, number: int, mask: np.array, flag: bool) -> int:
    results = 0
    result, mask = calculate_for_cell(map, [coord[0]-1, coord[1]], number, mask, flag)
    results +=result
    result, mask = calculate_for_cell(map, [coord[0]+1, coord[1]], number, mask, flag)
    results +=result
    result, mask = calculate_for_cell(map, [coord[0], coord[1]-1], number, mask, flag)
    results +=result
    result, mask = calculate_for_cell(map, [coord[0], coord[1]+1], number, mask, flag)
    results +=result
    return results, mask


# %%
def count_all_trailheads(map: np.array, coords: list, flag: bool) -> int:

    score= 0
    for coord in coords:
        # calculate trailheads
        number = 0
        mask = np.zeros(map.shape, dtype=bool)
        result, _ = find_higher_value(map, coord, number, mask, flag)
        score += result
    return score

# %%
data = load_input_data(path=path_to_input)
coords = get_zero_coords(map=data)
score = count_all_trailheads(map=data, coords=coords, flag=True)
print("Part one result: " + str(score))

score = count_all_trailheads(map=data, coords=coords, flag=False)
print("Part two result: " + str(score))


