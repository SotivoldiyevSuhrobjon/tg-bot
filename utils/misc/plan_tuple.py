async def rate_tariff(data):
    quality = []
    dict_list = data
    tuple_list = [(d['name'], d['id']) for d in dict_list]
    for i, t in enumerate(tuple_list, start=0):
        new_tuple = t
        quality.append(t)
    return quality


# async def get_name_id_price(data):
#     quality = []
#     dict_list = data
#     tuple_list = [(d['period'], d['price']) for d in dict_list]
#     for i, t in enumerate(tuple_list, start=0):
#         new_tuple = t
#         quality.append(t)
#     print(quality)
#     return quality

# async def rate_muddat(data):
#     quality = []
#     dict_list = data
#     print(dict_list)
#     tuple_list = [(d['period']) for d in dict_list]
#     for i, t in enumerate(tuple_list, start=0):
#         # new_tuple = t
#         quality.append(t)
#     print(quality)
#     return quality
