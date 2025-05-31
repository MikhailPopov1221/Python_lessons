

def generate_html(resume_data: dict):
    if not resume_data:
        output = """
        <html>
        <body>
        <h1>Ошибка, данные для генерации страницы не найдены </h1>
        </body>
        </html>
        """
        return output
    
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Моё Резюме</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Roboto', Arial, sans-serif;
                line-height: 1.6;
                background-color: #f5f7fa;
                color: #333;
                padding: 20px;
            }
            
            .container {
                max-width: 850px;
                margin: 0 auto;
                background-color: #fff;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                overflow: hidden;
            }
            
            header {
                background: linear-gradient(135deg, #3a7bd5, #3a6073);
                color: white;
                padding: 30px;
                text-align: center;
            }
            
            header h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
                font-weight: 700;
            }
            
            header p {
                margin-bottom: 8px;
                font-size: 1.1rem;
            }
            
            .contact-info {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 15px;
            }
            
            .contact-info p {
                margin: 0 15px;
                display: flex;
                align-items: center;
            }
            
            .contact-info i {
                margin-right: 5px;
            }
            
            .content {
                padding: 30px;
            }
            
            .section {
                margin-bottom: 30px;
            }
            
            h2 {
                color: #3a7bd5;
                border-bottom: 2px solid #3a7bd5;
                padding-bottom: 10px;
                margin-bottom: 20px;
                font-weight: 500;
            }
            
            .item {
                margin-bottom: 25px;
                position: relative;
                padding-left: 20px;
            }
            
            .item:before {
                content: '';
                position: absolute;
                left: 0;
                top: 8px;
                height: calc(100% - 8px);
                width: 2px;
                background-color: #3a7bd5;
            }
            
            .item:last-child {
                margin-bottom: 0;
            }
            
            .item:last-child:before {
                height: 15px;
            }
            
            .item h3 {
                color: #2c3e50;
                font-weight: 500;
                margin-bottom: 5px;
            }
            
            .date {
                color: #7f8c8d;
                font-size: 0.9rem;
                margin-bottom: 8px;
            }
            
            .skills {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }
            
            .skill {
                background: linear-gradient(135deg, #3a7bd5, #3a6073);
                color: white;
                padding: 8px 15px;
                border-radius: 20px;
                font-size: 0.9rem;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s;
            }
            
            .skill:hover {
                transform: translateY(-2px);
            }
            
            .footer {
                text-align: center;
                padding: 20px;
                background-color: #f9f9f9;
                color: #7f8c8d;
                font-size: 0.9rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
    """
    
    if "personal_info" in resume_data:
        personal_info = resume_data["personal_info"]
        html += f"""
            <header>
                <h1>{personal_info.get("Имя", "Имя не найдено")}</h1>
                <p>{personal_info.get("Профессия", "Профессия не найдена")}</p>
                <div class="contact-info">
                    <p>{personal_info.get("Email", "")}</p>
                    <p>{personal_info.get("Телефон", "")}</p>
                    <p>{personal_info.get("Город", "")}</p>
                </div>
            </header>
        """
    
    html += """
        <div class="content">
    """
    
    if "education" in resume_data:
        html += """
            <div class="section">
                <h2>Образование</h2>
        """
        
        for edu in resume_data["education"]:
            html += f"""
                <div class="item">
                    <h3>{edu.get("Название", "")}</h3>
                    <div class="date"> {edu.get("Годы", "")}</div>
                    <p>{edu.get("Специальность", "")}</p>
                </div>
            """
             
        html += """
        </div> 
        """
        
    if "experience" in resume_data:
        html += """
            <div class="section">
                <h2>Опыт работы</h2>
        """
        
        for exp in resume_data["experience"]:
            html += f"""
                <div class="item">
                    <h3>{exp.get("Компания", "")}</h3>
                    <h3>{exp.get("Должность", "")}</h3>
                    <div class="date"> {exp.get("Годы", "")}</div>
                    <p>{exp.get("Описание", "")}</p>
                </div>
            """
            
        html += "</div>"
        
    if "skills" in resume_data:
        html += """
            <div class="section">
                <h2>Навыки</h2>
                <div class="skills">
        """
        
        for skill in resume_data["skills"]:
            html += f'<div class="skill">{skill}</div>'
        
        html += """
            </div>
        </div>
        """
        
    html += """
                </div>
                <div class="footer">
                    Создано с помощью "Генератор резюме" 2025г.
                </div>
            </div>
        </body>
    </html>
    """
    
    return html
        


def save_html_to_file(html_data: str, filename: str):
    try:
        with open(filename, "w", encoding="utf-8") as fl:
            fl.write(html_data)
        
    except Exception as e:
        print(e)
        print("Не удалось сохранить данные в файл")
        