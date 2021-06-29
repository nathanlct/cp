n_tri = 1
n_pent = 1
n_hexa = 1

val_tri = 1
val_pent = 1
val_hexa = 1

while True:
    if val_tri == val_pent and val_pent == val_hexa:
        print(n_tri, val_tri)
        if val_tri > 40755:
            break

    n_tri += 1
    val_tri = n_tri * (n_tri + 1) // 2

    while val_pent < val_tri:
        n_pent += 1
        val_pent = n_pent * (3*n_pent - 1) // 2
    
    while val_hexa < val_tri:
        n_hexa += 1
        val_hexa = n_hexa * (2*n_hexa - 1)

    