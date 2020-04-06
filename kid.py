import global_params


class Kid:
    def __init__(self, ineligible_names={'male': [], 'female': []}):
        self.sex = self.choose_sex()
        self.name = self.choose_name(ineligible_names=ineligible_names)

    def choose_sex(self):
        rand_choice = global_params.rand_wrapper(1, 2)

        sex = ''
        if rand_choice == 1:
            sex = 'male'

        elif rand_choice == 2:
            sex = 'female'

        return sex

    def choose_name(self, ineligible_names):
        name_found = False

        while not name_found:
            rand_choice = global_params.rand_wrapper(1, global_params.num_names)
            name = global_params.names[self.sex][rand_choice-1]

            name_found = name not in ineligible_names[self.sex]

        return name