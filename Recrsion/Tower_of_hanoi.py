def tower(n, source, auxiliary, target):
    if n <= 0:
        return f"{source} has {n} disk cannot apply Tower of Hanoi."

    if n==1:
        print( f"move {n} from {source} to {target}")
        return

    tower(n - 1, source, target, auxiliary)
    print(f"move {n} from {source} to {target},")
    tower(n - 1, auxiliary, source, target)

tower(3, 'a', 'b', 'c')