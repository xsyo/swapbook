
def get_avatar_path(instanse, filename):
    file_type = filename.split('.')[-1]
    return f'avatarts/avatar-{instanse.id}.{file_type}'