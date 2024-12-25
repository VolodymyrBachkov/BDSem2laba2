from engine import initialize_engine
from queries import add_sample_data, display_data
from alembic.config import Config
from alembic import command

def run_migrations_online():
    alembic_cfg = Config("alembic.ini")
    # Застосовуємо міграції до останньої версії
    command.upgrade(alembic_cfg, "head")

def apply_migration_by_version(version):
    alembic_cfg = Config("alembic.ini")
    # Застосовуємо міграцію за вказаною версією
    command.upgrade(alembic_cfg, version)

def show_tables(session):
    print("\n== Таблиці ==")
    display_data(session)

def add_sample_information(session):
    print("\n== Додавання прикладів даних ==")
    add_sample_data(session)

def create_migration():
    alembic_cfg = Config("alembic.ini")
    command.revision(alembic_cfg, message="Added new migration", autogenerate=True)
    print("Міграцію створено!")

def configure_logging():
    logging_state = input("Увімкнути логування? (y/n): ").strip().lower()
    if logging_state == 'y':
        logging_state = True
    else:
        logging_state = False
    return logging_state

def menu():
    session = initialize_engine(logging_state=True)  # Ініціалізація сеансу з логуванням

    while True:
        print("\n== Меню ==")
        print("1. Показати таблиці")
        print("2. Додати приклади інформації")
        print("3. Створити міграцію")
        print("4. Застосувати міграцію")
        print("  4.1. Застосувати останню")
        print("  4.2. Застосувати (вказати версію)")
        print("5. Налаштування логування")
        print("6. Вихід")
        
        choice = input("Оберіть опцію (1-6): ").strip()

        if choice == '1':
            show_tables(session)
        elif choice == '2':
            add_sample_information(session)
        elif choice == '3':
            create_migration()
        elif choice == '4':
            sub_choice = input("Оберіть опцію:\n1. Застосувати останню\n2. Застосувати за версією\n").strip()
            if sub_choice == '1':
                run_migrations_online()
            elif sub_choice == '2':
                version = input("Введіть версію міграції: ").strip()
                apply_migration_by_version(version)
        elif choice == '5':
            logging_state = configure_logging()
            session = initialize_engine(logging_state=logging_state)  # Ініціалізація сеансу з логуванням
        elif choice == '6':
            print("Вихід...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

def main():
    menu()

if __name__ == "__main__":
    main()
