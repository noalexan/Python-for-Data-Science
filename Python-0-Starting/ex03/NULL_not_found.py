def NULL_not_found(object: any) -> int:
    print(type(object))
    return int(object == object) if object else 0
