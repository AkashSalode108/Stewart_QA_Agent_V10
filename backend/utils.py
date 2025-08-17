import os

ALLOWED_EXTENSIONS = ['.xlsx', '.csv', '.pdf']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in [ext.strip('.') for ext in ALLOWED_EXTENSIONS]

def save_uploaded_file(uploaded_file, save_dir="data"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path
