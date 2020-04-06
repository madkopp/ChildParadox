from kid import Kid
import global_params


class Family:
    def __init__(self):
        self.kid_names = {'male':   [],
                          'female': []}
        self.kids = self.make_kids()

    def make_kids(self):
        kids = []
        for n in range(global_params.num_kids_per_family):
            new_kid = Kid(ineligible_names=self.kid_names)
            self.kid_names[new_kid.sex].append(new_kid.name)
            kids.append(new_kid)

        return kids

    def add_kid_names(self, kid_names):
        for sex in kid_names:
            self.kid_names[sex] += kid_names[sex]