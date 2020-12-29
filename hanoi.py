
def hanoi(disc, from_, to):
	def move(d, f, t, v):
		if d <= 1:
			print(f'Move disc {d} from {f} to {t}.')
		else:
			move(d-1, f, v, t)
			print(f'Move disc {d} from {f} to {t}')
			move(d-1, v, t, f)

	move(disc, from_, to, 2)

if __name__ == '__main__':
	hanoi(3, 1, 3)
