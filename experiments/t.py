
def get_mapping(elevations):
    mapping = {"W":1, "S":2,"G":3,"T":4,"R":5}

    array = sum(elevations, [])
    return [mapping.get(i) for i in array]


# is the elevation greator than 100 then we can say that the data contains a hightland
def is_max_above_100(elevations):
    array = sum(elevations, []) # we can also use itertools.chain to make it faster.
    if max(array)>100:
        return True
    else:
        return False

def calculate_sum(elevations):
    sizes = {"W":0, "S":0,"G":0,"T":0,"R":0}

    array = sum(elevations, [])
    for i in array:
        if i == "W":
            sizes["W"]+=1
        if i == "S":
            sizes["S"]+=1
        if i == "G":
            sizes["G"]+=1
        if i == "T":
            sizes["T"]+=1
        if i == "R":
            sizes["R"]+=1
    return sizes

def return_max(sizes):
    # label, count
    return max(sizes.items())[0], max(sizes.items())[1]

def get_boundary_elements(features):
    sizes = {"W":0, "S":0,"G":0,"T":0,"R":0}
    m = n = len(features)
    elements = []
    for i in range(len(features)): 
        for j in range(len(features)): 
            if (i == 0): 
                elements.append( features[i][j])
            elif (i == m-1): 
                elements.append( features[i][j])
            elif (j == 0): 
                elements.append( features[i][j]) 
            elif (j == n-1): 
                elements.append( features[i][j])
            else: 
                pass
    for i in elements:
        if i == "W":
            sizes["W"]+=1
        if i == "S":
            sizes["S"]+=1
        if i == "G":
            sizes["G"]+=1
        if i == "T":
            sizes["T"]+=1
        if i == "R":
            sizes["R"]+=1
    return sizes

# if there 'T' max in a dataset then we can say that the data contains a forest
def get_forest(sizes):
    if return_max(sizes)[1] == "T":
        return "forest"
    else:
        return ""


# if the boundary contains more number of grass then we can say that the data contains a river
def get_river(sizes):
    if return_max(sizes)[1] == "G":
        return "river"
    else:
        return ""

def get_highland(elevations):
    if is_max_above_100(elevations):
        return "highland"
    else:
        return ""
    

def findTerrainTypes(elevations, features):
    features_with_mapping = get_mapping(features)
    prediction = []
    prediction.append(get_highland(elevations))
    sizes_f = calculate_sum(elevations)
    prediction.append(get_forest(sizes_f))
    sizes_r = get_boundary_elements(features)
    prediction.append(get_river(sizes_r))
    return prediction
