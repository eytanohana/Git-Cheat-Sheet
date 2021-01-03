
def hanoi(disc):
    def move(d, f, t, v):
        if d <= 1:
            yield f'Move disc {d} from {f} to {t}.'
        else:
            yield from move(d - 1, f, v, t)
            yield f'Move disc {d} from {f} to {t}.'
            yield from move(d - 1, v, t, f)

    return move(disc, 1, 3, 2)


if __name__ == '__main__':
    for m in hanoi(10):
        print(m)
