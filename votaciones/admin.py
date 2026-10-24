from django.contrib import admin
from .models import Voto

# Intentar registrar el modelo de candidatos sin importar cómo se llame en models.py
try:
    from .models import Candidato
    admin.site.register(Candidato)
except ImportError:
    try:
        from .models import Participante
        admin.site.register(Participante)
    except ImportError:
        pass

# Intentar registrar los demás modelos si existen
try:
    from .models import Edicion
    admin.site.register(Edicion)
except ImportError:
    pass

try:
    from .models import Categoria
    admin.site.register(Categoria)
except ImportError:
    pass

admin.site.register(Voto)