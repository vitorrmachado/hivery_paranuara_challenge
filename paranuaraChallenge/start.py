import sys
import os.path

django_starter = 'python manage.py '

def install_django_2():
    answer = input("Do you want to install Django 2 to run this code [n/y]? ")
    if(answer.lower() == 'y'):
        print('Installing Django 2.')
        import pip
        pip.main(['install', 'django==2.0'])

def first_call():
    return not os.path.isfile('no_migration')

def generate_migrations():
    os.system(django_starter + "makemigrations")
    os.system(django_starter + "migrate")

    file = open('no_migration', 'w')
    file.close()

if __name__ == "__main__":

    if(sys.version_info[0] < 3):
        print("Sorry! This project requires at least Python 3.")
    else:
        try:
            import django
            if django.VERSION[0] > 2:
                install_django_2()
        except ImportError:
            install_django_2()

        print("Initializing Django:")

        if first_call():
            generate_migrations()

        if len(sys.argv) > 1 and sys.argv[1] == 'test':
            os.system(django_starter + "test")
        else:
            os.system(django_starter + "runserver --noreload")