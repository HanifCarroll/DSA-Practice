fun list_product (xs: int list) =
    if null xs
    1
    else hd xs * list_product(tl xs)