import os

project_structure = {
    'sales-automation': [
        'config.py', 'requirements.txt', 'run.py', 'README.md',
        {'app': [
            '__init__.py', 'routes.py', 'models.py', 'forms.py',
            {'utils': ['scraping.py', 'email_handler.py', 'analytics.py', '__init__.py']},
            {'templates': [
                'base.html', 'index.html', 'scrape.html', 'campaigns.html', 'create_campaign.html',
                'analytics.html', 'leads.html', 'scripts.html', 'email_template.html'
            ]},
            {'static': [
                {'css': ['style.css']},
                {'js': ['scripts.js', 'validation.js']},
                {'images': ['pixel.png']}
            ]}
        ]}
    ]
}

def create_structure(base_path, structure):
    for item in structure:
        if isinstance(item, dict):
            for folder, contents in item.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                create_structure(folder_path, contents)
        else:
            file_path = os.path.join(base_path, item)
            with open(file_path, 'w') as f:
                f.write(f'# Placeholder for {os.path.basename(file_path)}')

# Define the base folder for the project
base_folder = 'sales-automation'

# Create the base folder and the project structure
os.makedirs(base_folder, exist_ok=True)
create_structure(base_folder, project_structure[base_folder])
print("Project structure generated successfully.")
