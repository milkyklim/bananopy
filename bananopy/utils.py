def unfold_keys(dictionary):
    r = []
    for k, v in dictionary.items():
        if isinstance(v, dict):
            r += unfold_keys(v)
            continue
        if isinstance(v, list):
            for el in v:
                r += unfold_keys(el)
            continue
        r.append(k)
    return r
