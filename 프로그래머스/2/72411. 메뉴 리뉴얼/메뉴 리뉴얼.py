from itertools import combinations

def solution(orders, course):

    result = []
    
    dict_ = {count: {} for count in course} 
    max_ = max(len(order) for order in orders)
    
    for order in orders:
        for count in course:
            order_combi = list(combinations(list(order), count))
            for combi in order_combi:
                menus = "".join(sorted(combi))
                if menus in dict_[count]:
                    dict_[count][menus] += 1
                else:
                    dict_[count][menus] = 1
                    
    # print(dict_)
    for num, menus in dict_.items():
        if len(menus) == 0:
            continue
        max_count = max(list(menus.values()))
        if max_count < 2:
            continue
        for menu, count in menus.items():
            if count == max_count:
                result.append(menu)
      
    return sorted(result)
                