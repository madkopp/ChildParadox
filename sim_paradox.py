from family import Family
import global_params


families = []
for n in range(global_params.num_families):
    new_family = Family()
    families.append(new_family)

families_with_at_least_one_girl = []
for family in families:
    at_least_one_girl = False
    for kid in family.kids:
        at_least_one_girl |= kid.sex == 'female'

    if at_least_one_girl:
        families_with_at_least_one_girl.append(family)

families_with_two_girls = []
for family in families_with_at_least_one_girl:
    two_girls = True
    for kid in family.kids:
        two_girls &= kid.sex == 'female'

    if two_girls:
        families_with_two_girls.append(family)

print('Percent with two girls (no name): ', len(families_with_two_girls)/len(families_with_at_least_one_girl))




chosen_name = 1
families_with_chosen_name = []
for family in families_with_at_least_one_girl:
    if chosen_name in family.kid_names['female']:
        families_with_chosen_name.append(family)

families_with_two_girls = []
for family in families_with_chosen_name:
    two_girls = True
    for kid in family.kids:
        two_girls &= kid.sex == 'female'

    if two_girls:
        families_with_two_girls.append(family)

print('Percent with two girls (given name): ', len(families_with_two_girls)/len(families_with_chosen_name))