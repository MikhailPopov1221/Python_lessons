titles = ["ЛИЧНАЯ_ИНФОРМАЦИЯ", "ОБРАЗОВАНИЕ", "ОПЫТ_РАБОТЫ", "НАВЫКИ"]


def parse_resume_data(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as fl:
            content = fl.readlines()
        
        sections = {} 
        current_section = None

        for line in content:
            if line == "\n":
                continue
            if line.strip().upper() in titles:
                current_section = line.strip().upper()
                sections[current_section] = []
            else:
                sections[current_section].append(line.strip())
            
        resume_data = {}
        
        if "ЛИЧНАЯ_ИНФОРМАЦИЯ" in sections:
            personal_info = {}
            for line in sections["ЛИЧНАЯ_ИНФОРМАЦИЯ"]:
                key, value = line.strip().split(":",1)
                personal_info[key.strip()] = value.strip()
            resume_data["personal_info"] = personal_info
            
        if "ОБРАЗОВАНИЕ" in sections:
            education = []
            current_education = {}
            
            for line in sections["ОБРАЗОВАНИЕ"]:
                key, value = line.strip().split(":",1)
                
                if key.strip().lower() == 'название' and current_education:
                    education.append(current_education)
                    current_education = {}
                
                current_education[key.strip()] = value.strip()
            
            if current_education:
                education.append(current_education)
            resume_data['education'] = education
            
        if "ОПЫТ_РАБОТЫ" in sections:
            experience = []
            current_experience = {}
            
            for line in sections["ОПЫТ_РАБОТЫ"]:
                key, value = line.strip().split(":",1)
                
                if key.strip().lower() == 'компания' and current_experience:
                    experience.append(current_experience)
                    current_experience = {}
                
                current_experience[key.strip()] = value.strip()
            
            if current_experience:
                experience.append(current_experience)
            resume_data['experience'] = experience
        
        if "НАВЫКИ" in sections:
            resume_data["skills"] = sections["НАВЫКИ"]
            
        return resume_data
        
    except FileNotFoundError:
        print(f" Ошибка, файл {filename} не найден")
        return None
    
    except Exception as e:
        print(f"Возникла ошибка при парсинге файла")
        print(type(e), e)
        return None