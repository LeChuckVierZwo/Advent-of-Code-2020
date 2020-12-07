from functools import reduce

with open("input") as f:
    groups = f.read().split("\n\n")

solve_part_one = 0
solve_part_two = 0
for group in groups:
    set_part_one = reduce(set.union, map(set, group.split()))
    set_part_two = reduce(set.intersection, map(set, group.split()))
    solve_part_one += len(set_part_one)
    solve_part_two += len(set_part_two)

print(solve_part_one)
print(solve_part_two)

#two-liner
#part 1
part_one = 0
for group in open("input").read().split("\n\n"):    from functools import reduce; union_set = reduce(set.union, map(set, group.split())); part_one +=  len(union_set); print(part_one);
#part 2
part_two = 0
for group in open("input").read().split("\n\n"):    from functools import reduce; intersection_set = reduce(set.intersection, map(set, group.split())); part_two += len(intersection_set); print(part_two);