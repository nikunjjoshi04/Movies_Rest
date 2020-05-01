try:
    from .production import *
except ImportError:
    try:
        from .dev import *
    except ImportError:
        try:
            from .home_dev import *
        except ImportError as e:
            print('Plz import settings ...!!!')
            print('Settings file is Not Found')
