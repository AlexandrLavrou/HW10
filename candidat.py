class Candidates:

    def __init__(self, ident, name, picture, position, skills):
        self.ident = ident
        self.name = name
        self.pictures = picture
        self.position = position
        self.skills = skills

    def __repr__(self):
        return f"{self.name}\n{self.position}\n{self.skills}\n\n"

    def get_candy_info(self):
        return f"<pre>\n" \
               f"<h4>Имя кандидата - {self.name}\n" \
               f"Позиция {self.position}\n" \
               f"Навыки: {self.skills}\n" \
               f"</pre>\n\n"

    def get_foto_candy(self):
        return f"\n<img src={self.pictures}>\n"

    def chek_candy_from_ID(self, input_id):
        if int(input_id) == int(self.ident):
            return self.get_foto_candy() + self.get_candy_info()


    def chek_candy_skill(self, input_skill):
        temp_skills = self.skills.split(", ")
        get_candy_with_skill = ""
        for skill in temp_skills:
            if input_skill.lower() == skill.lower():
                get_candy_with_skill = self.get_candy_info()
            else:
                continue
            return get_candy_with_skill


