# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: ResearchCatalog
def switch_profile():
    profiles = {
        'researcher': {
            'name': 'Researcher',
            'role': 'Активный исследователь',
            'permissions': ['read', 'write', 'publish'],
            'current_profile': 'researcher',
        },
        'reviewer': {
            'name': 'Reviewer',
            'role': 'Рецензент',
            'permissions': ['read', 'review'],
            'current_profile': None,
        },
        'admin': {
            'name': 'Admin',
            'role': 'Администратор',
            'permissions': ['read', 'write', 'publish', 'manage'],
            'current_profile': None,
        }
    }
    print("=== ResearchCatalog: Управление профилями ===")
    print(f"Текущий профиль: {profiles['researcher']['current_profile'] or 'Нет'}")
    for name, profile in profiles.items():
        if profile['current_profile'] == name:
            print(f"Активен: {profile['name']} ({profile['role']})")
    print("\nДоступные профили:")
    for name, profile in profiles.items():
        if profile['current_profile'] is None:
            print(f"  - {profile['name']} ({profile['role']}) — {profile['permissions']}")
    print("\nДля переключения профиля выполните:")
    print("  from ResearchCatalog import switch_profile")
    print("  switch_profile(profile_name='admin')")
    print("  print(f\"Сейчас вы: {profiles[profile_name]['name']}\")")
    return profiles
